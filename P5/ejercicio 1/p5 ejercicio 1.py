# Decorador para registrar la operación
def operation_logger(func):
    def wrapper(operation, *args, **kwargs):
        try:
            # Ejecuta la función decorada
            result = func(operation, *args, **kwargs)
            # Imprime el registro de la operación
            print(f"Operación: {operation.__name__}, Entradas: {args}, Resultado: {result}")
            return result
        except ZeroDivisionError:
            # Maneja el caso de división por cero
            print(f"Error: División por cero no es permitida. Entradas: {args}")
            return None
    return wrapper

# Función principal para realizar operaciones matemáticas
@operation_logger
def math_operation(operation, *args):
    return operation(*args)

# Funciones lambda para operaciones básicas
add = lambda *args: sum(args)  # Suma de todos los argumentos
subtract = lambda a, b: a - b  # Resta de dos números
multiply = lambda a, b: a * b  # Multiplicación de dos números
divide = lambda a, b: a / b    # División (la división por cero se maneja en el decorador)

# Probando el sistema
print("Resultados de las pruebas:")
math_operation(add, 5, 3)               # Suma: 5 + 3
math_operation(subtract, 10, 4)         # Resta: 10 - 4
math_operation(multiply, 2, 6)          # Multiplicación: 2 * 6
math_operation(divide, 15, 3)           # División válida: 15 / 3
math_operation(divide, 10, 0)           # División por cero
math_operation(add, 1, 2, 3, 4, 5)      # Suma con múltiples argumentos: 1 + 2 + 3 + 4 + 5
