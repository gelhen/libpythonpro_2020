"""
O nome deste arquivo foi definido por conveção, então todas as fixture aqui definidas dentro
ficaram disponiveis para todos os módulos definidos dentro do test_spam
"""
import pytest

from libpythonpro.spam.db import Conexao


@pytest.fixture(scope='session')
def conexao():
    # setup
    conexao_obj = Conexao()
    yield conexao_obj
    # tear down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_pbj = conexao.gerar_sessao()
    yield sessao_pbj
    sessao_pbj.roll_back()
    sessao_pbj.fechar()