import requests
import time
import json
import os


class ConsultaCnpj:

    def __init__(self):
        self.url = f"https://receitaws.com.br/v1/cnpj/"
        self.header = {"User-Agent": "Mozilla/5.0"}

    def consultar_dados_cliente(self, cnpj: str) -> dict:

        """incluir get da razão social"""

        cnpj_limpo = cnpj.replace('.', '').replace('/', '').replace('-', '')
        url_consulta = self.url + cnpj_limpo

        try:
            response = requests.get(url_consulta, headers=self.header, timeout=30)
            if response.status_code == 200:
                data = response.json()
                return {
                    "CNPJ": cnpj,
                    "Telefone": data.get("telefone", ""),
                    "Email": data.get("email", "")
                }
            else:
                print(f"Erro {response.status_code} para CNPJ {cnpj}")
        except Exception as e:
            print(f"Erro ao consultar CNPJ {cnpj}: {e}")
        return {"CNPJ": cnpj, "Telefone": "", "Email": "", "Site": ""}

