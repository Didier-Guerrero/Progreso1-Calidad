from lector import LectorCSV
from gestor import GestorClientes

class Main:
    def __init__(self):
        self.gestor = None

    def ejecutar(self):
        while True:
            print("\n--- Sistema de Gestión de Clientes ---")
            print("1. Cargar archivo CSV")
            print("2. Buscar cliente por ID")
            print("3. Listar clientes por ciudad")
            print("4. Listar clientes ordenados por edad")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                archivo = input("Ingrese el nombre del archivo CSV: ")
                lector = LectorCSV(archivo)
                clientes, invalidos = lector.cargar_clientes()
                self.gestor = GestorClientes(clientes)
                print(f"Clientes cargados: {len(clientes)}")
                print(f" Registros inválidos ignorados: {invalidos}")

            elif opcion == '2':
                if self.gestor:
                    try:
                        cliente_id = int(input("Ingrese el ID del cliente: "))
                        cliente = self.gestor.buscar_por_id(cliente_id)
                        print(cliente if cliente else "Cliente no encontrado.")
                    except ValueError:
                        print("ID inválido. Debe ser un número.")
                else:
                    print(" Primero debe cargar un archivo CSV:")

            elif opcion == '3':
                if self.gestor:
                    ciudad = input("Ingrese la ciudad: ")
                    resultado = self.gestor.listar_por_ciudad(ciudad)
                    if resultado:
                        for cliente in resultado:
                            print(cliente)
                        print(f"Total encontrados: {len(resultado)}")
                    else:
                        print("No se encontraron clientes en esa ciudad.")
                else:
                    print(" Primero debe cargar un archivo CSV:")

            elif opcion == '4':
                if self.gestor:
                    ordenados = self.gestor.listar_ordenado_por_edad()
                    for cliente in ordenados:
                        print(cliente)
                else:
                    print(" Primero debe cargar un archivo CSV:")

            elif opcion == '5':
                print(" Programa finalizado.")
                break
            else:
                print(" Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    app = Main()
    app.ejecutar()
