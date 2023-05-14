import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(file_path: str, report_type: str) -> str:
        extension = file_path.split(".")[-1]
        if extension == "csv":
            with open(file_path, newline='') as arquivo:
                reader = csv.DictReader(arquivo)
                stock = [row for row in reader]
        elif extension == "json":
            with open(file_path) as file:
                stock = json.load(file)
        else:
            raise ValueError("Extensão inválida")

        if report_type == "simples":
            report = SimpleReport.generate(stock)
        elif report_type == "completo":
            report = CompleteReport.generate(stock)
        else:
            raise ValueError("Relatório inválido")

        return report
