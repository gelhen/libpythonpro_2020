import pytest
from libpythonpro.spam.db import Conexao
from libpythonpro.spam.modelos import Usuario


@pytest.fixture
def conexao():
    #setup
    conexao_obj = Conexao()
    yield conexao_obj
    #tear down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_pbj = conexao.gerar_sessao()
    yield sessao_pbj
    sessao_pbj.roll_back()
    sessao_pbj.fechar()


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Andre')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Andre'), Usuario(nome='Marcos')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
