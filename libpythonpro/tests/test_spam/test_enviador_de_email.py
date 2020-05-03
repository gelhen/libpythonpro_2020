import pytest
from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['ti@tozzoalimentos.com.br', 'gelhen@gmail.com']
)
def test_destinatario(destinatario):
    enviador = Enviador()
    remetente = 'gelhen@gmail.com'
    resultado = enviador.enviar(
        remetente,
        destinatario,
        'Cursos Python Pro',
        'Primeira turma Guido Von Rosson Aberta'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['', 'gelhen']
)
def test_destinatario_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        remetente = 'gelhen@gmail.com'
        enviador.enviar(
            remetente,
            destinatario,
            'Cursos Python Pro',
            'Primeira turma Guido Von Rosson Aberta'
        )
