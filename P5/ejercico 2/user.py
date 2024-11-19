class User:
    def _init_(self, name, user_id, borrowed_books=None):
        if borrowed_books is None:
            borrowed_books = []
        self._name = name
        self._user_id = user_id
        self._borrowed_books = borrowed_books

    @property
    def name(self):
        return self._name

    @property
    def user_id(self):
        return self._user_id

    @property
    def borrowed_books(self):
        return self._borrowed_books

    def _str_(self):
        return f"Usuario: {self._name}, ID: {self._user_id}, Libros prestados: {', '.join(self._borrowed_books) if self._borrowed_books else 'Ninguno'}"