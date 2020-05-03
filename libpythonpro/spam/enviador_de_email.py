class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in destinatario:
            raise EmailInvalido(f'E-mail de remetente inválido: {remetente}')
        return destinatario


class EmailInvalido(Exception):
    pass
