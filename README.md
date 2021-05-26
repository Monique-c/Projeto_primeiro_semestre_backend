# Backend

Neste guia iremos configurar o ambiente de desenvolvimento com a instalação e configuração de um ambiente isolado, instalação dos requisitos do projeto, instalação e utilização do MySQL e utilização do Flask.

---

### Requisitos mínimos

1. _Python_
2. _MySQL_

<br/>

| Setup               |                        |
| ------------------- | ---------------------- |
| Memória RAM         | 16GiB                  |
| Processador         | i5-8300H CPU @ 2.30GHz |
| Sistema Operacional | Ubuntu 21.04           |

<br/>
<br/>

---

## Instalação e configuração do ambiente virtual

**Verifique se o pip está instalado**

```bash
python -m pip --version
```

_Siga a documentação oficial do pip caso você não tenha instalado:_

[Installation - pip documentation v21.1](https://pip.pypa.io/en/stable/installing/)

<br/>

**Instalando o virtualenv**

_Ferramenta para criar ambientes Python isolados._

```bash
python -m pip install virtualenv
```

**Clone o repositório do backend**

```bash
git clone https://github.com/fa-API-Group-02/backend
```

**Abra o projeto no vsCode**

```bash
cd backend
code .
```

**Abra o terminal do VsCode e Configure o ambiente**

```bash
python -m venv venv
```

**Ative o ambiente**

No terminal Windows PowerShell

```powershell
venv\Scripts\activate
```

**OU**

Terminal Bash

```bash
. venv/Scripts/activate

# Linux: . venv/bin/activate
```

**Atualize a versão pip**

```bash
pip install -U pip
```

**Instalando as dependências do projeto**

```bash
pip install -r requirements.txt
```

**Setup Completo :)**

---

<br/>
<br/>

# Instalação e Configuração do MySQL 🐬

Baixe o installer de 435.4M

[MySQL :: Download MySQL Installer](https://dev.mysql.com/downloads/installer/)

### Antes de iniciar o download será solicitado que você entre ou crie uma conta na Oracle, isso é opcional.

<br/>

⬇️ _CLIQUE EM NO THANKS, JUST START MY DOWNLOAD_ ⬇️

**Assista o vídeo para mais orientações:**

[https://www.youtube.com/watch?v=KYaZVqHHXpM](https://youtu.be/KYaZVqHHXpM)

**Atenção** 💡

1. Defina a senha do root e anote em algum lugar (Não esqueça essa senha de forma alguma)
2. Em user Accounts, adicione um um novo usuário. Como no exemplo abaixo:

User Name: **admin**

Password: **admin**

<br/>

**Dica:** Caso você não tenha feito isso, crie um novo usuário posteriormente.

Com um usuário `root` em um Shell MySQL ou no Workbench:

    CREATE USER `'admin'`@`'localhost'` IDENTIFIED BY `'admin'`;
    GRANT ALL PRIVILEGES ON _._ TO `'admin'`@`'localhost'`;

Continue o processo de instalação.

<br/>

### Utilização do MySQL WORKBENCH 🐬

[Utilização do MySQL Workbench 🐬](https://youtu.be/k9x_4gwfgXI)

<br/>
<br/>

---

# Utilizando o FLASK 🌶️

[Com o ambiente ativado ...]()

```bash
python app.py
```

O servidor foi iniciado e pode ser acessado em [localhost](http://localhost:5000/).

A porta padrão do nosso projeto é 5000.

---
