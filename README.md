# libpythonpro_2020
Modulo para exemplificar construçao de projetos Python no curso PyTools

Link do curso [Python Pro](https://www.python.pro.br/)

[![Build Status](https://travis-ci.org/gelhen/libpythonpro_2020.svg?branch=master)](https://travis-ci.org/gelhen/libpythonpro_2020)
    
Suportada versão 3 de Python

Para instalar:

```console
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements-dev.txt
```

Para conferir a qualidade do código:
```console 
flake8
```

configurar o Travis

Link do [Travis](https://travis-ci.org/)
Criar um arquivo .travis.yml na raiz do projeto

````.yaml
language: python
python:
 - 3.6
 - 2.7
install:
 - pip install -r requirements-dev.txt
script:
 - flake8

````