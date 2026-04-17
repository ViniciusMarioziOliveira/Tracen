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

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge\&logo=flask\&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge\&logo=firebase\&logoColor=black)
![Firestore](https://img.shields.io/badge/Firestore-FF7139?style=for-the-badge\&logo=firebase\&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge\&logo=jsonwebtokens\&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge\&logo=vercel\&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge\&logo=swagger\&logoColor=black)

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
