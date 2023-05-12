from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(products):
        fabrication = [item["data_de_fabricacao"]
                       for item in products]

        validate = [item["data_de_validade"]
                    for item in products
                    if item["data_de_validade"] >= datetime
                    .now().strftime("%Y-%m-%d")]

        company = Counter([item["nome_da_empresa"]
                           for item in products]).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {min(fabrication)}\n"
            f"Data de validade mais próxima: {min(validate)}\n"
            f"Empresa com mais produtos: {company}"
        )
