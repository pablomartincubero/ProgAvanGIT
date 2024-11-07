# Práctica 4: Arrays

from numpy import zeros  # Importación para facilitar las acciones con matrices

class CMatFloat:  # Clase que representa una matriz dinámica 1D/2D
    
    def __init__(self):
        self._Matriz = None  # Almacena la matriz 
        self._m_nFilas = 0  # Almacena el número de filas de la matriz
        self._m_nColumnas = 0  # Almacena el número de columnas de la matriz

    def CrearMatriz(self, nFilas, nColumnas):  # Método para crear una matriz de máximo 2 dimensiones de ceros.
        self._Matriz = zeros((nFilas, nColumnas), dtype=float)
        self._m_nFilas = nFilas
        self._m_nColumnas = nColumnas

    def CrearMatriz1D(self, nElementos):  
        self.CrearMatriz(1, nElementos)

    def Introducir(self):  
        if not self.Existe():
            print("No hay una matriz creada.")
            return
        for i in range(self._m_nFilas):
            for j in range(self._m_nColumnas):
                self._Matriz[i][j] = leer_float(f"Introduzca valor de la posición ({i},{j}): ")

    def Mostrar(self):  
        if self.Existe():
            print("Matriz actual:")
            print(self._Matriz)
        else:
            print("No hay una matriz creada para mostrar.")

    def Existe(self):
        return self._Matriz is not None

    def SumarMatrices(self, otra_matriz):  
        if self.Existe() and otra_matriz.Existe() and self._Matriz.shape == otra_matriz._Matriz.shape:
            return self._Matriz + otra_matriz._Matriz
        else:
            print("Error: Dimensiones de la matriz no son iguales.")
            return None

    def RestarMatrices(self, otra_matriz):  # Método que resta la matriz actual con otra matriz.
        if self.Existe() and otra_matriz.Existe() and self._Matriz.shape == otra_matriz._Matriz.shape:
            return self._Matriz - otra_matriz._Matriz
        else:
            print("Error: Las dimensiones de las matrices no coinciden.")
            return None

def leer_int(mensaje="Introduce un número entero: "):  # Función auxiliar que lee un número entero del teclado.
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")

def leer_float(mensaje="Introduce un número decimal: "):  # Función auxiliar que solicita al usuario un número decimal.
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número decimal.")

def crear_menu(opciones_menu):  # Función que muestra un menú de opciones y solicita al usuario
    print()
    for i, opcion in enumerate(opciones_menu, 1):
        print(f"{i}. {opcion}")
    return leer_int("Seleccione una opción: ")


def main():
    matriz = CMatFloat()

    while True:
        opcion = crear_menu(["Construir matriz 1D", "Construir matriz 2D", "Introducir matriz", "Mostrar matriz", "Operaciones con matrices", "Terminar"])

        match opcion:
            case 1:
                nElementos = leer_int("Ingrese el número de elementos de la matriz 1D: ")
                matriz.CrearMatriz1D(nElementos)

            case 2:
                filas = leer_int("Ingrese el número de filas: ")
                columnas = leer_int("Ingrese el número de columnas: ")
                matriz.CrearMatriz(filas, columnas)

            case 3:
                matriz.Introducir()

            case 4:
                matriz.Mostrar()

            case 5:
                operaciones_con_matrices(matriz)

            case 6:
                print("Programa terminado.")
                break

            case _:
                print("Opción no válida.")

def operaciones_con_matrices(matriz):
    while True:
        sub_opcion = crear_menu(["Sumar matrices", "Restar matrices", "Volver al menú principal"])

        match sub_opcion:
            case 1:
                otra_matriz = CMatFloat()
                filas = matriz._m_nFilas
                columnas = matriz._m_nColumnas
                otra_matriz.CrearMatriz(filas, columnas)
                
                print("Introduce los valores para la segunda matriz:")
                otra_matriz.Introducir()
                
                resultado = matriz.SumarMatrices(otra_matriz)
                
                if resultado is not None:
                    print("Resultado de la suma de matrices:")
                    print(resultado)

            case 2:
                otra_matriz = CMatFloat()
                filas = matriz._m_nFilas
                columnas = matriz._m_nColumnas
                otra_matriz.CrearMatriz(filas, columnas)
                
                print("Introduce los valores para la segunda matriz:")
                otra_matriz.Introducir()
                
                resultado = matriz.RestarMatrices(otra_matriz)

                if resultado is not None:
                    print("Resultado de la resta de matrices:")
                    print(resultado)

            case 3:
                break

            case _:
                print("Opción no válida.")

if __name__ == "__main__":
    main()
