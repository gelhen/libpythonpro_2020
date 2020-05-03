from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [Usuario(nome='Andre', email='gelhen@gmail.com'),
         Usuario(nome='Marcos', email='gelhen@gmail.com')
         ],
        [
            Usuario(nome='Andre', email='gelhen@gmail.com')
        ]
    ]
)
def test_qte_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_email(
        'gelhen@gmail.com',
        'Curso Python Pro',
        'Confira os Módulos Fantasticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Andre', email='gelhen@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_email(
        'gelhen@gmail.com',
        'Curso Python Pro',
        'Confira os Módulos Fantasticos'
    )
    enviador.enviar.assert_called_once_with(
        'gelhen@gmail.com',
        'gelhen@gmail.com',
        'Curso Python Pro',
        'Confira os Módulos Fantasticos'
    )


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_email(
        'gelhen@gmail.com',
        'Curso Python Pro',
        'Confira os Módulos Fantasticos'
    )
