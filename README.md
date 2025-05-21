# 📄 Projeto - Processador de Currículos com OCR + LLM (Flask + Docker)

Este projeto é uma aplicação Flask que permite:

- 🧾 Receber múltiplos currículos em PDF ou imagem (PNG/JPEG)
- 🔍 Realizar OCR com Tesseract para extrair o texto
- 📃 Gerar sumários automáticos usando LLMs da Hugging Face
- ❓ Responder perguntas como “Qual currículo é mais adequado para a vaga de Engenheiro de Software?”
- 💾 Registrar logs no MongoDB (sem armazenar os arquivos)

---

## ⚠️ Aviso importante sobre limitações técnicas

- **Máquina com CPU limitada e sem GPU**
- Modelos utilizados são leves e simplificados (`facebook/bart-large-cnn` e `google/flan-t5-base`)
- O limite de tokens para geração é baixo para evitar travamentos e estouros de memória
- Por isso, **recomendamos testar no máximo 2 arquivos por vez**, apesar da API aceitar múltiplos arquivos

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
docker-compose build
```

```bash
docker-compose up
```
ou 

```bash
docker-compose up --build
```

### 3. Acesse a documentação interativa da API (Swagger UI)

Quando os dois containers estiverem iniciados acesse:

http://localhost:5000/apidocs/


### 3. Teste na interface Swagger

Teste a API enviando currículos
Na interface Swagger:

Use o campo files para selecionar arquivos (PDF ou imagens PNG/JPEG)

Informe um request_id válido (exemplo UUID: 123e4567-e89b-12d3-a456-426614174000)

Informe seu user_id (ex: fabio)

Opcionalmente, insira uma query para perguntar sobre os currículos (ex: "Qual currículo é melhor para Engenheiro de Software?")

Clique em "Try it out" para enviar e ver a resposta da API