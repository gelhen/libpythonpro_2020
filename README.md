# libpythonpro_2020
Modulo para exemplificar construçao de projetos Python no curso PyTools

Link do curso [Python Pro](https://www.python.pro.br/)

[![Build Status](https://travis-ci.org/gelhen/libpythonpro_2020.svg?branch=master)](https://travis-ci.org/gelhen/libpythonpro_2020)
[![Updates](https://pyup.io/repos/github/gelhen/libpythonpro_2020/shield.svg)](https://pyup.io/repos/github/gelhen/libpythonpro_2020/)    
[![Python 3](https://pyup.io/repos/github/gelhen/libpythonpro_2020/python-3-shield.svg)](https://pyup.io/repos/github/gelhen/libpythonpro_2020/)

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
O parametro - q remove detalhes de dependencias durante o build
````.yaml
language: python
python:
 - 3.6
install:
 - pip install -q -r requirements-dev.txt
script:
 - flake8

````

Upgrade de dependencia e gerenciando dependencia com pyup

Link [Pyup](https://pyup.io/)

Criar Setup.py para preparar envio para o pypi

######Criação de Release
Para marcar o estado do projeto uma tag no github, com o nome 0.1(Versão do projeto)
```console
git tag 0.1
```
Enviar tag para o repositorio
```console
git push --tags
``` 

######Publicação no PyPi
Criar uma conta no pypi [PyPI](https://pypi.org)

Criar uma distribuição do projeto

```console
python setup.py sdist
```
Para fazer a puplicação 

```console
 pip install twine
 twine upload dist/*
 
 ```