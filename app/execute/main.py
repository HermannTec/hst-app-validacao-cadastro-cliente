from app.service.validation_fields import ValidationFields
import logging
from app.service.consulta_cnpj.consulta_cnpj import ConsultaCnpj


class Main:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.validation = ValidationFields()
        self.consulta_cnpj = ConsultaCnpj()

    def execucao(self, event: dict) -> bool:

        self.logger.info("iniciando execução de validação de dados")
        try:

            """Exemplo"""
            resultado_consulta_cnpj = self.consulta_cnpj.consultar_dados_cliente(event.get("cnpj", None))
            """Exemplo"""

            "escreva seu codigo aqui que recebe a resposta do service validar dados se deu tudo certo ou não"
            "o lambda_handler aguarda a resposta dessa função para saber se os dados foram validados com sucesso ou se ococrreu algum erro por falta de dados por exemplo"
            "ou falha na consulta de algum dado"

        except Exception as error:
            raise error
