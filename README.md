# 🏋️ API Academia Tracen

API RESTful desenvolvida em Flask para gerenciamento de alunos e controle de acesso (catraca) com autenticação JWT.

---

## 📌 Sobre o Projeto

A **API Academia Tracen** permite:

* Cadastro e gerenciamento de alunos
* Controle de acesso via catraca
* Autenticação segura com JWT
* Integração com Firebase Firestore
* Documentação automática com Swagger (OpenAPI)

---

## 🚀 Tecnologias Utilizadas

* Python + Flask
* Firebase Firestore
* JWT (JSON Web Token)
* Flasgger (Swagger)
* dotenv
* CORS

---

## ⚙️ Configuração do Ambiente

### 1. Clone o projeto

```bash
git clone https://github.com/seu-repositorio/tracen-api.git
cd tracen-api
```

### 2. Crie o arquivo `.env`

```env
SECRET_KEY=sua_chave_secreta
ADM_USUARIO=admin
ADM_SENHA=123

# Para ambiente Vercel (opcional)
FIREBASE_CREDENTIALS={...json...}
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o Firebase

* Local: coloque o arquivo `firebase.json` na raiz
* Produção (Vercel): use variável de ambiente `FIREBASE_CREDENTIALS`

### 5. Execute a aplicação

```bash
python app.py
```

A API estará disponível em:

```
http://localhost:5000
```

---

## 📖 Documentação Swagger

Acesse:

```
http://localhost:5000/apidocs
```

---

## 🔐 Autenticação

A API utiliza **JWT (Bearer Token)**.

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

Envie o token no header:

```
Authorization: Bearer SEU_TOKEN
```

---

## 🚪 Endpoints

### 🟢 Sistema

#### GET /

Retorna status da API

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

Valida acesso do aluno

#### Body:

```json
{
  "cpf": "12345678900"
}
```

#### Respostas possíveis:

✅ Liberado:

```json
{
  "status": "liberado",
  "msg": "Acesso liberado"
}
```

❌ Bloqueado:

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

---

#### 🔍 GET /alunos/{cpf}

Busca aluno por CPF

---

#### ➕ POST /alunos 🔒

Cria um novo aluno

```json
{
  "nome": "João da Silva",
  "cpf": "12345678900"
}
```

Campos opcionais:

* `status` (default: "ativo")
* `bloqueado` (default: false)

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

* Aluno **bloqueado** ou com status diferente de `"ativo"` não passa na catraca
* Token expira em **1 hora**
* CPF é usado como ID único no banco

---

## 📁 Estrutura do Projeto

```
📦 tracen-api
 ┣ 📜 app.py
 ┣ 📜 auth.py
 ┣ 📜 openapi.yaml
 ┣ 📜 firebase.json (ou env)
 ┣ 📜 .env
 ┗ 📜 requirements.txt
```

---

## 👨‍💻 Autor

**Vini do Back**

---

## 📌 Observações

* Certifique-se de proteger sua `SECRET_KEY`
* Nunca exponha suas credenciais do Firebase
* Utilize HTTPS em produção

---

## 🏁 Conclusão

A API fornece uma base sólida para sistemas de academia com controle de acesso, podendo ser facilmente integrada com frontends web ou mobile.

---
