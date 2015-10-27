# Sistema de inscrição para a Festa de Natal


## Dependências de sistema

* python3
* virtualenv
* virtualenvwrapper (opcional)
* mysql
* npm


## Construindo ambiente de dev


### 1. Clonar ambiente

```
git clone git@github.com:sonhar-acordado-sp/festas-sonhar-acordado.git
cd festas-sonhar-acordado
```


### 2. Criar virtualenv

Se *não* estiver disponível o virtualenvwrapper, faça como abaixo.

```
virtualenv -p /usr/bin/python3 env
source env/bin/activate
```

Se estiver disponível o `virtualenvwrapper`, faça como abaixo.

```
mkvirtualenv -p /usr/bin/python3 festas-sonhar-acordado
workon festa-sonhar-acordado
```


### 3. Instalar dependências do projeto

```
pip install -r requirements.txt
```


### 4. Criar uma base de dados no MySQL

Assume-se que usuário corrente tem plenas permissões.

```
mysql -e 'CREATE SCHEMA grandesfestas';
python manage.py migrate
```


### 5. Cria um usuário e senha para o admin do Django

```
python manage.py createsuperuser --username admin --email a@b.cd
```


### 6. Baixar parafernalha do node

```
npm install
```


### 7. Rodando o Django

```
python manage.py runserver
```

Depois acesse no navegador http://localhost:8000.


## Desenvolvimento

O frontend e o backend estão separados e a comunicação entre eles é feita
através de uma API json. A descrição da API está http://localhost:8000/apiv1/.

O que for relacionado a parte de frontend está na pasta `festa-sonhar-acordado/webapp`
e o que for relacionado ao backend django está em `festa-sonhar-acordado/grandesfestas`.
