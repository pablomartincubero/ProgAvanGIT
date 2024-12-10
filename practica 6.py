from datetime import time

# Clase Base: Ficha
class Ficha:
    def __init__(self, nombre="", edad=0, nacio=time(0, 0, 0)):
        self._nombre = nombre
        self._edad = edad
        self._nacio = nacio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        self._edad = value

    @property
    def nacio(self):
        return self._nacio

    @nacio.setter
    def nacio(self, value):
        self._nacio = value

    def visualizar(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Nacimiento: {self._nacio.strftime('%H:%M:%S')}"

# Clase Derivada: Empleado
class Empleado(Ficha):
    def __init__(self, nombre="", edad=0, nacio=time(0, 0, 0), categoria="", antiguedad=0):
        super().__init__(nombre, edad, nacio)
        self._categoria = categoria
        self._antiguedad = antiguedad

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, value):
        self._categoria = value

    @property
    def antiguedad(self):
        return self._antiguedad

    @antiguedad.setter
    def antiguedad(self, value):
        self._antiguedad = value

    def visualizar(self):
        return super().visualizar() + f", Categoría: {self._categoria}, Antigüedad: {self._antiguedad} años"

# Clase Derivada: Cliente
class Cliente(Ficha):
    def __init__(self, nombre="", edad=0, nacio=time(0, 0, 0), dni=""):
        super().__init__(nombre, edad, nacio)
        self._dni = dni

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, value):
        self._dni = value

    def visualizar(self):
        return super().visualizar() + f", DNI: {self._dni}"

    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.nombre == other.nombre and self.edad == other.edad
        return False

# Clase RegistroDiario
class RegistroDiario:
    def __init__(self):
        self._personas = []

    def agregar_persona(self, persona):
        if isinstance(persona, (Empleado, Cliente)):
            self._personas.append(persona)
        else:
            raise ValueError("Solo se pueden agregar objetos de tipo Empleado o Cliente.")

    def visualizar_registro(self):
        return "\n".join([persona.visualizar() for persona in self._personas])

    def visualizar_empleados(self):
        return "\n".join([persona.visualizar() for persona in self._personas if isinstance(persona, Empleado)])

    def es_empleado(self, persona):
        return isinstance(persona, Empleado)

    def __getitem__(self, index):
        if 0 <= index < len(self._personas):
            return self._personas[index]
        else:
            raise IndexError("Índice fuera de rango.")

    def __add__(self, otro_registro):
        if isinstance(otro_registro, RegistroDiario):
            nuevo_registro = RegistroDiario()
            nuevo_registro._personas = self._personas + otro_registro._personas
            return nuevo_registro
        raise ValueError("Solo se puede combinar con otro RegistroDiario.")

# Función para leer cadenas
def leer_cadena(mensaje):
    while True:
        cadena = input(mensaje).strip()
        if cadena:
            return cadena
        print("Por favor, introduzca una cadena no vacía.")

# Programa principal
if __name__ == "__main__":
    registro = RegistroDiario()

    while True:
        print("\nMenú:")
        print("1. Introducir empleado")
        print("2. Introducir cliente")
        print("3. Buscar por nombre (y edad)")
        print("4. Mostrar registro diario")
        print("5. Mostrar empleados")
        print("6. Visualizar persona por índice")
        print("7. Combinar registros diarios")
        print("8. Salir")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            nombre = leer_cadena("Nombre del empleado: ")
            edad = int(input("Edad del empleado: "))
            categoria = leer_cadena("Categoría del empleado: ")
            antiguedad = int(input("Antigüedad del empleado (en años): "))
            empleado = Empleado(nombre, edad, time(9, 0, 0), categoria, antiguedad)
            registro.agregar_persona(empleado)

        elif opcion == "2":
            nombre = leer_cadena("Nombre del cliente: ")
            edad = int(input("Edad del cliente: "))
            dni = leer_cadena("DNI del cliente: ")
            cliente = Cliente(nombre, edad, time(10, 0, 0), dni)
            registro.agregar_persona(cliente)

        elif opcion == "3":
            nombre = leer_cadena("Nombre: ")
            edad = int(input("Edad: "))
            encontrado = False
            for persona in registro._personas:
                if persona.nombre == nombre and persona.edad == edad:
                    print(persona.visualizar())
                    encontrado = True
                    break
            if not encontrado:
                print("Persona no encontrada.")

        elif opcion == "4":
            print("Registro diario:")
            print(registro.visualizar_registro())

        elif opcion == "5":
            print("Empleados registrados:")
            print(registro.visualizar_empleados())

        elif opcion == "6":
            indice = int(input("Índice de la persona: "))
            try:
                print(registro[indice].visualizar())
            except IndexError:
                print("Índice fuera de rango.")

        elif opcion == "7":
            otro_registro = RegistroDiario()
            print("Añadiendo empleados y clientes al segundo registro.")
            otro_registro.agregar_persona(Empleado("Juan", 30, time(8, 0, 0), "Técnico", 5))
            otro_registro.agregar_persona(Cliente("Ana", 25, time(10, 0, 0), "12345678A"))
            combinado = registro + otro_registro
            print("Registros combinados:")
            print(combinado.visualizar_registro())

        elif opcion == "8":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")
