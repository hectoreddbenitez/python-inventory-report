class SimpleReport:
    @classmethod
    def generate(self, list_):

        oldest_manufact_date = ...

        next_expires_date = ...

        more_products_company = ...

        return (
          f"Data de fabricação mais antiga: {oldest_manufact_date}"
          f"Data de validade mais próxima: {next_expires_date}"
          f"Empresa com mais produtos: {more_products_company}"
        )
