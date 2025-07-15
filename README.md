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

## 🔹 Identidade Visual do Projeto

> O projeto **DevOps-EML1-EX2** combina práticas modernas de DevOps e MLOps para garantir a **execução automatizada, segura e rastreável de pipelines de inferência** em Machine Learning, com foco em **infraestrutura leve**, **portabilidade com Docker** e **integração com serviços de nuvem como o Firestore**.
> A proposta enfatiza **eficiência operacional, reprodutibilidade e confiabilidade em modelos de IA aplicados a dados ambientais críticos**.

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
git clone https://github.com/tralencar/devops_eml1_ex2.git
cd devops_eml1_ex2
```

### 2️⃣ Instale o Poetry (se necessário)

```bash
pip install poetry
```

### 3️⃣ Configure o ambiente virtual local

```bash
poetry config virtualenvs.in-project true
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

```bash
make project-init
```

---

### 2️⃣ Com Docker:
```bash
make build
make run
```

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
make project-init # Instala dependências e inicializa o Firestore com os dados CSV
```

### 🚀 Execução da Inferência

```bash
make run         # Executa o pipeline principal de predição com poetry
```

### 📦 Docker

```bash
make build       # Cria a imagem Docker
make docker-run  # Executa a imagem Docker
make clean       # Remove a imagem Docker
make rebuild     # Limpa e reconstrói a imagem Docker
```

---