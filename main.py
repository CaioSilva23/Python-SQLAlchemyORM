import repositorios.cliente_repositorio as cliente_repositorio, entidades.cliente as cliente
import fabricas.fabrica_conexao as fb_conexao


fabrica = fb_conexao.FabricaConexao()
sessao = fabrica.criar_sessao()


nome_cliente = input("Digite o nome: ")
idade_cliente = int(input("Digite a idade: "))
novo_cliente = cliente.Cliente(nome_cliente, idade_cliente)
repositorio = cliente_repositorio.ClienteRepositorio()
repositorio.inserir_cliente(novo_cliente, sessao)

sessao.commit()