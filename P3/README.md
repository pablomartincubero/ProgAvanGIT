# PREGUNTAS A LA IA SOBRE LA PRACTICA 3

1-¿Qué son las clases en python?

Las **clases** en Python son una de las características fundamentales de la programación orientada a objetos (POO). Una clase es una plantilla para crear objetos (instancias) que encapsulan datos (atributos) y comportamientos (métodos) relacionados. 

2-¿Para que utilizo return true/false?

return true` se utiliza en programación para devolver el valor booleano `true` desde una función. Este es un patrón común en funciones que verifican condiciones o realiza comprobaciones. También podemos utilizar los return para devolver valores de operaciones o en nuestro caso en alguna de las funciones para devolver los valores de las horas que queremos mostrar en un futuro en mi programa.

3-¿Cuál es la razón para utilizar @classmethod y @staticmethod en la clase Time?

@classmethod: Utilizado para métodos que necesitan acceder a atributos de clase (cls). Por ejemplo, get_time_count utiliza cls.time_count para obtener el número de instancias de Time.

@staticmethod: Utilizado para métodos que no necesitan acceder ni a la instancia (self) ni a la clase (cls). Por ejemplo, is_valid_format verifica si un formato es válido sin necesidad de instancias de Time.

4-¿Que es el cls?

cls en Python se usa en los métodos de clase. Es una referencia a la propia clase, similar a cómo self se refiere a la instancia de la clase. Permite acceder a los atributos y métodos de clase y no a la instancia específica.

5-¿Que hace print(f"El tiempo es: {time_obj.get_time()}")?

la f antes de la cadena indica que es una f-string (o cadena de formato en inglés, formatted string). Las f-strings permiten incluir expresiones dentro de llaves {}, que serán evaluadas y sus resultados se insertarán en la cadena.

6-¿Qué hace current_time = Time.from_string(time_str)?

Esta línea de código está creando un objeto current_time a partir de una cadena de texto time_str utilizando el método from_string de la clase Time. En otras palabras, está convirtiendo una representación en texto de una hora en un objeto de tiempo que puede ser manipulado y utilizado en el programa.

7-¿Cómo puedo manejar excepciones específicas en Python?

Con la línea except ValueError. En este caso, está diseñada para capturar y manejar cualquier excepción de tipo ValueError que pueda ocurrir en el bloque try anterior. Esto es útil para evitar que el programa se detenga abruptamente debido a errores que se pueden prever y manejar adecuadamente.
