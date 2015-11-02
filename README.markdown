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


## Usando a API

A criação e extração de dados de voluntários, inscrições e treinamentos é feita
através da API fornecida pelo django-restframework. Os endpoints configurados são

* "voluntários": "http://localhost:8000/apiv1/volunteers/"
* "inscrições": "http://localhost:8000/apiv1/subscriptions/",
* "treinamentos": "http://localhost:8000/apiv1/trainings/",

### Gerando um token de acesso

O Token de acesso permite acessar dados dos voluntário e de inscrições.
Contudo, ainda sem o tokem é possível se inscrever.

Comando
```
$ curl --data "username=admin&password=admin" http://localhost:8000/apiv1/token-auth/
```

Retorno
```
{"token":"b4f9759156ab9e512e7d3d078cbea43ac7b81ebb"}
```


### Listando voluntários

Comando
```
$ curl http://localhost:8000/apiv1/volunteers/ -H 'Authorization: Token b4f9759156ab9e512e7d3d078cbea43ac7b81ebb'
```


### Listando treinamentos

Não é preciso token para listar treinamentos

```
$ curl http://localhost:8000/apiv1/trainings/
```

Retorno
```
[{"id":1,"local":{"id":1,"name":"Sede do Sonhar Acordado","cep":"05609-060","address":"Rua Maestro João Nunes, 30","complement":"","state":"SP","city":"São Paulo","lat":0.0,"lon":0.0},"date":"2015-10-23T09:32:54.633151-02:00"},{"id":2,"local":{"id":1,"name":"Sede do Sonhar Acordado","cep":"05609-060","address":"Rua Maestro João Nunes, 30","complement":"","state":"SP","city":"São Paulo","lat":0.0,"lon":0.0},"date":"2015-10-30T09:32:54.634974-02:00"},{"id":3,"local":{"id":1,"name":"Sede do Sonhar Acordado","cep":"05609-060","address":"Rua Maestro João Nunes, 30","complement":"","state":"SP","city":"São Paulo","lat":0.0,"lon":0.0},"date":"2015-11-06T09:32:54.636145-02:00"}]
```


### Criando um voluntário

Comando
```
$ curl http://localhost:8000/apiv1/volunteers/ -H "Content-Type: application/json" --data '@-' << EOF
{
    "email": "pedro@brasil.com",
    "name": "Pedro Alvares Cabral",
    "rg": "xxxxxxxxx",
    "birthdate": "1468-10-22",
    "phone": "(11) 99999-9999",
    "occupation": "Comandante",
    "organization": "Reino de Portugal",
    "cep": "88888-888",
    "address": "Rua Porto Seguro, 1500",
    "complement": "",
    "state": "BA",
    "city": "Porto Seguro"
}
EOF
```

Retorno
```
{"id":1,"email":"pedro@brasil.com","name":"Pedro Alvares Cabral","rg":"xxxxxxxxx","birthdate":"1468-10-22","phone":"(11) 99999-9999","occupation":"Comandante","organization":"Reino de Portugal","cep":"88888-888","address":"Rua Porto Seguro, 1500","complement":"","state":"BA","city":"Porto Seguro"}
```

### Criando uma inscrição

Nessa parte é preciso ter o id de um voluntário e de um treinamento

Comando
```
curl http://localhost:8000/apiv1/subscriptions/ -H "Content-Type: application/json" --data '{"volunteer": 1, "training": 1}
```

Retorno
```
{"id":1,"volunteer":1,"training":1,"present":false,"paid":0.0,"payment":"","extra":0,"valid":false}
```


### Atualizando só um campo da inscrição

É preciso usar o método PATCH com o id da inscrição.

Comando
```
$ curl http://localhost:8000/apiv1/subscriptions/1/ -X PATCH -H "Content-Type: application/json" --data '{"present": true}'
```

Algumas bibliotecas não implementam o PATCH. Neste caso, pode-se adicionar um o HEADER
`X-HTTP-Method-Override: PATCH` para instuir o restframwork a atualizar só um campo.

Comando alternativo
```
$ curl http://localhost:8000/apiv1/subscriptions/1/ -H "Content-Type: application/json" -H "X-HTTP-Method-Override: PATCH" --data '{"present": true}'
```

Retorno
```
{"id":1,"volunteer":1,"training":1,"present":true,"paid":0.0,"payment":"","extra":0,"valid":false}
```


### Dados de pagamento

Para pagar pelo Paypal foi criado um endpoint para obter os dados de geração
do formulário. Neste endpoint de pagamento deve ser fornecido um número de inscrição
no fim da url.

Comando
```
$ curl http://localhost:8000/apiv1/paymentform/1/
```

Retorno
```
{"custom":"Festa de Natal 2015","cmd":"_xclick","lc":"BR","image_button":"https://www.sandbox.paypal.com/en_US/i/btn/btn_buynowCC_LG.gif","notify_url":"http://localhost:8000/payment/paypal/","charset":"utf-8","business":"receiver@paypaltest.com","currency_code":"BRL","invoice":"Subscription(id=1)","item_name":"Inscrição de Pedro Alvares Cabral","amount":40.0,"endpoint":"https://www.sandbox.paypal.com/cgi-bin/webscr","cancel_return":"/pagamento-cancelado","return":"/obrigado","no_shipping":"1"}
```
