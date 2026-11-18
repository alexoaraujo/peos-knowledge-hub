# Auditoria técnica dos dez PMUs — PEOS Knowledge Hub

Esta auditoria distingue **consistência técnica automatizada** de **homologação editorial**, autorização de execução e direitos de publicação. O código de auditoria é `tools/audit_pmu_readiness.py`, acionado em `.github/workflows/integridade-biblioteca.yml`. Não altera textos da biblioteca, manifests, IDs ou hashes.

## Matriz de decisão

| PMU | Escopo conforme manifesto | Verificação técnica | Parecer editorial |
| --- | --- | --- | --- |
| PMU-001 | Prompt Universal PEOS | CI `audit_pmu_readiness.py` | PENDENTE |
| PMU-002 | Criação de Projeto 360° | CI `audit_pmu_readiness.py` | PENDENTE |
| PMU-003 | Auditoria Integral 360° | CI `audit_pmu_readiness.py` | PENDENTE |
| PMU-004 | Continuidade Autônoma Controlada | CI `audit_pmu_readiness.py` | PENDENTE |
| PMU-005 | Engenharia Full Stack | CI `audit_pmu_readiness.py` | PENDENTE |
| PMU-006 | UX/UI e Design System | CI `audit_pmu_readiness.py` | PENDENTE |
| PMU-007 | Segurança e Compliance | CI `audit_pmu_readiness.py` | PENDENTE |
| PMU-008 | Dados e Inteligência Artificial | CI `audit_pmu_readiness.py` | PENDENTE |
| PMU-009 | DevOps, SRE e Release | CI `audit_pmu_readiness.py` | PENDENTE |
| PMU-010 | Modernização e Migração | CI `audit_pmu_readiness.py` | PENDENTE |

A coluna técnica deve ser interpretada com o **resultado do workflow em SHA verificável**; a presença do código não é prova de execução ou de aprovação.

## Contratos validados automaticamente

- Dez PMUs, dez workflows, dez agentes e 659 IDs canônicos existentes.
- ID, título, finalidade, versão, referências e seis etapas presentes no texto original e consistentes com `pmu/manifest.json`.
- Hash SHA-256 do arquivo de cada PMU coincide com o manifesto; caminhos devem ficar em `pmu/prompts/`.
- Entradas obrigatórias `OBJETIVO` e `PROJETO`, política `fail_closed` e `require_evidence` mantida.
- Um workflow por PMU, seis etapas correspondentes a `S01...S06`, gates `G0...G5` e evidência obrigatória em todas as etapas.
- Nenhum workflow declara mutações de produção sem autorização explícita.
- Um agente por PMU com `status=DESIGN_ONLY`, `execution_mode=PLAN_ONLY`, `permissions=[]` e revisão humana prevista.
- `status=PROPOSED` mantido e nenhuma aprovação editorial declarada por CI.

## Cenários negativos de contexto e autorização

O motor e a CLI foram fortalecidos para **rejeitar objetivos vazios** e declarar explicitamente quando a entrada obrigatória `PROJETO` está ausente. O campo `context.status=INCOMPLETE` não equivale a aprovação; mesmo com `--project` informado, o plano permanece `PLAN_ONLY`, com `NO_EXTERNAL_MUTATIONS`, etapas `NOT_STARTED`, evidências nulas e gates `NOT_EVALUATED`/`BLOCKED_UNTIL_VERIFIED`.

Exemplo de verificação sem efeitos externos:

```bash
python3 -m hub.cli compose --goal "Auditar segurança" --project "PEOS Knowledge Hub"
python3 -m unittest tests.test_pmu_negative_gates -v
```

A suíte de testes negativa abrange objetivo vazio, falta de contexto, valor inválido, limites de tamanho e instruções hostis na solicitação para ignorar gates e conceder privilégios. A aprovação editorial da issue #17 e os direitos da issue #2 **permanecem pendentes**: uma verificação técnica não constitui aceite humano.

## Limitações e próximo aceite

O script não avalia se a redação é suficientemente original, completa ou adequada a um caso real; não detecta todo risco de instruções contraditórias e não prova direitos autorais. Não altera o estado editorial dos PMUs.

Para concluir a [issue #17](https://github.com/alexoaraujo/peos-knowledge-hub/issues/17), o mantenedor deverá registrar uma **decisão editorial individual** fundamentada para cada PMU (objetivo, qualidade, riscos, testes de aplicação e abrangência), com SHA e UTC. Pode decidir explicitamente **manter PROPOSED** para um release limitado, ou excluir PMUs do artefato; não transformá-los automaticamente em `ACTIVE`.

Em qualquer cenário o gate de redistribuição segue **BLOCKED** pela [issue #2](https://github.com/alexoaraujo/peos-knowledge-hub/issues/2), e a auditoria manual do portal segue pendente na [issue #8](https://github.com/alexoaraujo/peos-knowledge-hub/issues/8). Um relatório técnico PASS nunca constitui homologação editorial ou autorização de release.
