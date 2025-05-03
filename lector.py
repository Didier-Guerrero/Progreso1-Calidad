import pandas as pd
from cliente import Cliente

class LectorCSV:
    def __init__(self, archivo):
        self.archivo = archivo

    def cargar_clientes(self):
        clientes = []
        registros_invalidos = 0
        try:
            datos = pd.read_csv(self.archivo, dtype=str, on_bad_lines='skip', encoding='utf-8')
            if not {'id', 'nombre', 'email', 'ciudad', 'edad'}.issubset(datos.columns):
                print("Columnas inválidas en el archivo.")
                return clientes, registros_invalidos

            datos = datos.dropna(subset=['id', 'nombre', 'email', 'ciudad', 'edad'])
            datos = datos[datos['id'].str.isdigit() & datos['edad'].str.isdigit()]
            registros_invalidos = len(pd.read_csv(self.archivo, encoding='utf-8')) - len(datos)

            for _, fila in datos.iterrows():
                cliente = Cliente(
                    int(fila['id']),
                    fila['nombre'],
                    fila['email'],
                    fila['ciudad'],
                    int(fila['edad'])
                )
                clientes.append(cliente)

            return clientes, registros_invalidos

        except FileNotFoundError:
            print(" Archivo no encontrado.")
            return clientes, registros_invalidos
        except Exception as e:
            print(f" Error al cargar el archivo: {e}")
            return clientes, registros_invalidos
