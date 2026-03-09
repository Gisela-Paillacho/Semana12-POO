from servicios.biblioteca_servicio import BibliotecaServicio

biblioteca = BibliotecaServicio()

# Libro inicial
biblioteca.agregar_libro(
    "Introduccion a Python",
    "Gisela Paillacho",
    "Programacion",
    "ISBN001"
)

# Usuario inicial
biblioteca.registrar_usuario(
    "Juan Carlos Tapia",
    "U001"
)

while True:

    print("\n===== BIBLIOTECA DIGITAL =====")
    print("1. Agregar libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Eliminar usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro por titulo")
    print("8. Buscar libro por autor")
    print("9. Buscar libro por categoria")
    print("10. Listar libros de usuario")
    print("0. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":

        titulo = input("Titulo: ")
        autor = input("Autor: ")
        categoria = input("Categoria: ")
        isbn = input("ISBN: ")

        biblioteca.agregar_libro(titulo, autor, categoria, isbn)

    elif opcion == "2":

        isbn = input("ISBN del libro: ")
        biblioteca.quitar_libro(isbn)

    elif opcion == "3":

        nombre = input("Nombre: ")
        id_usuario = input("ID usuario: ")

        biblioteca.registrar_usuario(nombre, id_usuario)

    elif opcion == "4":

        id_usuario = input("ID usuario: ")
        biblioteca.eliminar_usuario(id_usuario)

    elif opcion == "5":

        id_usuario = input("ID usuario: ")
        isbn = input("ISBN libro: ")

        biblioteca.prestar_libro(id_usuario, isbn)

    elif opcion == "6":

        id_usuario = input("ID usuario: ")
        isbn = input("ISBN libro: ")

        biblioteca.devolver_libro(id_usuario, isbn)

    elif opcion == "7":

        titulo = input("Titulo: ")
        biblioteca.buscar_por_titulo(titulo)

    elif opcion == "8":

        autor = input("Autor: ")
        biblioteca.buscar_por_autor(autor)

    elif opcion == "9":

        categoria = input("Categoria: ")
        biblioteca.buscar_por_categoria(categoria)

    elif opcion == "10":

        id_usuario = input("ID usuario: ")
        biblioteca.libros_usuario(id_usuario)

    elif opcion == "0":
        print("Saliendo del sistema")
        break

    else:
        print("Opcion invalida")