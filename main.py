import repositorios.cliente_repositorio as cliente_repositorio, entidades.cliente as cliente
from entidades import produto
from repositorios import pedido_repositorio, produto_repositorio
import fabricas.fabrica_conexao as fb_conexao

loop = True
while loop:
    print(30 * "-", "MENU", 30 * "-")
    print("1. Cliente")
    print("2. Produtos")
    print("3. Pedidos")
    print("0. Sair")
    print(67 * "-")

    menu_principal = int(input("Digite a opção desejada: "))

    if menu_principal == 1:
        print(30 * "-", "MENU", 30 * "-")
        print("1. Inserir cliente")
        print("2. Editar cliente")
        print("3. Remover cliente")
        print("4. Listar clientes")
        print("5. Listar cliente pelo ID")
        print("6. Listar clientes pelo nome")
        print("0. Sair")
        print(67 * "-")

        menu_cliente = int(input("Digite a opção desejada: "))

        if menu_cliente == 1:
            fabrica = fb_conexao.FabricaConexao()
            sessao = fabrica.criar_sessao()
            try:
                nome_cliente = input("Digite o nome: ")
                idade_cliente = int(input("Digite a idade: "))

                novo_cliente = cliente.Cliente(nome_cliente, idade_cliente)
                repositorio = cliente_repositorio.ClienteRepositorio()
                repositorio.inserir_cliente(novo_cliente, sessao)

                sessao.commit()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif menu_cliente == 2:
            fabrica = fb_conexao.FabricaConexao()
            sessao = fabrica.criar_sessao()
            try:
                id_cliente = int(input("Digite o ID do cliente a ser atualizado: "))
                nome_cliente = input("Digite o nome: ")
                idade_cliente = int(input("Digite a idade: "))

                novo_cliente = cliente.Cliente(nome_cliente, idade_cliente)
                repositorio = cliente_repositorio.ClienteRepositorio()
                repositorio.editar_cliente(id_cliente, novo_cliente, sessao)

                sessao.commit()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()
        elif menu_cliente == 3:
            fabrica = fb_conexao.FabricaConexao()
            sessao = fabrica.criar_sessao()

            try:
                id_cliente = int(input("Digite o ID do cliente que deseja remover: "))

                repositorio = cliente_repositorio.ClienteRepositorio()
                repositorio.remover_cliente(id_cliente, sessao)
                sessao.commit()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif menu_cliente == 4:
            fabrica = fb_conexao.FabricaConexao()
            sessao = fabrica.criar_sessao()
            try:
                repositorio = cliente_repositorio.ClienteRepositorio()
                clientes = repositorio.listar_cliente(sessao)

                for cliente in clientes:
                    print(cliente)
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif menu_cliente == 5:
            fabrica = fb_conexao.FabricaConexao()
            sessao = fabrica.criar_sessao()
            try:
                id_cliente = int(input("Digite o ID do cliente: "))
                repositorio = cliente_repositorio.ClienteRepositorio()
                cliente = repositorio.listar_cliente_id(id_cliente, sessao)
                print(cliente)
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()
        elif menu_cliente == 6:
            fabrica = fb_conexao.FabricaConexao()
            sessao = fabrica.criar_sessao()
            try:
                nome_cliente = input("Digite o nome que deseja buscar: ")
                repositorio = cliente_repositorio.ClienteRepositorio()
                clientes = repositorio.listar_cliente_nome(nome_cliente, sessao)
                for cliente in clientes:
                    print(cliente)
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()
        else:
            continue

    elif menu_principal == 2:
        print(30 * "-", "MENU", 30 * "-")
        print("1. Inserir produto")
        print("2. Buscar produto ID")
        print("0. Sair")
        print(67 * "-")

        menu_produto = int(input("Digite a opção desejada: "))

        if menu_produto == 1:
            fabrica = fb_conexao.FabricaConexao()
            sessao = fabrica.criar_sessao()
            try:
                descricao_produto = input("Informe a descricao do produto: ")
                valor_produto = float(input("Informe o valor do produto: "))
                novo_produto = produto.Produto(descricao_produto, valor_produto)
                repositorio_produto = produto_repositorio.ProdutoRepositorio()
                repositorio_produto.inserir_produto(novo_produto, sessao)
                sessao.commit()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif menu_produto == 2:
            fabrica = fb_conexao.FabricaConexao()
            sessao = fabrica.criar_sessao()

            try:
                id_produto = int(input("Digite o ID do produto a ser pesquisado: "))
                repositorio = produto_repositorio.ProdutoRepositorio()
                produto = repositorio.listar_produto_id(id_produto, sessao)
                print(produto)
                sessao.commit()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif menu_produto == 0:
            continue
        else:
            print("Opção inválida!")

    elif menu_principal == 3:
        print(30 * "-", "MENU", 30 * "-")
        print("1. Inserir pedido")
        print("0. Sair")
        print(67 * "-")

        menu_pedido = int(input("Digite a opção desejada: "))
        if menu_pedido == 1:
            fabrica = fb_conexao.FabricaConexao()
            sessao = fabrica.criar_sessao()
            try:
                loop_pedido = True
                lista_produto = []
                while loop_pedido:
                    print("1. Inserir produto")
                    print("0. Voltar")
                    menu_pedido_produto = int(input("Digite a opção desejada: "))
                    if menu_pedido_produto == 1:
                        id_produto_pedido = int(input("Digite o ID do produto deste pedido: "))
                        lista_produto.append(id_produto_pedido)
                    elif menu_pedido_produto == 0:
                        break
                id_cliente_pedido = int(input("Informe o ID do cliente relacionado com o pedido: "))
                repositorio_pedido = pedido_repositorio.PedidoRepositorio()
                repositorio_pedido.inserir_pedido(id_cliente_pedido, sessao, lista_produto)
                sessao.commit()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()
        elif menu_pedido == 0:
            continue
        else:
            print("Opção inválida!")

    elif menu_principal == 0:
        print("Até mais!")
        break
    else:
        print("Opção inválida!")
