# Python-API
Uma API desenvolvida em Pyhton/flask
![image](https://user-images.githubusercontent.com/75399046/174487036-0ae56c80-20c8-47e4-9463-4e592b1a220b.png)

#### **Rotas**

---

|Endpoint|Nome|Função| 
|---|---|---|
|/users|Usuarios|Lista todos os usuarios disponiveis na API, metodo GET
|/users/id|Usuario|Lista o usuario correspondente ao id informado na URL, metodo GET
|/add_user|Adicionar|Adiciona o usuario escrito no corpo da requisição via Json, metodo POST
|/edit_user/id|Editar|Edita o usuario correspondente ao id informado na URL, metodo PUT, informar o json no corpo da requisição com os dados ja alterados
|/delete_user/id|Deletar|Deleta o usuario correspondente ao id informado na URL, metodo DELETE

---
#### **Tecnicas e tecnologias usadas**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
- ``SqlAlchemist``
- ``CRUD``
- ``API Rest``

---

#### **Acesso ao projeto**
- Baixe o reposiotorio do projeto usando o comando ``git clone https://github.com/Gclayton0207/crud-completo-Python.git``
- Insira seu usuario e senha do MySQL no arquivo ``prepara_banco.py`` e execute para inciar o banco de dados
![mysql](https://user-images.githubusercontent.com/75399046/174485241-a3d9fb2b-2c3f-4180-a3ab-e1ae5f593451.png)

- Utilize o comando ``pip install -r requirements.txt`` no terminal para instalar os requerimentos do projeto
- Utilize o comando ``python  .\app.py`` no terminal para executar a api de forma local, geralmente inicia no caminho http://127.0.0.1:5000
- Para vizualizar a api recomendo os programas ``Insomnia`` ou ``Postman`` sao 2 testadores de api conforme imagem abaixo

![insomnia](https://user-images.githubusercontent.com/75399046/174488017-266f54a2-1cfd-4771-be52-ab6bec6840aa.png)



---
