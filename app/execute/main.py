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
            dados_validados = self.validation.validar_dados(event)

            resultado_consulta_cnpj = self.consulta_cnpj.consultar_dados_cliente(event.get("cnpj", None))
            dados_validados.update(resultado_consulta_cnpj)

            return dados_validados

        except Exception as error:
            raise error
