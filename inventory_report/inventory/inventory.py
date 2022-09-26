from ast import parse
from csv import DictReader
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def file_reader(path):
        # product_list = []
        if ".csv" in path:
            with open(path, encoding="utf8") as file:
                return [lines for lines in DictReader(file)]
        if '.json' in path:
            with open(path, encoding="utf8") as file:
                return json.load(file)

    @classmethod
    def import_data(cls, path, relatory):
        products_list = Inventory.file_reader(path)
        if relatory == "simples":
            simples_report = SimpleReport.generate(products_list)
            return simples_report
        if relatory == "completo":
            complete_report = CompleteReport.generate(products_list)
            return complete_report
