from datetime import date
import statistics


class SimpleReport:
    @classmethod
    def generate(self, list):

        oldest_manufact_date = min(
            [product["data_de_fabricacao"] for product in list]
        )

        next_expires_date = min(
            [
                product["data_de_validade"]
                for product in list
                if product["data_de_validade"] > str(date.today())
            ]
        )

        companies = []
        for product in list:
            companies.append(product["nome_da_empresa"])

        more_products_company = statistics.mode(companies)

        return (
            f"Data de fabricação mais antiga: {oldest_manufact_date}\n"
            f"Data de validade mais próxima: {next_expires_date}\n"
            f"Empresa com mais produtos: {more_products_company}"
        )
