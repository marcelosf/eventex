# Eventex

Sistema de Eventos

[![Build Status](https://travis-ci.org/marcelosf/eventex.svg?branch=master)](https://travis-ci.org/marcelosf/eventex)



## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env.
6. Execute os testes.

´´´console
git clone git@github.com:marcelosf/eventex.git wttd
cd wttd
python -m venv .wttd
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
´´´

## Como fazer p deploy?

1. Crie uma instância noheroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. COnfigure o serviço de e-mail
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py
heroku config:set DEBUG=False
#Configure o e-mail
git push heroku master --force
```
