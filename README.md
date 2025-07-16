# Introdução à Documentação do Projeto DevOps-EML1-EX2

## Versão
`version = "0.1.0"`

## 🔹 Sobre o Projeto
⚙️ **DevOps-EML1-EX2** é um projeto de **Engenharia de Machine Learning (MLOps)** voltado à **inferência de potabilidade da água**. Ele integra pré-processamento de dados, carregamento e persistência via **Google Firestore** e automação com Docker e Makefile.

- **Nome do Projeto**: `devops-eml1-ex2`
- **Autor**: `tralencar`
- **Versão**: `0.1.0`
- **Licença**: `MIT`
- **Palavras-chave**: `MLOps`, `Firestore`, `qualidade da água`, `automação`, `predição`
- **Fonte dos Dados**: [Dataset (Qualidade da Água)](https://www.kaggle.com/datasets/adityakadiwal/water-potability/data) do Kaggle.

---

## 🔹 Visão geral do Projeto

> O projeto **DevOps-EML1-EX2** combina práticas modernas de DevOps e MLOps para garantir a **execução automatizada, segura e rastreável de pipelines de inferência** em Machine Learning, com foco em **infraestrutura leve**, **portabilidade com Docker** e **integração com serviços de nuvem como o Firestore**.
> A proposta enfatiza **eficiência operacional, reprodutibilidade e confiabilidade em modelos de IA aplicados a dados ambientais críticos**.

Neste projeto de classificação da potabilidade da água, foi adotada a metodologia CRISP-DM (Cross Industry Standard Process for Data Mining) devido à sua estrutura bem definida, iterativa e amplamente reconhecida na indústria de ciência de dados.

O CRISP-DM orientou todas as etapas do projeto conforme as seguintes informações:

1. Entendimento do Negócio: Definiu-se o objetivo de prever a potabilidade da água com base em parâmetros físico-químicos.
2. Entendimento dos Dados: Realizou-se uma análise exploratória para compreender a estrutura, qualidade e desbalanceamento dos dados.
3. Preparação dos Dados: Incluiu tratamento de valores ausentes, aplicação de SMOTE e divisão em treino e teste.
4. Modelagem: Modelos como Random Forest e XGBoost foram otimizados com Optuna.
5. Avaliação: O desempenho dos modelos foi comparado com base em métricas como accuracy, recall e f1-score.
6. Implantação: A pipeline de inferência foi implementada com o modelo Random Forest (melhor modelo encontrado no treinamento) otimizado, executado dentro de um contêiner Docker. Os dados de entrada foram obtidos do Firestore, o modelo carregado via arquivo .pkl, e os resultados das predições foram gravados de volta no Firestore com o mesmo identificador de origem.

A escolha pelo CRISP-DM garantiu organização, reprodutibilidade e alinhamento entre objetivos técnicos e de negócio, tornando-o ideal para projetos de ciência de dados estruturados como este.

## Estrutura do Projeto

<pre>📂 DEVOPS-EML1-EX2                                   ✅ (Diretório raiz do projeto)</pre>
<pre>├── 📂 .env                                          ✅ (Credenciais de serviço) - Deve ser configurado</pre>
<pre>│    └── serviceAccountKey.json                      📌 (Chave de autenticação do Firebase/Firestore) - Deve ser configurado</pre>
<pre>├── 📂 data                                          ✅ (Conjuntos de dados de entrada e processados)</pre>
<pre>│    ├── 📂 cloud_input                              📌 (Dados para inferência sem a coluna alvo)</pre>
<pre>│    │    └── water_potability_without_target.csv</pre>
<pre>│    ├── 📂 original_data                            📌 (Dados brutos com a coluna alvo)</pre>
<pre>│         └── water_potability.csv</pre>
<pre>├── 📂 notebooks                                     ✅ (Notebooks exploratórios e do CRISP-DM)</pre>
<pre>│    ├── best_rf_full.pkl                            📌 (Modelo treinado de Random Forest)</pre>
<pre>│    ├── best_xgb_full.pkl                           📌 (Modelo treinado de XGBoost)</pre>
<pre>│    ├── crisp_dm_stages.ipynb                       📌 (Notebook com etapas do CRISP-DM)</pre>
<pre>│    └── database_init.ipynb                         📌 (Notebook para carregamento dos dados inicias no Firebase/Firestore)</pre>
<pre>├── 📂 src                                           ✅ (Scripts principais da aplicação)</pre>
<pre>│    ├── best_rf_full.pkl                            📌 (Modelo Random Forest pronto para produção)</pre>
<pre>│    ├── firestore_init.py                           📌 (Script para carregamento dos dados inicias no Firebase/Firestore)</pre>
<pre>│    └── water_scan_main.py                          📌 (Script principal de predição: carrega modelo e grava resultados no Firestore)</pre>
<pre>├── 📄 .dockerignore                                 ✅ (Arquivos ignorados ao construir imagens Docker)</pre>
<pre>├── 📄 .gitignore                                    ✅ (Arquivos ignorados pelo Git)</pre>
<pre>├── 📄 .python-version                               ✅ (Define a versão do Python para ambientes virtuais)</pre>
<pre>├── 📄 Dockerfile                                    ✅ (Especificação da imagem Docker do projeto)</pre>
<pre>├── 📄 Makefile                                      ✅ (Comandos de automação do projeto)</pre>
<pre>├── 📄 pyproject.toml                                ✅ (Configuração de dependências e ferramentas com o Poetry)</pre>
<pre>├── 📄 README.md                                     ✅ (Documentação principal com instruções de uso)</pre>
<pre>└── 📄 requirements-min-docker.txt                   ✅ (Conjunto mínimo de dependências para execução via Docker)</pre>

---

## 🔹 Funcionalidades

✅ Linguagem: `Python`  
✅ Arquitetura leve para inferência de ML  
✅ Conexão com Firestore via `firebase-admin`  
✅ Carregamento e pré-processamento automático de dados  
✅ Predição com `scikit-learn` (Random Forest e XGBoost compatíveis)  
✅ Registro de resultados diretamente no Firestore  
✅ Dockerfile otimizado para produção  
✅ Automação com `Makefile`  
✅ Gerenciamento de dependências com `Poetry`  

---

## 🧪 Ferramentas de Desenvolvimento

- `Poetry`, `Docker`, `Make`, `Firebase Admin SDK`, `pandas`, `scikit-learn`, `imbalanced-learn`, `optuna`

---

## 🔹 Pré-requisitos

- Python >=3.11,<3.12
- Git
- Poetry
- Docker
- Make

---

## 🔹 Instalação das Dependências

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/tralencar/devops-eml1-ex2.git
```

```bash
cd devops-eml1-ex2
```

### 2️⃣ Instale o Poetry (se necessário)

```bash
pip install poetry
```

### 3️⃣ Configure o ambiente virtual local

```bash
poetry config virtualenvs.in-project true
```

```bash
poetry shell
```

### 4️⃣ Instale as dependências

```bash
poetry install
```

---

## 🔹 Configuração Inicial do Google Cloud Firestore

Para que o pipeline possa **carregar e salvar predições no Firestore**, é necessário realizar uma configuração inicial no **Firebase** do Google. Siga os passos a seguir:

### 1️⃣ Crie um Projeto no Google Cloud

Siga os passos no seguinte vídeo ["Criando um banco de dados do Cloud Firestore"](https://www.youtube.com/watch?v=aYyDjtacyO4)

1. Faça login na sua conta do gmail.
2. Acesse o site: [https://firebase.google.com](https://firebase.google.com)
3. Clique em **Go to console** na parte superior direita.
4. Crie um novo projeto com o nome (devops-eml1-ex2).
5. Anote o `ID do Projeto (devops-eml1-ex2)` para uso posterior.

### 2️⃣ Ative o Firestore

1. No menu lateral, acesse **Firestore Database**.
2. Clique em **Criar banco de dados**.
3. Escolha o **modo de teste** e a localização desejada. Clique em **avançar**.
4. Crie a **coleção `devops-eml1-ex2`**. Clique em **ativar**.

### 3️⃣ Gere a Chave de Serviço

1. Acesse **Botão de engrenagem ao lado do texto (Visão geral do projeto)** na parte superior esquerda da tela.
2. Clique em **Configuração do projeto**.
3. Clique na aba **Contas de serviço**.
4. Clique na opção **Python**.
5. Clique no botão **Gerar nova chave privada**.
6. Renomei o arquivo `.json` com o nome `serviceAccountKey.json`.
7. Baixe o arquivo `.json` e salve em `.env/serviceAccountKey.json` no seu projeto local.

### 4️⃣ Estrutura Esperada

Seu projeto deverá conter:
```
devops-eml1-ex2/
├── .env/
│   └── serviceAccountKey.json  ← 🔐 Chave do Firebase
```

---

## 🔹 Executar Pipeline de Predição

### 1️⃣ Subir Dados iniciais de teste para Firestore

> Depois da configuração inicial do Google Cloud Firestore é necessário adicionar os primeiros dados no banco de dados Firestore. Para isso, execute o seguinte comando no terminal de comando:

```bash
make project-init
```

> Os dados iniciais foram adicionados no Firebase com a coluna (Potability) sem informações ainda, pois esta coluna será completada com base na predição do modelo de Machine Learning nas etapas seguintes.

---

### 2️⃣ Com Docker:

> Abra o docker desktop e em seguida execute os seguintes comandos no terminal de comando no diretório do projeto:

```bash
make build
```

```bash
make docker-run
```

> Os dados foram atualizados no Firebase para a coluna (Potability) com base nas predições do modelo de Machine Learning.

---

### 🔹 Verificar Instalação

```bash
poetry run python -c "import pandas; print('Instalação bem-sucedida!')"
```

---

## 🔹 Tarefas Automatizadas com Makefile

O projeto oferece uma série de comandos via `make` para facilitar a automação de tarefas:

### 🔧 Instalação e Lockfile

```bash
make lock         # Gera o poetry.lock com a versão 1.8.3 do Poetry
```

```bash
make project-init # Instala dependências e inicializa o Firestore com os dados CSV
```

### 🚀 Execução da Inferência

```bash
make run         # Executa o pipeline principal de predição com poetry
```

### 📦 Docker

```bash
make build       # Cria a imagem Docker
```

```bash
make docker-run  # Executa a imagem Docker
```

```bash
make clean       # Remove a imagem Docker
```

---