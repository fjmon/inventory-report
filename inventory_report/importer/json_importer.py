import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(file_path: str) -> list:
        if not file_path.endswith('.json'):
            raise ValueError('Extensão inválida')

        with open(file_path) as file:
            return json.load(file)
