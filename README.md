# 📄 Projeto - Processador de Currículos com OCR + LLM (Flask + Docker)

Este projeto é uma aplicação Flask que permite:

- 🧾 Receber múltiplos currículos em PDF ou imagem (PNG/JPEG)
- 🔍 Realizar OCR com Tesseract para extrair o texto
- 📃 Gerar sumários automáticos usando LLMs da Hugging Face
- ❓ Responder perguntas como “Qual currículo é mais adequado para a vaga de Engenheiro de Software?”
- 💾 Registrar logs no MongoDB (sem armazenar os arquivos)

---

## ⚠️ Aviso importante

> 💻 Este projeto foi desenvolvido em uma máquina **sem GPU** e com **recursos limitados (pouca RAM e CPU fraca)**.  
> Por isso:
> - Os modelos utilizados são leves (`facebook/bart-large-cnn` e `google/flan-t5-base`)
> - O número de tokens foi reduzido para evitar estouros de memória ou travamentos
> - O desempenho pode ser baixo, mas funcional para testes e desenvolvimento local

---

## ✅ Pré-requisitos

- Docker instalado
- Docker Compose instalado

---

## 🚀 Como rodar o projeto com Docker

### 1. Clone ou copie o projeto em seu computador

Coloque os arquivos do projeto (código Python, Dockerfile, docker-compose.yml, etc.) em uma pasta local.

### 2. Construa a imagem do backend

No terminal, dentro da pasta do projeto:

```bash
docker-compose up --build
acesse http://localhost:5000/apidocs
