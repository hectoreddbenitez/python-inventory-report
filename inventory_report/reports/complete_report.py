from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(list):
        report = SimpleReport.generate(list)
        companies = []
        for product in list:
            companies.append(product["nome_da_empresa"])
        # documentação:
        # https://www.guru99.com/python-counter-collections-example.html
        companies_counter = Counter(companies)
        products_per_companie = []
        for (company, qtd) in companies_counter.items():
            products_per_companie.append(f"- {company}: {qtd}\n")

        return (
            f"{report}\n"
            "Produtos estocados por empresa:\n"
            # documetação:
            # https://www.delftstack.com/pt/howto/python/python-print-lists/
            f"{''.join(map(str,products_per_companie))}"
        )
