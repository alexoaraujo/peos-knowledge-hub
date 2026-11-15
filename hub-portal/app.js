'use strict';
/* Accessible read-only catalog viewer. No HTML injection, no external mutations. */
const byId = id => document.getElementById(id);
const ui = {q:byId('q'),ns:byId('ns'),sort:byId('sort'),results:byId('results'),count:byId('result-count'),stats:byId('stats'),more:byId('more'),clear:byId('clear'),error:byId('load-error')};
const norm = value => String(value ?? '').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
let list = [], filtered = [], visible = 0;
const PAGE_SIZE = 40;

function safePromptPath(value) {
  if (typeof value !== 'string' || !value || value.startsWith('/') || value.includes('\\')) return null;
  const segments = value.split('/');
  if (segments.some(s => !s || s === '.' || s === '..' || !/^[\w\-.]+$/.test(s))) return null;
  return '../' + segments.map(encodeURIComponent).join('/');
}
function appendPrompt(p) {
  const article = document.createElement('article');
  article.className = 'item';
  const tag = document.createElement('div');
  tag.className = 'tag';
  tag.textContent = String(p.namespace || '').toUpperCase() + ' · ' + String(p.id || '');
  const title = document.createElement('h2'); title.textContent = p.title || 'Sem título';
  const category = document.createElement('p'); category.textContent = p.category || 'Sem categoria';
  const status = document.createElement('p'); status.textContent = 'Status: ' + (p.status || 'Não informado');
  const path = safePromptPath(p.path);
  article.append(tag, title, category, status);
  if (path) {
    const link = document.createElement('a');
    link.href = path; link.textContent = 'Abrir prompt original';
    article.append(link);
  }
  ui.results.append(article);
}
function showMore() {
  const next = Math.min(visible + PAGE_SIZE, filtered.length);
  for (let i = visible; i < next; i++) appendPrompt(filtered[i]);
  visible = next;
  ui.more.hidden = visible >= filtered.length;
  ui.count.textContent = filtered.length + ' resultado(s); exibindo ' + visible + '.';
  if (!filtered.length) {
    const empty = document.createElement('p');
    empty.className = 'empty-state';
    empty.textContent = 'Nenhum prompt encontrado. Tente outros termos ou limpe os filtros.';
    ui.results.append(empty);
  }
}
function render() {
  const words = norm(ui.q.value).trim().split(/\s+/).filter(Boolean);
  const namespace = ui.ns.value;
  filtered = list.filter(p => (!namespace || p.namespace === namespace) &&
    words.every(w => norm([p.id,p.title,p.category,p.group,...(Array.isArray(p.tags)?p.tags:[])].join(' ')).includes(w)));
  if (ui.sort.value === 'title') filtered.sort((a,b)=>String(a.title).localeCompare(String(b.title),'pt-BR'));
  if (ui.sort.value === 'id') filtered.sort((a,b)=>String(a.id).localeCompare(String(b.id),'pt-BR'));
  ui.results.replaceChildren(); visible = 0; showMore();
  ui.clear.disabled = !ui.q.value && !ui.ns.value && ui.sort.value === 'default';
}
function addStat(label, count) {
  const box = document.createElement('div'); box.className = 'stat';
  const number = document.createElement('strong'); number.textContent = count ?? 0;
  const caption = document.createElement('small'); caption.textContent = label;
  box.append(number, caption); ui.stats.append(box);
}
function load() {
  ui.error.hidden = true;
  ui.count.textContent = 'Carregando catálogo...';
  fetch('catalog.json').then(response => {
    if (!response.ok) throw Error('HTTP ' + response.status);
    return response.json();
  }).then(data => {
    if (!Array.isArray(data.entries) || !data.summary || !data.summary.by_namespace) throw Error('Formato de índice inválido');
    list = data.entries;
    ui.stats.replaceChildren();
    addStat('Entradas',data.summary.total_prompts);
    addStat('Canônicos',data.summary.by_namespace.canonical);
    addStat('BPD',data.summary.by_namespace.bpd);
    addStat('PMUs',data.summary.by_namespace.pmu);
    addStat('Workflows',data.summary.total_workflows);
    render();
  }).catch(() => {
    ui.count.textContent = 'Não foi possível carregar o catálogo.';
    ui.error.hidden = false;
    ui.more.hidden = true;
  });
}
ui.q.addEventListener('input', render);
ui.ns.addEventListener('change', render);
ui.sort.addEventListener('change', render);
ui.more.addEventListener('click', showMore);
ui.clear.addEventListener('click', () => {
  ui.q.value = ''; ui.ns.value = ''; ui.sort.value = 'default';
  render(); ui.q.focus();
});
byId('retry').addEventListener('click', load);
load();
