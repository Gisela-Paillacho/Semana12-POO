# Clase que representa un libro dentro de la biblioteca

class Libro:

    def __init__(self, titulo, autor, categoria, isbn):
        # Se usa una tupla para almacenar titulo y autor (inmutable)
        self.titulo_autor = (titulo, autor)

        self.categoria = categoria
        self.isbn = isbn

    def obtener_titulo(self):
        return self.titulo_autor[0]

    def obtener_autor(self):
        return self.titulo_autor[1]

    def __str__(self):
        return f"Título: {self.obtener_titulo()} | Autor: {self.obtener_autor()} | Categoría: {self.categoria} | ISBN: {self.isbn}"