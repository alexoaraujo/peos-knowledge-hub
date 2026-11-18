'use strict';
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const search = require('../hub-portal/search.js');
const data = JSON.parse(fs.readFileSync(path.join(__dirname, '../hub-portal/catalog.json'), 'utf8'));
const entries = data.entries;
const index = search.indexEntries(entries);

test('canonical baseline, all namespaces and facet values remain available', () => {
  assert.equal(entries.length, 797);
  assert.equal(search.query(index).length, 797);
  assert.equal(search.query(index, {namespace:'canonical'}).length, 659);
  assert.equal(search.query(index, {namespace:'bpd'}).length, 128);
  assert.equal(search.query(index, {namespace:'pmu'}).length, 10);
  assert.ok(search.options(entries,'category').length > 0);
  assert.ok(search.options(entries,'group').length > 0);
  assert.ok(search.options(entries,'tag').length > 0);
});

test('facets exact-match category, group and tag, including accent insensitive selection', () => {
  const tagEntry = entries.find(e => Array.isArray(e.tags) && e.tags.length);
  assert.ok(tagEntry);
  const category = tagEntry.category;
  const group = tagEntry.group;
  const tag = tagEntry.tags[0];
  assert.ok(search.query(index, {category, group, tag}).some(e => e.id === tagEntry.id && e.namespace === tagEntry.namespace));
  assert.ok(search.query(index, {category:'never-existing-category'}).length === 0);
  assert.ok(search.query(index, {tag:'never-existing-tag'}).length === 0);
  const accent = search.norm(category);
  assert.equal(search.query(index,{category:accent}).length, search.query(index,{category}).length);
});

test('combined filtering is intersection and query matches title and ID', () => {
  const entry = entries.find(e => e.namespace === 'canonical');
  const result = search.query(index,{namespace:'canonical',category:entry.category,query:entry.id});
  assert.ok(result.some(e => e.id === entry.id));
  assert.ok(result.every(e => e.namespace === 'canonical' && e.category === entry.category));
  assert.equal(search.query(index,{query:'not-found-xyz-938743'}).length,0);
});

test('sorting does not mutate the manifest order', () => {
  const before = entries.map(e => e.id);
  const results = search.query(index,{sort:'title'});
  assert.equal(results.length,797);
  assert.deepEqual(entries.map(e=>e.id),before);
  const idResults = search.query(index,{sort:'id'});
  assert.equal(idResults.length,797);
});

test('100 searches over the full catalog return consistent result counts', () => {
  const filters = {query:'seguranca',namespace:'canonical'};
  const count = search.query(index,filters).length;
  for (let i=0;i<100;i++) assert.equal(search.query(index,filters).length,count);
});
