import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def csv_load(file_path):
        with open(file_path, newline="") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    @staticmethod
    def json_load(file_path):
        with open(file_path) as file:
            return json.load(file)

    @staticmethod
    def xml_load(file_path):
        tree = ET.parse(file_path)
        roots = tree.getroot()
        stock = []
        item = {}
        for root in roots:
            for root in root:
                item[root.tag] = root.text
            stock.append(item)
            item = {}
        return stock

    @staticmethod
    def import_data(file_path: str, report_type: str) -> str:
        loaders = {
            "csv": Inventory.csv_load,
            "json": Inventory.json_load,
            "xml": Inventory.xml_load,
        }

        if report_type == "simples":
            report = SimpleReport.generate
        elif report_type == "completo":
            report = CompleteReport.generate
        else:
            raise ValueError("Relatório inválido")

        extension = file_path.split(".")[-1]
        if extension not in loaders:
            raise ValueError("Extensão inválida")

        stock = loaders[extension](file_path)
        final_report = report(stock)

        return final_report
