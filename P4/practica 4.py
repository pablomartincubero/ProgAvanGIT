import numpy as np

class CMatFloat:
    """
    Clase que representa una matriz dinámica 1D/2D.

    Atributos:
        _Matriz       # Almacena la matriz (utilice numpy)
        _m_nFilas     # Almacena el número de filas de la matriz
        _m_nColumnas  # Almacena el número de columnas de la matriz
    """

    def __init__(self):
        """Método para inicializar el atributo matriz con None y los atributos filas y columnas a 0."""
        self._Matriz = None
        self._m_nFilas = 0
        self._m_nColumnas = 0

    def CrearMatriz2D(self, nFilas, nColumnas):
        """Método para crear una matriz bidimensional de ceros."""
        self._Matriz = np.zeros((nFilas, nColumnas))
        self._m_nFilas = nFilas
        self._m_nColumnas = nColumnas

    def CrearMatriz1D(self, nElementos):
        """Método para crear una matriz unidimensional de ceros."""
        self.CrearMatriz2D(1, nElementos)

    def Introducir(self):
        """Método para introducir los elementos de la matriz."""
        if self.Existe():
            for i in range(self._m_nFilas):
                for j in range(self._m_nColumnas):
                    self._Matriz[i, j] = leer_float(f"Introduce el elemento ({i}, {j}): ")
        else:
            print("No se ha creado ninguna matriz.")

    def Mostrar(self):
        """Método para mostrar los elementos de la matriz."""
        if self.Existe():
            print("Matriz actual:")
            print(self._Matriz)
        else:
            print("No hay matriz para mostrar.")

    def Existe(self):
        """Método que verifica si la matriz está creada y no está vacía."""
        return self._Matriz is not None

    def SumarMatrices(self, otra_matriz):
        """Método que suma la matriz actual con otra matriz."""
        if self._Matriz.shape == otra_matriz._Matriz.shape:
            return self._Matriz + otra_matriz._Matriz
        else:
            print("Las dimensiones de las matrices no coinciden.")
            return None

    def RestarMatrices(self, otra_matriz):
        """Método que resta la matriz actual con otra matriz."""
        if self._Matriz.shape == otra_matriz._Matriz.shape:
            return self._Matriz - otra_matriz._Matriz
        else:
            print("Las dimensiones de las matrices no coinciden.")
            return None


def leer_int(mensaje="Introduce un número entero: "):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no válida. Inténtalo de nuevo.")

def leer_float(mensaje="Introduce un número decimal: "):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Inténtalo de nuevo.")

def crear_menu(opciones_menu):
    print("\n".join(f"{i + 1}. {opcion}" for i, opcion in enumerate(opciones_menu)))
    return leer_int("Selecciona una opción: ")


def main():
    matriz = CMatFloat()
    while True:
        opcion = crear_menu([
            "Construir matriz 1D",
            "Construir matriz 2D",
            "Introducir matriz",
            "Mostrar matriz",
            "Operaciones con matrices",
            "Terminar"
        ])
        
        if opcion == 1:
            nElementos = leer_int("Número de elementos: ")
            matriz.CrearMatriz1D(nElementos)
        elif opcion == 2:
            nFilas = leer_int("Número de filas: ")
            nColumnas = leer_int("Número de columnas: ")
            matriz.CrearMatriz2D(nFilas, nColumnas)
        elif opcion == 3:
            matriz.Introducir()
        elif opcion == 4:
            matriz.Mostrar()
        elif opcion == 5:
            while True:
                sub_opcion = crear_menu([
                    "Sumar matrices",
                    "Restar matrices",
                    "Volver al menú principal"
                ])
                
                if sub_opcion == 1:
                    otra_matriz = CMatFloat()
                    otra_matriz.CrearMatriz2D(matriz._m_nFilas, matriz._m_nColumnas)
                    otra_matriz.Introducir()
                    resultado = matriz.SumarMatrices(otra_matriz)
                    if resultado is not None:
                        print("Resultado de la suma:")
                        print(resultado)
                elif sub_opcion == 2:
                    otra_matriz = CMatFloat()
                    otra_matriz.CrearMatriz2D(matriz._m_nFilas, matriz._m_nColumnas)
                    otra_matriz.Introducir()
                    resultado = matriz.RestarMatrices(otra_matriz)
                    if resultado is not None:
                        print("Resultado de la resta:")
                        print(resultado)
                elif sub_opcion == 3:
                    break
        elif opcion == 6:
            print("Programa terminado.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
