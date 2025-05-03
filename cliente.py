class Cliente:
    def __init__(self, id, nombre, email, ciudad, edad):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.ciudad = ciudad
        self.edad = edad

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Email: {self.email} | Ciudad: {self.ciudad} | Edad: {self.edad}"
