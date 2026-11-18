'use strict';
const { test, expect } = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;

async function audit(page) {
  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa'])
    .analyze();
  const issues = results.violations.map(v => ({
    id: v.id,
    impact: v.impact,
    description: v.description,
    nodes: v.nodes.map(n => ({target:n.target,summary:n.failureSummary}))
  }));
  expect(issues).toEqual([]);
}

test('automated WCAG A/AA checks on initial catalog', async ({page}) => {
  await page.goto('/hub-portal/');
  await expect(page.locator('#result-count')).toHaveText('797 resultado(s); exibindo 40.');
  await audit(page);
});
test('automated WCAG A/AA checks with interactive filters', async ({page}) => {
  await page.goto('/hub-portal/');
  await expect(page.locator('#result-count')).toHaveText('797 resultado(s); exibindo 40.');
  await page.locator('#q').fill('seguranca');
  await expect(page.locator('.item').first()).toBeVisible();
  await audit(page);
});
test('automated WCAG A/AA checks in empty-result state at mobile width', async ({page}) => {
  await page.setViewportSize({width:375,height:780});
  await page.goto('/hub-portal/');
  await page.locator('#q').fill('peos-no-such-entry-987654');
  await expect(page.locator('.empty-state')).toBeVisible();
  await audit(page);
});
