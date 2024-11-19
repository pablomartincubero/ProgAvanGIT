
class Library:
    def _init_(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def remove_book(self, isbn):
        self._books = [book for book in self._books if book.isbn != isbn]

    def lend_book(self, isbn):
        for book in self._books:
            if book.isbn == isbn and not book.status:
                book.status = True
                return f"El libro '{book.title}' ha sido prestado."
        return "El libro no está disponible o no existe."

    def return_book(self, isbn):
        for book in self._books:
            if book.isbn == isbn and book.status:
                book.status = False
                return f"El libro '{book.title}' ha sido devuelto."
        return "El libro no se encuentra en préstamo."

    def find_book_by_title(self, title):
        return [book for book in self._books if title.lower() in book.title.lower()]

    def _str_(self):
        return "\n".join(str(book) for book in self._books)