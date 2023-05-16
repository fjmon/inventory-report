import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(file_path: str) -> list:
        if not file_path.endswith('.csv'):
            raise ValueError('extensão inválida')

        with open(file_path, newline="") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
