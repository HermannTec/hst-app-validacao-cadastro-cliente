import json
import logging
from app.execute.main import Main

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("Application started successfully.")
    try:
        result = Main().execucao(event)
        if result is True:
            return {
                "statusCode": 200,
                "body": json.dumps(result)
            }
    except Exception as error:
        logger.error(f"Erro durante a execução: {error}", exc_info=True)
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(error)})
        }


event = """{
  "nome_fantasia_empresa": "Hermann Soluções Tecnológicas",
  "razao_social": ""
  "nome_responsavel": "Douglas Hermann de Araujo",
  "data_hora_cadastro": "2025-06-23 19:32:44.394798"
  "endereco": {
    "cep": "03422000",
    "rua": "Avenida Guilherme Giorgi",
    "numero": "928",
    "complemento": "Sala 12",
    "bairro": "Vila Carrão",
    "cidade": "São Paulo",
    "estado": "SP"
  },
  "cnpj": "44.822.964/0001-90",
  "telefones": {
    "fixo": "1134567890",
    "celular": "11966000804"
  },
  "email": "hermannsolucoestecnologicas@gmail.com"
}"""

lambda_handler(event, '')