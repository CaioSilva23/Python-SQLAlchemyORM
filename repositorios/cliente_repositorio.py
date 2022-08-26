import fabricas.fabrica_conexao as fabrica_conexao

class ClienteRepositorio():
    

    def listar_cliente(self):
        fabrica = fabrica_conexao.FabricaConexao()
        conexao = fabrica.conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM cliente")
            print(cursor.fetchall())
        finally:
            conexao.close()
        


    def inserir_cliente(self, cliente):
        fabrica = fabrica_conexao.FabricaConexao()
        conexao = fabrica.conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO cliente (nome, idade) values (%s, %s)", (cliente.nome, cliente.idade))
        finally:
            conexao.close()
    

    def editar_cliente(self, id_cliente, cliente):
        fabrica = fabrica_conexao.FabricaConexao()
        conexao = fabrica.conectar()
        try:
            cursor = conexao.cursor()  
            cursor.execute("UPDATE cliente SET nome=%(nome)s, idade=%(idade)s WHERE idcliente=%(id_cliente)s",
                    ({'nome':cliente.nome,'idade': cliente.idade, 'id_cliente': id_cliente}))
        finally:
            conexao.close()
        

    def remover_cliente(self, id_cliente):
        fabrica = fabrica_conexao.FabricaConexao()
        conexao = fabrica.conectar()
        try:
            cursor = conexao.cursor()
            
            cursor.execute("DELETE FROM cliente WHERE idcliente=%s", (id_cliente, ))
        finally:
            conexao.close()