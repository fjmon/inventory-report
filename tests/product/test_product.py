from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        id=1,
        nome_do_produto="Produto",
        nome_da_empresa="Empresa",
        data_de_fabricacao="Fabricacao",
        data_de_validade="Validade",
        numero_de_serie="Serie",
        instrucoes_de_armazenamento="Instrucoes",
    )

    assert product.id == 1
    assert product.nome_do_produto == "Produto"
    assert product.nome_da_empresa == "Empresa"
    assert product.data_de_fabricacao == "Fabricacao"
    assert product.data_de_validade == "Validade"
    assert product.numero_de_serie == "Serie"
    assert product.instrucoes_de_armazenamento == "Instrucoes"
