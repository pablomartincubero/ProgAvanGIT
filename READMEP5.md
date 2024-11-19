
# PREGUNTAS HECHAS A LA IA PARA LA PRACTICA 5

1-	¿Qué hace el decorador operation_logger?
Es un decorador que registra el nombre de la operación, los argumentos de entrada y el resultado. Además, maneja el caso específico de división por cero con un mensaje de error.

2-	¿Qué sucede si intentas dividir un número entre 0?
El decorador operation_logger captura el error de división por cero (ZeroDivisionError) y muestra un mensaje indicando que la operación no es válida. La función devuelve None en este caso.

3-	¿Qué función lambda se utiliza para sumar varios números, y cómo funciona?
La función add = lambda *args: sum(args) se utiliza para sumar varios números. Recibe un número variable de argumentos (*args) y utiliza la función incorporada sum para calcular la suma total.

4-	¿Qué imprime el programa cuando se ejecuta math_operation(add, 1, 2, 3, 4, 5)?
Operación: <lambda>, Entradas: (1, 2, 3, 4, 5), Resultado: 15
Esto ocurre porque la función add suma todos los números proporcionados y devuelve 15.

5-	¿Cómo puedes modificar el código para que la función subtract acepte más de dos números y reste todos los valores?
Puedes cambiar la función lambda subtract para aceptar varios argumentos y restarlos secuencialmente. El código modificado sería:
subtract = lambda a, *args: a - sum(args)
Ahora, puedes ejecutar algo como math_operation(subtract, 10, 4, 2) para obtener 10 - 4 - 2 = 4.

6-	¿Por qué la lista borrowed_books se inicializa con None en lugar de usar directamente una lista vacía como valor predeterminado en el constructor?
En Python, usar una lista vacía directamente como valor predeterminado en un argumento puede ser problemático porque las listas son mutables. Esto significa que si varios objetos comparten esa lista, cualquier modificación afectará a todos. 
Al usar None y luego asignar una nueva lista dentro del constructor, se asegura que cada instancia de la clase User tenga su propia lista independiente.

7-	¿Qué hace el método lend_book y cómo garantiza que no se pueda prestar un libro que ya está en préstamo?
El método lend_book busca un libro en la lista _books por su ISBN. 
Si encuentra el libro y su atributo status es False (es decir, el libro no está en préstamo), cambia su estado a True para indicar que ahora está prestado y devuelve un mensaje confirmando el préstamo. 
Si el libro ya está en préstamo (status es True) o no existe, devuelve un mensaje indicando que no está disponible o no existe. Esto garantiza que un libro no pueda ser prestado si ya está en préstamo.
