# CodeQL Lab — Pipeline CI/CD com GitHub Actions

Projeto desenvolvido para a disciplina de **Desenvolvimento de Sistemas**, com foco em **Segurança da Informação**, utilizando uma pipeline CI/CD no GitHub Actions com análise de segurança automatizada por CodeQL.

Este repositório tem como objetivo demonstrar o funcionamento de uma pipeline composta por três etapas principais:

1. Análise de segurança com CodeQL
2. Execução de testes automatizados
3. Simulação de deploy para ambiente de stage

---

## Objetivo do projeto

O objetivo principal deste projeto é criar uma pipeline CI/CD capaz de analisar automaticamente o código-fonte, executar testes e simular um deploy.

A proposta é garantir que alterações feitas no código passem por validações antes de serem consideradas prontas.

A pipeline é executada automaticamente quando ocorre:

- push na branch `main`;
- pull request para a branch `main`.

---

## Tecnologias utilizadas

- GitHub
- GitHub Actions
- CodeQL
- Python
- Flask
- Pytest
- Flake8

---

## Estrutura do repositório

```text
codeql-lab/
├── .github/
│   └── workflows/
│       └── codeql.yml
├── tests/
│   └── test_main.py
├── code.py
├── requirements.txt
└── README.md
