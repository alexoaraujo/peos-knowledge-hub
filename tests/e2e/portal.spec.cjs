'use strict';
const { test, expect } = require('@playwright/test');
const catalog = require('../../hub-portal/catalog.json');
const url = '/hub-portal/';

test('loads all catalog entries and progressively renders 40 at a time', async ({ page }) => {
  await page.goto(url);
  await expect(page.locator('#result-count')).toHaveText('797 resultado(s); exibindo 40.');
  await expect(page.locator('.item')).toHaveCount(40);
  await page.getByRole('button', { name: 'Exibir mais resultados' }).click();
  await expect(page.locator('.item')).toHaveCount(80);
  await expect(page.locator('#result-count')).toHaveText('797 resultado(s); exibindo 80.');
});

test('filters intersect category, group, tags, namespace and ID, then reset', async ({ page }) => {
  const sample = catalog.entries.find(p => p.namespace === 'bpd' && p.tags.length && p.category && p.group);
  expect(sample).toBeTruthy();
  await page.goto(url);
  await page.locator('#ns').selectOption(sample.namespace);
  await page.locator('#category').selectOption(sample.category);
  await page.locator('#group').selectOption(sample.group);
  await page.locator('#tag').selectOption(sample.tags[0]);
  await page.locator('#q').fill(sample.id);
  await expect(page.locator('.item')).toHaveCount(1);
  await expect(page.locator('.item .tag')).toContainText(sample.id);
  const link = page.locator('.item a');
  await expect(link).toHaveAttribute('href', /\.md$/);
  await page.getByRole('button',{name:'Limpar filtros'}).click();
  await expect(page.locator('#q')).toHaveValue('');
  await expect(page.locator('#ns')).toHaveValue('');
  await expect(page.locator('#category')).toHaveValue('');
  await expect(page.locator('#group')).toHaveValue('');
  await expect(page.locator('#tag')).toHaveValue('');
  await expect(page.locator('#result-count')).toHaveText('797 resultado(s); exibindo 40.');
});

test('search is accent-insensitive and empty states are explicit', async ({ page }) => {
  await page.goto(url);
  await page.locator('#q').fill('seguranca');
  await expect(page.locator('.item').first()).toBeVisible();
  await page.locator('#q').fill('peos-no-such-entry-987654');
  await expect(page.locator('#result-count')).toHaveText('0 resultado(s); exibindo 0.');
  await expect(page.locator('.empty-state')).toContainText('Nenhum prompt encontrado');
});

test('keyboard skip link, visible labels, and responsive widths', async ({ page }) => {
  await page.setViewportSize({width:375,height:750});
  await page.goto(url);
  await page.keyboard.press('Tab');
  await expect(page.locator('.skip-link')).toBeFocused();
  await page.keyboard.press('Enter');
  await expect(page.locator('#catalog-results')).toBeFocused();
  for (const id of ['q','ns','category','group','tag','sort']) {
    await expect(page.locator('label[for="'+id+'"]')).toBeVisible();
  }
  let overflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
  expect(overflow).toBeFalsy();
  await page.setViewportSize({width:320,height:720});
  overflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
  expect(overflow).toBeFalsy();
});

test('fetch failure exposes retry and recovers without hard reload', async ({ page }) => {
  await page.route('**/hub-portal/catalog.json', route => route.abort());
  await page.goto(url);
  await expect(page.locator('#load-error')).toBeVisible();
  await expect(page.locator('#result-count')).toHaveText('Não foi possível carregar o catálogo.');
  await page.unroute('**/hub-portal/catalog.json');
  await page.getByRole('button',{name:'Tentar novamente'}).click();
  await expect(page.locator('#result-count')).toHaveText('797 resultado(s); exibindo 40.');
  await expect(page.locator('#load-error')).toBeHidden();
});
