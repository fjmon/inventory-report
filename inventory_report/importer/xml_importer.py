import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_path: str) -> list:
        if not file_path.endswith('.xml'):
            raise ValueError('Extensão inválida')

        tree = ET.parse(file_path)
        roots = tree.getroot()
        stock = []
        item = {}
        for root in roots:
            for subroot in root:
                item[subroot.tag] = subroot.text
            stock.append(item)
            item = {}
        return stock
