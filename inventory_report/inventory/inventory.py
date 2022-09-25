from csv import DictReader
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:

    @classmethod
    def importa_data(path):
        try:
            product_list = []
            with open(path, encoding="utf8") as file:
                read_file = DictReader(file, delimiter=",", quotechar='"')
                for row in read_file:
                    product_list.append(row)
            file.close()
            return product_list
        except FileNotFoundError:
            raise FileNotFoundError

    @classmethod
    def relatoy_generator():
        ...
