'use strict';
/* Static, fail-closed preview of existing PEOS PMU/workflow contracts. */
(function () {
  const form = document.getElementById('plan-form');
  const goal = document.getElementById('plan-goal');
  const pmuSelect = document.getElementById('plan-pmu');
  const submit = document.getElementById('plan-submit');
  const message = document.getElementById('plan-message');
  const output = document.getElementById('plan-output');
  let pmus = new Map(), workflows = new Map(), references = new Map();

  const line = (tag, value) => {
    const node = document.createElement(tag);
    node.textContent = value;
    return node;
  };
  function fail(reason) {
    pmus = new Map(); workflows = new Map(); references = new Map();
    pmuSelect.disabled = true;
    submit.disabled = true;
    output.replaceChildren();
    output.hidden = true;
    message.textContent = reason;
  }
  function verify(p, w, catalog) {
    if (!Array.isArray(p.prompts) || p.prompts.length !== 10 ||
        !Array.isArray(w.workflows) || w.workflows.length !== 10 ||
        !Array.isArray(catalog.entries) || catalog.entries.length !== 797) {
      throw Error('Manifestos incompletos');
    }
    const entries = new Map(catalog.entries.filter(e =>
      e.namespace === 'canonical' && /^[0-9]{4}$/.test(e.id) &&
      /^[0-9a-f]{64}$/.test(e.sha256)).map(e => [e.id, e]));
    if (entries.size !== 659) throw Error('Catálogo canônico inválido');
    const pmuIndex = new Map(catalog.entries.filter(e =>
      e.namespace === 'pmu' && /^PMU-0(?:0[1-9]|10)$/.test(e.id) &&
      /^[0-9a-f]{64}$/.test(e.sha256)).map(e => [e.id, e]));
    if (pmuIndex.size !== 10) throw Error('Índice PMU incompleto');
    const resultP = new Map(), resultW = new Map();
    for (const item of p.prompts) {
      if (!/^PMU-0(?:0[1-9]|10)$/.test(item.id) || item.status !== 'PROPOSED' ||
          !/^[0-9a-f]{64}$/.test(item.sha256) ||
          !pmuIndex.has(item.id) || pmuIndex.get(item.id).sha256 !== item.sha256 ||
          pmuIndex.get(item.id).status !== item.status ||
          !Array.isArray(item.refs) || !item.refs.length ||
          new Set(item.refs).size !== item.refs.length ||
          item.refs.some(id => !entries.has(id)) ||
          !Array.isArray(item.stages) || item.stages.length !== 6 ||
          item.stages.some(name => typeof name !== 'string' || !name.trim()) ||
          resultP.has(item.id)) {
        throw Error('PMU ou referências inválidas');
      }
      resultP.set(item.id, item);
    }
    for (const wf of w.workflows) {
      if (!/^WF-0(?:0[1-9]|10)$/.test(wf.id) || !resultP.has(wf.pmu_id) ||
          wf.id !== 'WF-' + wf.pmu_id.slice(4) ||
          wf.version !== resultP.get(wf.pmu_id).version ||
          !Array.isArray(wf.steps) ||
          wf.steps.length !== resultP.get(wf.pmu_id).stages.length ||
          wf.steps.some((step, index) =>
            step.id !== 'S' + String(index + 1).padStart(2, '0') ||
            step.name !== resultP.get(wf.pmu_id).stages[index] ||
            step.required_gate !== 'G' + index ||
            step.evidence_required !== true) ||
          resultW.has(wf.pmu_id)) {
        throw Error('Workflow sem gates de evidência');
      }
      resultW.set(wf.pmu_id, wf);
    }
    if (resultW.size !== 10) throw Error('Workflow ausente');
    return {pmus: resultP, workflows: resultW, entries};
  }
  function preview(event) {
    event.preventDefault();
    output.replaceChildren();
    output.hidden = true;
    const request = goal.value.trim();
    const p = pmus.get(pmuSelect.value);
    const workflow = workflows.get(pmuSelect.value);
    if (!request || request.length > 500 || !p || !workflow) {
      message.textContent = 'Informe um objetivo válido e selecione um PMU disponível.';
      return;
    }
    output.append(
      line('h3', p.id + ' · ' + p.name),
      line('p', 'Objetivo: ' + request),
      line('p', 'Status editorial: PROPOSED · Execução: PLAN_ONLY · Permissões: nenhuma'),
      line('p', 'Workflow: ' + workflow.id + ' · Gates: NOT_EVALUATED · Publicação: BLOCKED')
    );
    const stepsHeading = line('h4', 'Etapas planejadas (não iniciadas)');
    output.append(stepsHeading);
    const steps = document.createElement('ol');
    for (const step of workflow.steps) {
      steps.append(line('li', step.name + ' · ' + step.required_gate +
        ' · BLOCKED_UNTIL_VERIFIED · evidência obrigatória'));
    }
    output.append(steps);
    output.append(line('h4', 'Dependências canônicas do PMU'));
    const links = document.createElement('ul');
    for (const id of p.refs) {
      const entry = references.get(id);
      const link = document.createElement('a');
      // Canonical paths are strictly restricted to existing catalog paths.
      const path = entry.path;
      if (!/^prompts\/[0-9]{4}-[0-9]{4}\/[0-9]{4}\.md$/.test(path)) {
        message.textContent = 'Referência com caminho inválido; plano indisponível.';
        output.replaceChildren();
        return;
      }
      link.href = '../' + path;
      link.textContent = id + ' · ' + entry.title;
      link.title = 'SHA-256: ' + entry.sha256;
      const li = document.createElement('li');
      li.append(link);
      links.append(li);
    }
    output.append(links);
    output.hidden = false;
    message.textContent = 'Prévia gerada localmente: nenhuma ação executada ou aprovada.';
  }
  document.addEventListener('peos:select-pmu', event => {
    const selected = event.detail && event.detail.pmuId;
    if (typeof selected !== 'string' || !pmus.has(selected) ||
        pmuSelect.disabled || !workflows.has(selected)) {
      message.textContent = 'Plano indisponível: contratos do PMU ainda não verificados.';
      return;
    }
    pmuSelect.value = selected;
    output.replaceChildren();
    output.hidden = true;
    message.textContent = 'PMU ' + selected + ' selecionado. Informe o objetivo para visualizar o plano.';
    document.getElementById('plan-preview').scrollIntoView({ block: 'start' });
    goal.focus();
  });
  form.addEventListener('submit', preview);
  Promise.all([
    fetch('../pmu/manifest.json').then(r => { if (!r.ok) throw Error('PMU'); return r.json(); }),
    fetch('../workflows/manifest.json').then(r => { if (!r.ok) throw Error('Workflow'); return r.json(); }),
    fetch('catalog.json').then(r => { if (!r.ok) throw Error('Catálogo'); return r.json(); })
  ]).then(([p, w, catalog]) => {
    const state = verify(p, w, catalog);
    pmus = state.pmus; workflows = state.workflows; references = state.entries;
    pmuSelect.replaceChildren();
    for (const entry of pmus.values()) {
      const option = document.createElement('option');
      option.value = entry.id;
      option.textContent = entry.id + ' · ' + entry.name + ' (PROPOSED)';
      pmuSelect.append(option);
    }
    pmuSelect.disabled = false;
    submit.disabled = false;
    message.textContent = 'Pronto para compor uma prévia somente leitura.';
  }).catch(() => fail('Contratos não verificados: prévia indisponível. O catálogo continua acessível.'));
})();
