from inventory_report.inventory.product import Product
from tests.factories.product_factory import ProductFactory


def test_cria_produto():

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

    assert product.id == mock.id
    assert product.nome_do_produto == mock.nome_do_produto
    assert product.nome_da_empresa == mock.nome_da_empresa
    assert product.data_de_fabricacao == mock.data_de_fabricacao
    assert product.data_de_validade == mock.data_de_validade
    assert product.numero_de_serie == mock.numero_de_serie
    assert (
        product.instrucoes_de_armazenamento == mock.instrucoes_de_armazenamento
    )
