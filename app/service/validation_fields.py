import logging


class ValidationFields:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def validar_dados(self, event: dict):
        self.logger.info("validando dados")
        try:
            "escreva seu codigo aqui"
        except Exception as error:
            raise error
