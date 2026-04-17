# 🏋️ API Academia Tracen

API RESTful desenvolvida em Flask para gerenciamento de alunos e controle de acesso (catraca) com autenticação JWT.

---

## 📌 Sobre o Projeto

A **API Academia Tracen** é uma solução completa para academias que desejam digitalizar e automatizar:

* 👨‍🎓 Cadastro e gerenciamento de alunos
* 🚪 Controle de acesso inteligente (catraca)
* 🔐 Autenticação segura com JWT
* ☁️ Armazenamento em nuvem com Firebase
* 📄 Documentação interativa com Swagger (OpenAPI)

Projetada para ser simples, eficiente e facilmente integrável com sistemas web ou mobile.

---

## 🚀 Tecnologias Utilizadas

![Image](https://images.openai.com/static-rsc-4/Y_i2gFr9dFhp_DA1b2-nQ1hIfacd4L7xfysWqSp5JwfK4EX_471aYNLONpyuB9c2WOEW-WEh7OmK-6R-eoWHKRaSAgYBhV02egOg22k0VGCQBJ42euebjYnOH0cUb9CCJfhzMqlOsxEZMl22M7aiGsBSTsmd5xQVJ0soYOEU-C5Aw9ZBnLs6wE5yqoplpFWt?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/KRMP65IxsAnTMNj9pB05C71RIHbLS4cyi-EJb84nyVK_ymFSjQ1pk1AP4CFceqQK1Is8-0lUEv33MjPn2VxmVcfKxoeLFSM2XY2xTfc9OhJOFN4oNzy37bTbUdqC4xE9luqYm-DzujW-JQtVh-CPz-N95KOeTQ2TYaUvfn6XlvUpgAAj0-ai3tnbbY4Tl-Kl?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/1sBDt-qRxOqKT0X6mxvCAxhHU31RP4-nhp0DC-dyJlEL1Q9m0WuI9gk_-02rNXs6cDjIazu2en7hNWKw8uMi9HkZaBHgUMF7d6Xn_8tGrCF_g4SrgTgkhVOZZCMdR7VZnmyMJ3B5MaB6T-Npyl3_lAXdrVrJOZOcQA3kg8DXfI1bYnsdROq7pjJfCjiboaK5?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/LEj1ZGdFD05-zks2kxt6p7s8B1biu5giG86Z-C9TeAnzf9Cj0bK2B3u7gibTsE-JMO0RD_XlI9Msn1tZQZyofx1pmt1lRVXlxjAq0fBpEJOb28E3wpQUCyZozripJRHrULewINGjcACa7Tmu9PNaywyJ3c84EDh6Gn5DWWkPSu7xsIX8BqdKHJQJhzssc4Fm?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/7ZSQcBP8MT5ZqYaZjzE9RwOWLV-ncal9P5-souLmc6N_cBPwh9lBM-ix4UnhDGd_jv-4Dr7szWDO8VbYhQwND8pxjXrCQui35jsHadFZ_006jj-tsYXjnKPH4IXYm0e62znnKLlkx1K5kZ4q84Zy1sMSHqcCanPZqiUo6Vouzw_rJEthWRZ02GjO0ZAgFjlT?purpose=fullsize)

* **Python** → Linguagem principal
* **Flask** → Framework web leve e poderoso
* **Firebase Firestore** → Banco de dados NoSQL em tempo real
* **JWT (JSON Web Token)** → Autenticação segura
* **Vercel** → Deploy e hospedagem
* **Swagger / OpenAPI (Flasgger)** → Documentação interativa da API
* **CORS & dotenv** → Configuração e segurança

---

## 🌐 API em Produção

Acesse a documentação interativa:

```
https://tracen-beta.vercel.app/apidocs/
```

---

## 🔐 Autenticação

A API utiliza autenticação baseada em **JWT (Bearer Token)**.

### 🔑 Login

```http
POST /login
```

#### Body:

```json
{
  "usuario": "admin",
  "senha": "123"
}
```

#### Resposta:

```json
{
  "token": "seu_token_jwt"
}
```

---

### 🔒 Rotas protegidas

Para acessar rotas protegidas, envie o token no header:

```
Authorization: Bearer SEU_TOKEN
```

---

## 🚪 Endpoints

### 🟢 Sistema

#### GET /

Retorna o status da API

```json
{
  "api": "Academia Tracen",
  "versao": "1.0"
}
```

---

### 🔐 Autenticação

#### POST /login

Realiza login e retorna token JWT

---

### 🔥 Catraca

#### POST /catraca

Valida o acesso do aluno na academia

#### Body:

```json
{
  "cpf": "12345678900"
}
```

#### Respostas:

✅ **Liberado**

```json
{
  "status": "liberado",
  "msg": "Acesso liberado"
}
```

❌ **Bloqueado**

```json
{
  "status": "bloqueado",
  "msg": "Procure a secretaria da academia"
}
```

---

### 👨‍🎓 Alunos

#### 📄 GET /alunos

Lista todos os alunos

#### 🔍 GET /alunos/{cpf}

Busca aluno por CPF

#### ➕ POST /alunos 🔒

Cria um novo aluno

```json
{
  "nome": "João da Silva",
  "cpf": "12345678900"
}
```

Campos opcionais:

* `status` (default: `"ativo"`)
* `bloqueado` (default: `false`)

---

#### 🔄 PUT /alunos/{cpf} 🔒

Atualiza completamente um aluno

```json
{
  "nome": "João",
  "status": "ativo",
  "bloqueado": false
}
```

---

#### ✏️ PATCH /alunos/{cpf} 🔒

Atualização parcial

```json
{
  "bloqueado": true
}
```

---

#### ❌ DELETE /alunos/{cpf} 🔒

Remove um aluno

---

## ⚠️ Tratamento de Erros

| Código | Descrição                       |
| ------ | ------------------------------- |
| 400    | Dados inválidos                 |
| 401    | Não autorizado / Token inválido |
| 403    | Acesso bloqueado                |
| 404    | Não encontrado                  |
| 500    | Erro interno                    |

---

## 🧠 Regras de Negócio

* 🚫 Aluno **bloqueado** ou com status diferente de `"ativo"` não passa na catraca
* ⏳ Token expira em **1 hora**
* 🆔 CPF é utilizado como identificador único

---

## 📁 Estrutura do Projeto

```
📦 tracen-api
 ┣ 📜 app.py
 ┣ 📜 auth.py
 ┣ 📜 openapi.yaml
 ┣ 📜 firebase.json
 ┣ 📜 vercel.json
 ┣ 📜 .env
 ┗ 📜 requirements.txt
```

---

## 👨‍💻 Autor

**Vini do Back**

---

## 📌 Observações

* 🔐 Proteja sua `SECRET_KEY`
* ☁️ Nunca exponha credenciais do Firebase
* 🔒 Utilize HTTPS em produção

---

## 🏁 Conclusão

A **API Academia Tracen** oferece uma base moderna e escalável para sistemas de academias, com foco em segurança, desempenho e simplicidade de integração.

---
