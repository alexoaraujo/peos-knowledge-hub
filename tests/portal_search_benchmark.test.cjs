'use strict';
const { test } = require('node:test');
const assert = require('node:assert/strict');
const { performance } = require('node:perf_hooks');
const fs = require('node:fs');
const path = require('node:path');
const {indexEntries, query} = require('../hub-portal/search.js');

const catalog = JSON.parse(fs.readFileSync(path.join(__dirname,'../hub-portal/catalog.json'),'utf8'));
const indexed = indexEntries(catalog.entries);

test('repeatable 500-query faceted-search benchmark over canonical catalog', (t) => {
  assert.equal(indexed.length,797);
  const scenarios = [
    {query:'seguranca',namespace:'canonical'},
    {query:'projeto',sort:'title'},
    {category:'Prompts Mestres e Universais'},
    {namespace:'bpd'},
    {tag:'Segurança'}
  ];
  const samples = [];
  for(let i = 0; i < 500; i++){
    const filters = scenarios[i % scenarios.length];
    const start = performance.now();
    const results = query(indexed,filters);
    samples.push(performance.now()-start);
    assert.ok(Array.isArray(results));
    assert.ok(results.length <= 797);
  }
  samples.sort((a,b)=>a-b);
  const mean = samples.reduce((a,b)=>a+b,0) / samples.length;
  const p95 = samples[Math.ceil(samples.length * .95) - 1];
  t.diagnostic(JSON.stringify({
    kind:'PEOS_SEARCH_BENCHMARK',
    environment:process.platform,
    items:catalog.entries.length,
    queries:samples.length,
    mean_ms:+mean.toFixed(3),
    p95_ms:+p95.toFixed(3)
  }));
  // This is a hang/regression guard, NOT a production performance SLA.
  assert.ok(p95 < 2000, 'p95 exceeds conservative CI sanity limit');
});
