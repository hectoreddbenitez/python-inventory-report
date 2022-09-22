from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(list):
        report = SimpleReport.generate(list)
        companies = []
        for product in list:
            companies.append(product["nome_da_empresa"])
        # o counter normal devolve a contagem em ordem descendente, não
        # respeita a ordem original de entrada
        companies_counter = dict(Counter(companies))
        products_per_companie = []
        for (company, qtd) in companies_counter.items():
            products_per_companie.append(f"- {company}: {qtd}\n")

        return (
            f"{report}\n"
            "Produtos estocados por empresa:\n"
            # referencia: https://www.delftstack.com/pt/howto/python/python-print-lists/
            f"{''.join(map(str,products_per_companie))}"
        )
