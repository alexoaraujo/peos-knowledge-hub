# Análise técnica e incorporação — Programação e Design

## Escopo e fontes

- **Acervo mestre (v1.1.0):** 647 prompts canônicos, comparados historicamente com 273 da v1.0.
- **Fonte adicional:** `Biblioteca-de-Prompts-para-Programação-e-Design.txt`, 128 entradas numeradas de 1 a 128.
- **Setores adicionais e workflow:** 30 seções originais, preservadas na íntegra.
- **Conteúdo consolidado:** 775 entradas navegáveis; não há afirmação de 775 finalidades semanticamente diferentes.
- **Coleção local:** `BPD-001` a `BPD-128`, nomes e texto preservados; nenhuma colisão com IDs mestres.
- **Revisão editorial pendente:** 11 hipóteses de finalidades específicas de Design/UX (não promovidas).

## 1. Seções originais e quantidade de itens

| Seção | Subcategoria original | Entradas |
|---:|---|---:|
| 01 | Ideação do projeto | 5 |
| 02 | Levantamento de requisitos | 5 |
| 03 | Planejamento técnico | 5 |
| 04 | Arquitetura de software | 5 |
| 05 | Escolha de tecnologias | 5 |
| 06 | Estrutura de projeto | 5 |
| 07 | Banco de dados | 5 |
| 08 | APIs | 5 |
| 09 | Backend | 5 |
| 10 | Frontend | 5 |
| 11 | UX/UI Design | 5 |
| 12 | Design System | 5 |
| 13 | Responsividade | 4 |
| 14 | Acessibilidade | 3 |
| 15 | Autenticação e autorização | 3 |
| 16 | Segurança | 4 |
| 17 | Code Review | 4 |
| 18 | Debug e correção | 5 |
| 19 | Refatoração | 4 |
| 20 | Testes | 5 |
| 21 | Performance | 4 |
| 22 | DevOps e infraestrutura | 4 |
| 23 | Observabilidade | 4 |
| 24 | Documentação | 4 |
| 25 | Auditoria completa de projeto | 5 |
| 26 | Prompts de execução autônoma | 5 |
| 27 | Prompts para IA agir como equipe técnica | 7 |
| 28 | Prompt Mestre — Programação + Design | 1 |
| 29 | Prompt para continuar automaticamente um projeto | 1 |
| 30 | Prompt para transformar uma ideia em aplicação pronta | 1 |

## 2. Critérios de curadoria

| Classe | Regra | Consequência |
|---|---|---|
| Correspondência temática | Prompt local aponta para um ou mais IDs canônicos que tratam tópico próximo | Manter texto local e linkar ao canônico; não renumerar |
| Complemento operacional | O texto local traz instrução mais curta, diferente recorte ou procedimento complementar | Indexar por fase e seção, preservando a origem |
| Possível lacuna de UX/UI | Artefato de Design não explicitado como finalidade própria no catálogo | Criar item de revisão, **sem alocar ID canônico** |
| Colisão ou substituição | Um número 1..128 local aparenta coincidir com 0001..0128 canônico | Usar prefixo local `BPD`, nunca substituir registros existentes |
| Fusão editorial | Somente mediante demonstração de equivalência de objetivo, entradas, saída e validação | Novo release, PR revisada, evento de changelog e testes |

## 3. Candidatos a especialização UX/UI

| ID local | Tema | Observação |
|---|---|---|
| BPD-051 | UX completo | Relacionado a 0404, 0409; revisar equivalência antes de criar novo ID |
| BPD-052 | Wireframe | Relacionado a 0404, 2409; revisar equivalência antes de criar novo ID |
| BPD-053 | Layout profissional | Relacionado a 0404; revisar equivalência antes de criar novo ID |
| BPD-054 | Redesign | Relacionado a 0404, 2504; revisar equivalência antes de criar novo ID |
| BPD-055 | Hierarquia visual | Relacionado a 0404, 0422; revisar equivalência antes de criar novo ID |
| BPD-059 | Estados dos componentes | Relacionado a 0404, 0422; revisar equivalência antes de criar novo ID |
| BPD-060 | Consistência | Relacionado a 0404, 2504; revisar equivalência antes de criar novo ID |
| BPD-061 | Responsividade completa | Relacionado a 0405, 0406; revisar equivalência antes de criar novo ID |
| BPD-062 | Mobile-first | Relacionado a 0405, 0505; revisar equivalência antes de criar novo ID |
| BPD-063 | Tabelas responsivas | Relacionado a 0409, 0405; revisar equivalência antes de criar novo ID |
| BPD-064 | Menu responsivo | Relacionado a 0404, 0405; revisar equivalência antes de criar novo ID |

## 4. Setorização proposta

**Design de Produto e UX:** novo eixo editorial transversal relacionado a desenvolvimento frontend, qualidade e acessibilidade.
Não altera as 36 categorias originais. Após revisão, pode ser criada uma categoria de UX/UI com novos IDs na faixa livre `3600-3699`,
mantendo o histórico dos 647 IDs sem renumeração. Os subtemas candidatos incluem descoberta de UX, arquitetura da informação,
wireframes, hierarquia visual, redesenho, estados de componentes, consistência visual, mobile-first e padrões responsivos.

**Índices transversais sugeridos para o acervo completo:** profissão (Product Designer, UX Researcher, UI Designer, Frontend, QA, Accessibility),
fase (ideação, descoberta, arquitetura, construção, validação, produção), entregável (wireframe, fluxo, mapa de navegação,
componente, design token, auditoria), plataforma (web, mobile), risco e tecnologia.

## 5. Controle automático de integridade

```bash
python3 tools/library.py audit
python3 tools/collections_integration.py check
python3 tools/library.py validate
python3 -m unittest discover -s tests -v
```

Os testes verificam: (a) preservação 273 → 647; (b) duplicação e remoção de IDs mestres;
(c) integridade de cada um dos 128 excertos em relação à fonte integral; (d) hashes SHA-256 e snapshots;
(e) links canônicos existentes e (f) compilação de índices determinística.

## 6. Divergências e limites

- **Não houve promoção automática a prompt mestre**: nenhuma avaliação textual isolada prova identidade funcional entre bibliotecas.
- As associações de IDs são propostas editoriais de afinidade temática, ainda requerem revisão independente.
- Novos conteúdos não autorizam reescrever as fichas existentes da v1.1 ou alterar os snapshots de releases históricas.
- Os 11 candidatos a lacuna precisam de decisão editorial por finalidade e contrato de saída antes de criar IDs novos.
- As 30 seções BPD são subcategorias da coleção, e não uma nova contagem de categorias canônicas.

## 7. Resultado e próximos gates

**Gate estrutural:** aprovado pela validação automática local. **Gate editorial-semântico:** revisão pendente.
Próxima etapa recomendada: revisar as 11 finalidades UX/UI, criar fichas completas e testes de aceitação,
publicar release 1.2.0 (ou v2.0 para nova taxonomia) após revisão humana e checks verdes.
