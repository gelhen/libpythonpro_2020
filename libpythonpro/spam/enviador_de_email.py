class Enviador:
    qtd_email_enviados = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in destinatario:
            raise EmailInvalido(f'E-mail de remetente inválido: {remetente}')
        self.qtd_email_enviados += 1
        return destinatario


class EmailInvalido(Exception):
    pass
