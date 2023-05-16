from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def type_report(report_type, stock):
        if report_type == "simples":
            report = SimpleReport.generate(stock)
        elif report_type == "completo":
            report = CompleteReport.generate(stock)
        else:
            raise ValueError("Relatório inválido")
        return report

    @staticmethod
    def import_data(file_path: str, report_type: str) -> str:
        extension = file_path.split(".")[-1]
        if extension == 'csv':
            importer = CsvImporter()
        elif extension == 'json':
            importer = JsonImporter()
        elif extension == 'xml':
            importer = XmlImporter()
        else:
            raise ValueError('Extensão inválida')

        stock = importer.import_data(file_path)

        return Inventory.type_report(report_type, stock)
