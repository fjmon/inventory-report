from .simple_report import SimpleReport
from collections import Counter


class CompleteReport:
    @staticmethod
    def generate(product):
        list = ""
        simple_report = f"{SimpleReport.generate(product)}\n"
        companies = Counter([item["nome_da_empresa"] for item in product])
        for item in companies.items():
            list += f"- {item[0]}: {item[1]}\n"
        return f"{simple_report}Produtos estocados por empresa:\n{list}"
