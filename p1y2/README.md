# PREGUNTAS HECHAS A LA IA(CHATGPT) DE LA PRACTICA 1

# EJERCICIO 1
1-¿Qué hace la funcion range? --> range(1,6)  
La función range lo que hace es contar desde el primer numero (1) hasta el ultimo -1 (5)

2-¿Que significa la operacion %? --> i%2
La operación representa el calculo del modulo, por ejemplo 1%2=1

3-¿Para que sirve el if?
El if es un condicional que se ejecuta en el caso de que la condición propuesta en la funcion se cumpla.

4-¿Para que se una el for? -->for i in range(1,6)
Es un bucle finito el cual va dando valores a i desde 1 hasta 6 incrementando su valor de 1 en 1

5-¿Que hace el break?
El break lo que hace es salir del bucle for, acaba con el bucle y le pone fin

6-¿Que hace el pass?
El pass es una declaracion nula que no realiza ninguna accion

# EJERCICIO 2
1-¿Como puedoconvertir un texto en minusulas?
Usando la función .lower haces que el texto se convierta en minusculas

2-¿Porque inicializa la variable count_replacements a 0?
Para definir un punto de inicio: Inicializar a 0 puede indicar que estás comenzando desde un estado neutral.

3-¿Para que sirve la operación +=?
Se utiliza para ir incrementando de 1 en 1 la variable count_replacements y vaya contando el numero de veces que se repiten las palabras.

4-¿Para que sirve el return?
Se utiliza para devolver un valor al lugar donde se llama a la función

# EJERCICIO 3

1-¿Como defines una función en python?
Para definir una función debes escribirla como: def nombre de la funcion (parametros que quieras pasarle a la función) 

2-¿Cuál es la funcionalidad e .append?
Su uso se basa unicamente en añadir al final de la cadena los numeros que vayan cumpliendo las condiciones if.

3-¿Que hace la linea primes = prime_list(limit)?
Esta linea guarda en la variable primes todos los valores de los numeros primos encontrados por la función prime_list

4-¿Que hace la instrucción if str(prime) == str(prime)[::-1]:?
Para saber que una palabra es un palindromo tienen que leerse iguales de delante hacia  atras que atras hacia delante, con [::-1] lo que hace es dar la vuelta al texto, poniendo al principio lo que estaba en el final y con el str compara un texto con el otro modificado y en caso de que sean iguales esta función devuelve un 1.

# EJERCICIO 4

1-¿Que hace la instrucción map(int, entrada.split())?
La función split() divide la cadena en una lista de subcadenas (strings) en cada espacio. Por ejemplo, si entrada es "1 2 -3 4", el resultado sería ["1", "2", "-3", "4"].

map(int, entrada.split()) aplica la función int a cada elemento de la lista obtenida por entrada.split(), convirtiendo cada subcadena a un entero. Ejemplo: map(int, ["1", "2", "-3", "4"]) produce un iterable de enteros: 1, 2, -3, 4.

Finalmente, list(...) convierte el iterable producido por map() en una lista de Python.

Por lo tanto, list(map(int, entrada.split())) genera una lista de enteros a partir de la cadena de entrada.

2-¿Para sumar numeros de una lista?
sum(lista)

3-¿Como saber si un elemento de un alista es unico?
return len(lista) == len(set(lista))

 # EJERCICIO 5
¿Que es tareas y para que se crea?
Es un tipo de dato: tareas[] es una lista, que es una estructura de datos en Python que permite almacenar una colección de elementos. Las listas son dinámicas, lo que significa que pueden cambiar de tamaño (puedes añadir o eliminar elementos).

¿Que significa "except ValueError"?
Este bloque se ejecuta si se produce un error de tipo ValueError dentro del bloque try. El ValueError es un tipo específico de excepción que se lanza cuando una operación o función recibe un argumento con el tipo correcto pero con un valor inapropiado.

# EJERCICIO 6

¿Cual es la funcion de len()?
len() cuenta todos los caracteres, incluidos espacios, signos de puntuación y caracteres especiales

¿Qué función tiene max?
max() en Python se utiliza para encontrar el valor máximo en un iterable

¿Que hace el comando is?
se utiliza para comprobar si cadena1 y cadena2 son el mismo objeto en memoria.
is: Es un operador de identidad en Python que verifica si dos variables apuntan al mismo objeto en memoria. Es diferente del operador ==, que comprueba si los valores de los objetos son iguales.





