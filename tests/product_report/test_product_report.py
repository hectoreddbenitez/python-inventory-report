from inventory_report.inventory.product import Product
from tests.factories.product_factory import ProductFactory


def test_relatorio_produto():
    mock = ProductFactory()

    product = Product(
        mock.id,
        mock.nome_do_produto,
        mock.nome_da_empresa,
        mock.data_de_fabricacao,
        mock.data_de_validade,
        mock.numero_de_serie,
        mock.instrucoes_de_armazenamento,
    )

    result = (
        f"O produto {mock.nome_do_produto}"
        f" fabricado em {mock.data_de_fabricacao}"
        f" por {mock.nome_da_empresa} com validade"
        f" até {mock.data_de_validade}"
        f" precisa ser armazenado {mock.instrucoes_de_armazenamento}."
    )

    assert product.__repr__() == result
