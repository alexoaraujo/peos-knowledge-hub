'use strict';
/** Pure, dependency-free faceted search for the 797-entry PEOS catalog. */
(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.PEOSSearch = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  const norm = value => String(value ?? '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().trim();
  const str = value => typeof value === 'string' ? value : '';
  const tagsOf = item => Array.isArray(item.tags) ? item.tags.filter(x => typeof x === 'string') : [];

  function indexEntries(entries) {
    if (!Array.isArray(entries)) throw new TypeError('entries must be an array');
    return entries.map((item, order) => ({
      item,
      order,
      searchable: norm([item.id, item.title, item.category, item.group, ...tagsOf(item)].map(str).join(' ')),
      category: norm(item.category),
      group: norm(item.group),
      tags: tagsOf(item).map(norm)
    }));
  }
  function options(entries, key) {
    const values = new Map();
    for (const e of entries) {
      const fields = key === 'tag' ? tagsOf(e) : [str(e[key])];
      for (const value of fields) if (value.trim() && !values.has(norm(value))) values.set(norm(value), value);
    }
    return [...values.values()].sort((a,b) => a.localeCompare(b, 'pt-BR'));
  }
  function query(index, filters = {}) {
    const terms = norm(filters.query).split(/\s+/).filter(Boolean);
    const category = norm(filters.category), group = norm(filters.group), tag = norm(filters.tag);
    const namespace = norm(filters.namespace);
    const matches = index.filter(e =>
      (!namespace || norm(e.item.namespace) === namespace) &&
      (!category || e.category === category) &&
      (!group || e.group === group) &&
      (!tag || e.tags.includes(tag)) &&
      terms.every(term => e.searchable.includes(term))
    );
    const sort = filters.sort || 'default';
    if (sort === 'title') matches.sort((a,b) => str(a.item.title).localeCompare(str(b.item.title),'pt-BR') || a.order-b.order);
    if (sort === 'id') matches.sort((a,b) => str(a.item.id).localeCompare(str(b.item.id),'pt-BR') || a.order-b.order);
    return matches.map(e => e.item);
  }
  return Object.freeze({norm, indexEntries, options, query});
});
