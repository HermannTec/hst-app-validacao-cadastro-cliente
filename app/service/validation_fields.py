import logging
import re

class ValidationFields:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def validar_dados(self, event: dict):
        try:
            self.logger.info("Iniciando validação dos dados")


            campos_obrigatorios = ["nome_empresa", "nome_responsavel", "email", "cnpj", "endereco", "telefones"]
            for campo in campos_obrigatorios:
                if campo not in event or not event[campo]:
                    raise ValueError(f"Campo obrigatório ausente ou vazio: {campo}")



            cnpj = re.sub(r'\D', '', event["cnpj"])
            if not re.fullmatch(r'\d{14}', cnpj):
                raise ValueError("CNPJ inválido")
            event["cnpj"] = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"



            email = event["email"].strip()
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                raise ValueError("Email inválido")
            event["email"] = email

            for tipo, telefone in event["telefones"].items():
                telefone = re.sub(r'\D', '', telefone)
                if not re.fullmatch(r'\d{10,11}', telefone):
                    raise ValueError(f"Telefone inválido ({tipo})")
                event["telefones"][tipo] = telefone


            cep = re.sub(r'\D', '', event["endereco"]["cep"])
            if not re.fullmatch(r'\d{8}', cep):
                raise ValueError("CEP inválido")
            event["endereco"]["cep"] = cep

            self.logger.info("Validação dos dados concluída com sucesso")
            return event

        except Exception as error:
            self.logger.error(f"Erro na validação: {error}")
            raise error
