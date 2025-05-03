class GestorClientes:
    def __init__(self, lista_clientes):
        self.clientes = lista_clientes

    def buscar_por_id(self, cliente_id):
        for cliente in self.clientes:
            if cliente.id == cliente_id:
                return cliente
        return None

    def listar_por_ciudad(self, ciudad):
      return [cliente for cliente in self.clientes if cliente.ciudad == ciudad]


    def listar_ordenado_por_edad(self):
        return sorted(self.clientes, key=lambda cliente: cliente.edad)
