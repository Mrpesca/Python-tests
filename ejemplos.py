#Ejemplos de DEEPSEEK para los temas del curso
# Ejemplos de conceptos básicos y sintaxis de Python

# 1. Variables y tipos de datos
nombre = "Juan"
edad = 25
altura = 1.75
es_estudiante = True

# 2. Operadores
suma = 10 + 5
resta = 10 - 5
multiplicacion = 10 * 5
division = 10 / 5
modulo = 10 % 3

# 3. Condicionales
if edad > 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# 4. Bucles
for i in range(5):
    print(f"Iteración {i}")

contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

# 5. Listas
frutas = ["manzana", "banana", "cereza"]
frutas.append("naranja")
print(frutas)

# 6. Tuplas
coordenadas = (10, 20)
print(coordenadas)

# 7. Diccionarios
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}
print(persona["nombre"])

# 8. Sets
numeros = {1, 2, 3, 4, 5}
numeros.add(6)
print(numeros)

# 9. Funciones
def saludar(nombre):
    return f"Hola, {nombre}"

print(saludar("Juan"))

# 10. Manejo de excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")

# 11. Entrada y salida de datos
nombre_usuario = input("Introduce tu nombre: ")
print(f"Bienvenido, {nombre_usuario}")

# 12. Módulos y librerías
import math
print(math.sqrt(16))

# 13. Clases y objetos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Soy {self.nombre} y tengo {self.edad} años"

persona1 = Persona("Ana", 30)
print(persona1.presentarse())

# 14. Iteradores
mi_lista = [1, 2, 3]
mi_iterador = iter(mi_lista)
print(next(mi_iterador))

# 15. Expresiones lambda
cuadrado = lambda x: x ** 2
print(cuadrado(5))

# 16. Listas por comprensión
cuadrados = [x ** 2 for x in range(10)]
print(cuadrados)

# 17. Manejo de archivos
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, mundo")

with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# 18. Decoradores
def mi_decorador(func):
    def wrapper():
        print("Algo antes de la función")
        func()
        print("Algo después de la función")
    return wrapper

@mi_decorador
def decir_hola():
    print("¡Hola!")

decir_hola()

# 19. Generadores
def generador_numeros():
    yield 1
    yield 2
    yield 3

for numero in generador_numeros():
    print(numero)

# 20. Manejo de fechas y horas
from datetime import datetime
ahora = datetime.now()
print(ahora)

# 21. Expresiones regulares
import re
patron = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
email = "ejemplo@dominio.com"
if re.match(patron, email):
    print("Email válido")
else:
    print("Email no válido")

# 22. Manejo de JSON
import json
datos = '{"nombre": "Juan", "edad": 25}'
objeto = json.loads(datos)
print(objeto["nombre"])

# 23. Manejo de bases de datos (SQLite)
import sqlite3
conexion = sqlite3.connect("mi_base_de_datos.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre TEXT, edad INTEGER)")
cursor.execute("INSERT INTO usuarios VALUES ('Juan', 25)")
conexion.commit()
conexion.close()

# 24. Programación orientada a objetos (Herencia)
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

mi_perro = Perro("Rex")
print(mi_perro.hacer_sonido())

# 25. Manejo de errores personalizados
class MiErrorPersonalizado(Exception):
    pass

try:
    raise MiErrorPersonalizado("Este es un error personalizado")
except MiErrorPersonalizado as e:
    print(e)

# 26. Uso de contextos (with)
class MiContexto:
    def __enter__(self):
        print("Entrando en el contexto")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saliendo del contexto")

with MiContexto() as contexto:
    print("Dentro del contexto")

# 27. Uso de hilos
import threading

def tarea():
    print("Ejecutando tarea en un hilo")

hilo = threading.Thread(target=tarea)
hilo.start()
hilo.join()

# 28. Uso de multiprocesamiento
import multiprocessing

def tarea():
    print("Ejecutando tarea en un proceso")

proceso = multiprocessing.Process(target=tarea)
proceso.start()
proceso.join()

# 29. Uso de asyncio
import asyncio

async def tarea_asincrona():
    print("Iniciando tarea asíncrona")
    await asyncio.sleep(1)
    print("Tarea asíncrona completada")

asyncio.run(tarea_asincrona())

# 30. Uso de decoradores avanzados
def decorador_con_parametros(parametro):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(f"Parámetro del decorador: {parametro}")
            return func(*args, **kwargs)
        return wrapper
    return decorador

@decorador_con_parametros("Hola")
def funcion_decorada():
    print("Función decorada ejecutada")

funcion_decorada()