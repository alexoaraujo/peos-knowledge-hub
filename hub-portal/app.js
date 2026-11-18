'use strict';
/* Accessible read-only catalog viewer. No HTML injection, no external mutations. */
const byId = id => document.getElementById(id);
const ui = {q:byId('q'),ns:byId('ns'),category:byId('category'),group:byId('group'),tag:byId('tag'),sort:byId('sort'),results:byId('results'),count:byId('result-count'),stats:byId('stats'),more:byId('more'),clear:byId('clear'),error:byId('load-error')};
const search = window.PEOSSearch;
let list = [], indexed = [], filtered = [], visible = 0;
let pmuReferenceState = 'loading', pmuReferences = new Map();
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
  if (p.namespace === 'pmu') {
    const metadata = document.createElement('p');
    if (pmuReferenceState !== 'ready') {
      metadata.textContent = pmuReferenceState === 'error'
        ? 'Referências canônicas indisponíveis; consulte o manifesto PMU.'
        : 'Carregando referências canônicas...';
      article.append(metadata);
    } else {
      const refs = pmuReferences.get(p.id);
      if (!refs) {
        metadata.textContent = 'Referências canônicas não verificadas.';
        article.append(metadata);
      } else {
        const details = document.createElement('details');
        const summary = document.createElement('summary');
        summary.textContent = 'Referências canônicas (' + refs.length + ') · plano, não execução';
        details.append(summary);
        const entries = document.createElement('ul');
        for (const ref of refs) {
          const item = list.find(e => e.namespace === 'canonical' && e.id === ref);
          const destination = item && safePromptPath(item.path);
          if (!destination || !/^[0-9a-f]{64}$/.test(item.sha256)) continue;
          const li = document.createElement('li');
          const a = document.createElement('a');
          a.href = destination;
          a.textContent = ref + ' · ' + item.title;
          a.title = 'SHA-256: ' + item.sha256;
          li.append(a);
          entries.append(li);
        }
        if (entries.children.length === refs.length) {
          details.append(entries);
          article.append(details);
        } else {
          metadata.textContent = 'Referências incompletas; confira o manifesto PMU.';
          article.append(metadata);
        }
      }
    }
  }
  if (p.namespace === 'pmu') {
    const planButton = document.createElement('button');
    planButton.type = 'button';
    planButton.className = 'pmu-plan-action';
    planButton.textContent = 'Visualizar plano deste PMU';
    planButton.addEventListener('click', () => {
      document.dispatchEvent(new CustomEvent('peos:select-pmu', { detail: { pmuId: p.id } }));
    });
    article.append(planButton);
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
  filtered = search.query(indexed, {
    query:ui.q.value,
    namespace:ui.ns.value,
    category:ui.category.value,
    group:ui.group.value,
    tag:ui.tag.value,
    sort:ui.sort.value
  });
  ui.results.replaceChildren(); visible = 0; showMore();
  ui.clear.disabled = !ui.q.value && !ui.ns.value && !ui.category.value && !ui.group.value &&
    !ui.tag.value && ui.sort.value === 'default';
}
function facetOptions(select, key, title) {
  const values = search.options(list, key);
  select.replaceChildren();
  const first = document.createElement('option');
  first.value = ''; first.textContent = title;
  select.append(first);
  for (const value of values) {
    const option = document.createElement('option');
    option.value = value; option.textContent = value;
    select.append(option);
  }
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
    indexed = search.indexEntries(list);
    facetOptions(ui.category, 'category', 'Todas as categorias');
    facetOptions(ui.group, 'group', 'Todos os grupos');
    facetOptions(ui.tag, 'tag', 'Todas as tags');
    ui.stats.replaceChildren();
    addStat('Entradas',data.summary.total_prompts);
    addStat('Canônicos',data.summary.by_namespace.canonical);
    addStat('BPD',data.summary.by_namespace.bpd);
    addStat('PMUs',data.summary.by_namespace.pmu);
    addStat('Workflows',data.summary.total_workflows);
    render();
    fetch('../pmu/manifest.json').then(response => {
      if (!response.ok) throw Error('HTTP ' + response.status);
      return response.json();
    }).then(manifest => {
      if (!Array.isArray(manifest.prompts) || manifest.prompts.length !== 10) throw Error('Manifesto PMU inválido');
      const items = new Map();
      for (const entry of manifest.prompts) {
        if (!/^PMU-[0-9]{3}$/.test(entry.id) || !Array.isArray(entry.refs) ||
            entry.refs.length === 0 || entry.refs.some(ref => !/^[0-9]{4}$/.test(ref))) {
          throw Error('Referência PMU inválida');
        }
        if (items.has(entry.id)) throw Error('PMU duplicado');
        items.set(entry.id, entry.refs);
      }
      pmuReferences = items;
      pmuReferenceState = 'ready';
      render();
    }).catch(() => {
      pmuReferenceState = 'error';
      render();
    });
  }).catch(() => {
    ui.count.textContent = 'Não foi possível carregar o catálogo.';
    ui.error.hidden = false;
    ui.more.hidden = true;
  });
}
ui.q.addEventListener('input', render);
ui.ns.addEventListener('change', render);
ui.category.addEventListener('change', render);
ui.group.addEventListener('change', render);
ui.tag.addEventListener('change', render);
ui.sort.addEventListener('change', render);
ui.more.addEventListener('click', showMore);
ui.clear.addEventListener('click', () => {
  ui.q.value = ''; ui.ns.value = ''; ui.category.value = ''; ui.group.value = ''; ui.tag.value = ''; ui.sort.value = 'default';
  render(); ui.q.focus();
});
byId('retry').addEventListener('click', load);
load();
