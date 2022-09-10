from dominios.db import Produto


class ProdutoQuery:
    def inserir_produto(self, produto, sessao):
        sessao.add(produto)

    def listar_produto_id(self, id_produto, sessao):
        produto = sessao.query(Produto).filter(Produto.id == id_produto).first()
        return produto