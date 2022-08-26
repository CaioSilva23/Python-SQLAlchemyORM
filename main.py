import repositorios.cliente_repositorio as cliente_repositorio, entidades.cliente as cliente

    
cliente = cliente.Cliente("Neide",52)

repositorio_cliente = cliente_repositorio.ClienteRepositorio()

repositorio_cliente.listar_cliente()
# cliente_repositorio.ClienteRepositorio.inserir_cliente(cliente)
# cliente_repositorio.ClienteRepositorio.editar_cliente(1, cliente)
# cliente_repositorio.ClienteRepositorio.remover_cliente(8)






