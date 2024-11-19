from book import Book
from Library import Library
from user import User
from utils import generate_unique_id

def main():
    library = Library()
    while True:
        print("\nMenú de Biblioteca")
        print("1. Añadir libro")
        print("2. Eliminar libro")
        print("3. Registrar usuario")
        print("4. Realizar préstamo")
        print("5. Realizar devolución")
        print("6. Mostrar todos los libros")
        print("0. Salir")

        choice = input("Seleccione una opción: ")
        if choice == '1':
            title = input("Ingrese el título: ")
            author = input("Ingrese el autor: ")
            isbn = input("Ingrese el ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
            print("Libro añadido con éxito.")
        
        # Agregar más opciones para completar las funcionalidades...
        
        elif choice == '0':
            break

if __name__ == "_main_":
        main()