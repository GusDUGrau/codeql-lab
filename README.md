# CodeQL Lab — Pipeline CI/CD com GitHub Actions

Projeto desenvolvido para estudo de **Pipeline CI/CD** com foco em **Segurança da Informação**, utilizando **GitHub Actions** e **CodeQL** para análise automatizada de segurança.

Este repositório demonstra uma pipeline com três etapas principais:

1. Análise de segurança com CodeQL
2. Execução de testes automatizados
3. Simulação de deploy para ambiente de stage

---

## Objetivo

O objetivo deste projeto é criar uma pipeline CI/CD capaz de validar automaticamente o código enviado ao repositório.

A pipeline foi criada para:

- verificar vulnerabilidades no código com CodeQL;
- executar testes automatizados;
- validar o funcionamento básico do projeto;
- simular uma etapa de deploy;
- demonstrar boas práticas de integração contínua e segurança.

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
```

---

## Arquivo principal

O arquivo principal do projeto é:

```text
code.py
```

Ele contém uma aplicação simples em Python com Flask.

O projeto também possui um exemplo de código utilizado para demonstrar a análise de segurança feita pelo CodeQL.

---

## Pipeline CI/CD

A pipeline está configurada no arquivo:

```text
.github/workflows/codeql.yml
```

Ela é executada automaticamente quando ocorre alteração no repositório, como um `push` para a branch principal.

A pipeline é composta por três Jobs:

```text
Job 1 → Análise CodeQL
Job 2 → Testes Automatizados
Job 3 → Deploy para Stage
```

---

## Job 1 — Análise CodeQL

O primeiro Job executa a análise de segurança do código usando o CodeQL.

Essa etapa tem como objetivo identificar possíveis vulnerabilidades no projeto antes que o código avance para as próximas etapas.

Exemplos de vulnerabilidades que podem ser identificadas:

- SQL Injection
- Command Injection
- uso inseguro de dados de entrada
- falhas de segurança em código Python
- más práticas de desenvolvimento seguro

---

## Job 2 — Testes Automatizados

O segundo Job executa os testes automatizados do projeto.

Os testes ficam na pasta:

```text
tests/
```

O comando utilizado para rodar os testes é:

```bash
pytest tests/ -v
```

Essa etapa garante que o código continue funcionando corretamente após alterações.

---

## Job 3 — Deploy para Stage

O terceiro Job simula um deploy para o ambiente de stage.

Essa etapa representa o envio da aplicação para um ambiente de testes ou homologação.

O deploy só deve acontecer se as etapas anteriores forem concluídas com sucesso.

---

## Fluxo da pipeline

O funcionamento esperado da pipeline é:

```text
Código enviado para o GitHub
        ↓
Análise de segurança com CodeQL
        ↓
Execução dos testes automatizados
        ↓
Deploy simulado para stage
```

Se alguma etapa falhar, as próximas etapas não devem ser executadas.

---

## Dependências do projeto

As dependências estão no arquivo:

```text
requirements.txt
```

Para instalar as dependências localmente, utilize:

```bash
pip install -r requirements.txt
```

---

## Como executar localmente

Clone o repositório:

```bash
git clone https://github.com/GusDUGrau/codeql-lab.git
```

Entre na pasta do projeto:

```bash
cd codeql-lab
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute os testes:

```bash
pytest tests/ -v
```

---

## Como verificar a pipeline

Para verificar a execução da pipeline no GitHub:

1. Acesse o repositório
2. Clique na aba **Actions**
3. Selecione a execução mais recente
4. Verifique o status de cada Job

Legenda:

```text
Verde    → execução concluída com sucesso
Vermelho → ocorreu falha
Amarelo  → execução em andamento
```

---

## Como verificar alertas de segurança

Os alertas do CodeQL podem ser vistos na aba:



Nessa área, o GitHub mostra detalhes sobre possíveis vulnerabilidades encontradas no código.

<img width="1506" height="431" alt="Captura de tela 2026-05-29 195304" src="https://github.com/user-attachments/assets/6fc9408f-8f70-47bb-b752-dd3ecd63bb23" />
<img width="1446" height="347" alt="Captura de tela 2026-05-29 190349" src="https://github.com/user-attachments/assets/12590a86-75a7-442c-b259-e3a0b9b70207" />


---

# Evidências da Pipeline

Nesta seção estão as evidências do funcionamento da pipeline.  
Adicione abaixo os prints das execuções realizadas no GitHub Actions.
<img width="1877" height="891" alt="Captura de tela 2026-05-29 201330" src="https://github.com/user-attachments/assets/86c1a072-802b-413b-add0-17d085959e26" />


---

## 1. Pipeline executada com sucesso


<img width="1838" height="799" alt="Captura de tela 2026-05-29 201535" src="https://github.com/user-attachments/assets/65139bae-0e91-458b-b1e3-935d1e54d777" />

---

## 2. Job de Análise CodeQL

Adicione aqui o print do Job responsável pela análise de segurança com CodeQL.

<img width="1853" height="907" alt="Captura de tela 2026-05-29 200930" src="https://github.com/user-attachments/assets/a16d7aa0-5114-4afc-a7fa-81764a0e040d" />

---

## 3. Job de Testes Automatizados

Adicione aqui o print do Job responsável pela execução dos testes automatizados.

<img width="1523" height="797" alt="Captura de tela 2026-05-29 200845" src="https://github.com/user-attachments/assets/d2a6ac48-62a2-4ccd-ae7e-9114e8b7f1b6" />

---

## 4. Job de Deploy para Stage

Adicione aqui o print do Job responsável pela simulação de deploy para o ambiente stage.

<img width="1894" height="856" alt="Captura de tela 2026-05-29 200946" src="https://github.com/user-attachments/assets/83ea0d6d-c09e-45d5-8a0f-7ac2ac67644b" />


---

## 5. Alertas de segurança no CodeQL

Adicione aqui o print da aba **Security → Code scanning alerts**, caso existam alertas detectados pelo CodeQL.

<img width="1446" height="347" alt="Captura de tela 2026-05-29 190349" src="https://github.com/user-attachments/assets/f81175d9-cd59-4db7-8c68-b07cdb8357a8" />


---

## Comandos Git utilizados

Durante o desenvolvimento do projeto, foram utilizados comandos básicos do Git:

```bash
git status
git add .
git commit -m "ci: adiciona pipeline com CodeQL"
git push origin main
```

---

## Checklist do projeto

- [x] Repositório criado no GitHub
- [x] Repositório público
- [x] Workflow do GitHub Actions criado
- [x] CodeQL configurado
- [x] Pasta de testes criada
- [x] Arquivo de dependências criado
- [x] Pipeline com análise de segurança
- [x] Pipeline com testes automatizados
- [x] Pipeline com deploy simulado
- [ ] Prints da pipeline adicionados ao README
- [ ] Print do CodeQL adicionado ao README
- [ ] Print dos testes adicionado ao README
- [ ] Print do deploy adicionado ao README

---

## Autor
Nome: Gustavo Brito da Silva
SegInfo — FATEC
Disciplina: Desenvolvimento de Sistema seguro (SO)
Professor: Idirley Soares

Projeto acadêmico desenvolvido para estudo de **CI/CD**, **GitHub Actions** e **CodeQL** 
**Fatec Santana de Parnaiba**
---

## Conclusão

Este projeto demonstra a criação de uma pipeline CI/CD utilizando GitHub Actions e CodeQL.

A estrutura permite automatizar a análise de segurança, executar testes e simular um deploy, contribuindo para um processo de desenvolvimento mais seguro e organizado.
