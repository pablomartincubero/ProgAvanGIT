
class Book:
    def _init_(self, title, author, isbn, status=False):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._status = status  # False indica que el libro no está prestado

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def _str_(self):
        status_str = "Prestado" if self._status else "Disponible"
        return f"Título: {self._title}, Autor: {self._author}, ISBN: {self._isbn}, Estado: {status_str}"
    