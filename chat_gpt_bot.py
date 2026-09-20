# ============================================================
# 🐍 PYTHON DESDE CERO - EJEMPLOS BÁSICOS
# ============================================================
# Aquí vamos a practicar:
# comentarios, variables, tipos de datos, print, input,
# if, elif, else, while, for, break, continue, lower,
# funciones (def), return, clases (class) y más.
# ============================================================


# 1. COMENTARIOS

# Esto es un comentario de una sola línea.
# Python ignora todo lo que escribamos después del símbolo #.


"""
Esto parece un comentario de varias líneas,
pero técnicamente Python lo interpreta como
un string de varias líneas que no estamos utilizando.

Se suele utilizar para documentar código.
"""


'''
También podemos escribir strings
utilizando tres comillas simples.
'''


# 2. VARIABLES

# Una variable es como una cajita donde guardamos información.

my_name = 'UrielSA'          # str = texto
universidad = 'HyBridge'     # str = texto
soy = 'Estudiante actual'    # str = texto

edad = 22                    # int = número entero
altura = 1.80                # float = número decimal

soy_estudiante = True        # bool = verdadero
soy_estudiante2 = False      # bool = falso


# 3. MOSTRAR INFORMACIÓN CON print()

print(my_name)
print(universidad)
print(soy)
print(edad)
print(altura)
print(soy_estudiante)
print(soy_estudiante2)


# 4. SABER EL TIPO DE DATO

print(type(my_name))
print(type(edad))
print(type(altura))
print(type(soy_estudiante))


# Si queremos solamente el nombre del tipo:

print(type(my_name).__name__)
print(type(edad).__name__)
print(type(altura).__name__)
print(type(soy_estudiante).__name__)


# 5. STR = TEXTO

nombre = "Uriel"

print(nombre)

# Podemos unir textos:

nombre = "Uriel"
apellido = "SA"

nombre_completo = nombre + " " + apellido

print(nombre_completo)


# 6. INT = NÚMEROS ENTEROS

edad = 22
anio = 2026

print(edad)
print(anio)

# También podemos hacer operaciones:

numero1 = 10
numero2 = 5

print(numero1 + numero2)  # suma
print(numero1 - numero2)  # resta
print(numero1 * numero2)  # multiplicación
print(numero1 / numero2)  # división


# 7. FLOAT = NÚMEROS DECIMALES

altura = 1.80
precio = 99.99

print(altura)
print(precio)


# 8. BOOL = TRUE / FALSE

soy_estudiante = True

print(soy_estudiante)

# True significa verdadero.
# False significa falso.


# 9. COMPARACIONES

edad = 22

print(edad == 22)  # ¿edad es igual a 22?
print(edad != 18)  # ¿edad es diferente de 18?
print(edad > 18)   # ¿edad es mayor que 18?
print(edad < 30)   # ¿edad es menor que 30?
print(edad >= 22)  # ¿edad es mayor o igual a 22?
print(edad <= 25)  # ¿edad es menor o igual a 25?


# 10. IF

# IF significa:
# "SI esto ocurre, haz esto".

edad = 22

if edad >= 18:
    print("Eres mayor de edad")


# Otro ejemplo:

nombre = "Uriel"

if nombre == "Uriel":
    print("Hola Uriel")


# IMPORTANTE:
# Python utiliza espacios (indentación) para saber
# qué código pertenece al IF.


# 11. ELSE

# ELSE significa:
# "SI NO se cumple el IF, haz esto".

edad = 15

if edad >= 18:
    print("Puedes entrar")
else:
    print("No puedes entrar")


# 12. ELIF

# ELIF significa:
# "Si lo anterior no ocurrió, revisa esta otra condición".

edad = 20

if edad < 13:
    print("Eres niño")

elif edad < 18:
    print("Eres adolescente")

else:
    print("Eres adulto")


# Podemos tener varios ELIF:

calificacion = 8

if calificacion == 10:
    print("Excelente")

elif calificacion >= 8:
    print("Muy bien")

elif calificacion >= 6:
    print("Aprobaste")

else:
    print("Reprobaste")


# 13. AND

# AND significa que AMBAS condiciones deben cumplirse.

edad = 22
tiene_identificacion = True

if edad >= 18 and tiene_identificacion:
    print("Puedes entrar")
else:
    print("No puedes entrar")


# 14. OR

# OR significa que por lo menos UNA condición debe cumplirse.

dia = "sabado"

if dia == "sabado" or dia == "domingo":
    print("Es fin de semana")


# 15. NOT

# NOT significa "NO".

soy_estudiante = False

if not soy_estudiante:
    print("No eres estudiante")


# 16. LOWER()

# lower() convierte un texto a minúsculas.

nombre = "URIEL"

print(nombre.lower())

# Resultado:
# uriel


# Esto es muy útil para comparar textos:

respuesta = "SI"

if respuesta.lower() == "si":
    print("Elegiste que sí")


# Aunque el usuario escriba:
# SI
# Si
# sI
# si
#
# lower() lo convierte a:
# si


# 17. UPPER()

# upper() convierte todo a MAYÚSCULAS.

nombre = "uriel"

print(nombre.upper())

# Resultado:
# URIEL


# 18. INPUT()

# input() sirve para pedir información al usuario.

nombre = input("¿Cuál es tu nombre? ")

print("Hola mundo", nombre)


# IMPORTANTE:
# input() normalmente devuelve texto (str).


# 19. INPUT + INT

# Si queremos pedir un número entero:

edad = int(input("¿Cuál es tu edad? "))

print("Tu edad es:", edad)


# Ahora podemos hacer operaciones:

numero = int(input("Escribe un número: "))

print(numero + 10)


# 20. INPUT + FLOAT

altura = float(input("¿Cuál es tu altura? "))

print("Tu altura es:", altura)


# 21. WHILE

# WHILE significa:
# "MIENTRAS esta condición sea verdadera,
# sigue repitiendo".

contador = 1

while contador <= 5:
    print(contador)
    contador = contador + 1


# Resultado:
# 1
# 2
# 3
# 4
# 5


# 22. WHILE CON INPUT

numero = 1

while numero <= 3:
    print("Hola")
    numero = numero + 1


# El mensaje aparecerá 3 veces.


# 23. BREAK

# BREAK sirve para detener un ciclo inmediatamente.

contador = 1

while contador <= 10:

    print(contador)

    if contador == 5:
        break

    contador = contador + 1


# El ciclo se detiene cuando llega al 5.


# 24. CONTINUE

# CONTINUE salta esa vuelta del ciclo
# y continúa con la siguiente.

contador = 0

while contador < 5:

    contador = contador + 1

    if contador == 3:
        continue

    print(contador)


# El número 3 no se imprime.


# 25. FOR

# FOR sirve para repetir algo recorriendo elementos.

for numero in range(5):
    print(numero)


# Resultado:
# 0
# 1
# 2
# 3
# 4


# 26. FOR CON RANGE()

for numero in range(1, 6):
    print(numero)


# Resultado:
# 1
# 2
# 3
# 4
# 5


# 27. LISTAS

# Una lista permite guardar varios datos.

frutas = ["manzana", "pera", "platano", "uva"]

print(frutas)


# Podemos acceder a un elemento utilizando su posición.

print(frutas[0])
print(frutas[1])
print(frutas[2])


# IMPORTANTE:
# Python comienza a contar desde 0.


# 28. RECORRER UNA LISTA

frutas = ["manzana", "pera", "platano"]

for fruta in frutas:
    print(fruta)


# 29. AGREGAR ELEMENTOS A UNA LISTA

frutas = ["manzana", "pera"]

frutas.append("uva")

print(frutas)


# 30. FUNCIONES CON def

# Una función es un bloque de código
# que podemos reutilizar.

def saludar():
    print("Hola, bienvenido a Python")


# Para ejecutar la función:

saludar()


# 31. FUNCIÓN CON PARÁMETROS

# Podemos enviar información a una función.

def saludar(nombre):
    print("Hola", nombre)


saludar("Uriel")
saludar("Alondra")
saludar("Josaft")


# 32. VARIOS PARÁMETROS

def presentar(nombre, edad):
    print("Mi nombre es", nombre)
    print("Tengo", edad, "años")


presentar("Uriel", 22)


# 33. RETURN

# RETURN sirve para devolver un resultado
# desde una función.

def sumar(numero1, numero2):

    resultado = numero1 + numero2

    return resultado


resultado = sumar(10, 5)

print(resultado)


# También podemos hacerlo directamente:

print(sumar(20, 30))


# 34. DIFERENCIA ENTRE print() Y return

def ejemplo_print():
    print("Hola")


def ejemplo_return():
    return "Hola"


ejemplo_print()

mensaje = ejemplo_return()

print(mensaje)


# PRINT muestra algo en pantalla.
# RETURN devuelve un valor para poder utilizarlo después.


# 35. FUNCIÓN CON IF

def revisar_edad(edad):

    if edad >= 18:
        return "Eres mayor de edad"

    else:
        return "Eres menor de edad"


print(revisar_edad(22))
print(revisar_edad(15))


# 36. CLASES CON class

# Una clase es como un molde.
#
# Por ejemplo:
# podemos crear un molde llamado Persona
# y después crear diferentes personas utilizando ese molde.

class Persona:

    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad


# Ahora creamos objetos utilizando nuestra clase.

persona1 = Persona("Uriel", 22)
persona2 = Persona("Ana", 20)


print(persona1.nombre)
print(persona1.edad)

print(persona2.nombre)
print(persona2.edad)


# 37. MÉTODOS DENTRO DE UNA CLASE

class Persona:

    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad

    def saludar(self):

        print("Hola, soy", self.nombre)


persona1 = Persona("Uriel", 22)

persona1.saludar()


# 38. EJEMPLO COMPLETO

# Aquí juntamos varias cosas que aprendimos.

def revisar_usuario(nombre, edad):

    if edad >= 18:

        print("Hola", nombre)
        print("Eres mayor de edad")

    elif edad >= 13:

        print("Hola", nombre)
        print("Eres adolescente")

    else:

        print("Hola", nombre)
        print("Eres menor de edad")


nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))

revisar_usuario(nombre, edad)


# 39. EJEMPLO DE UN PEQUEÑO MENÚ

while True:

    print("\n===== MENÚ =====")
    print("1. Saludar")
    print("2. Mostrar mensaje")
    print("3. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":

        print("¡Hola! 👋")

    elif opcion == "2":

        print("Estás aprendiendo Python 🐍")

    elif opcion == "3":

        print("Programa terminado.")
        break

    else:

        print("Opción no válida.")


# 🧠 RESUMEN RÁPIDO

# print()
# -> Muestra información en pantalla.

# input()
# -> Pide información al usuario.

# if
# -> Si una condición se cumple.

# elif
# -> Si la condición anterior no se cumple,
#    revisa otra condición.

# else
# -> Si ninguna condición anterior se cumple.

# while
# -> Repite mientras una condición sea verdadera.

# for
# -> Recorre elementos o repite una cantidad determinada.

# break
# -> Detiene un ciclo.

# continue
# -> Salta una vuelta del ciclo.

# lower()
# -> Convierte texto a minúsculas.

# upper()
# -> Convierte texto a mayúsculas.

# def
# -> Crea una función.

# return
# -> Devuelve un valor desde una función.

# class
# -> Crea una clase, que funciona como un molde
#    para crear objetos.

# int
# -> Número entero.

# float
# -> Número decimal.

# str
# -> Texto.

# bool
# -> True o False.

# list
# -> Colección de elementos.


# ============================================================
# 💙❤️ FIN
# ============================================================

# Sigue practicando poco a poco.
# Primero aprende las bases y después ve aumentando
# la dificultad.
#
# Recuerda:
# programar es practicar, equivocarse, buscar el error
# y volver a intentarlo. 🐍💻
#
# ¡Suerte en tus practicas! ⭐
# Y no olvides comer frutas, verduras y bañarte xd 😂
