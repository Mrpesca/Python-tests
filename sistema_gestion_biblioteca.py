#programa para la gestion de biblioteca
class Libro:

    def __init__(self,titulo,autor,isbn):
        self.titulo: str = titulo  # Debe ser un string
        self.autor: str = autor    # Debe ser un string
        self.isbn: str = isbn      # Debe ser un string
        self.disponible: bool = True # Este es un booleano

#funcion agregar, agreega un nueblo libro
    def agregar(self,inventario):
        inventario.append(self)
        print(f"Libro agregado con éxito: {self.titulo} ({self.autor}) - ISBN: {self.isbn}")

#funcion prestar, si el libro no esta disponible indicará que no está disponible
    def prestar(self):
        if self.disponible == True:
            self.disponible = False
            print(f"Libro prestado con éxito: {self.titulo} ({self.autor}) - ISBN: {self.isbn}")
        else:
            print(f"Libro {self.titulo} ya prestado.")

# funcion que indica si un libro ha sido devuelto o no           
    def devolver(self):
        if self.disponible == False:
            self.disponible = True
            print(f"Libro devuelto con éxito: {self.titulo} ({self.autor}) - ISBN: {self.isbn}")
        else:
            print(f"Libro {self.titulo} disponible.")

#funcion que devuelve una listra con los libros de la biblioteca            
    def mostrar(self):
            #disponibilidad = "Si" if self.disponible else "No"
            if self.disponible == True:
                disponibilidad = "Si"
            else:
                disponibilidad = "No"
            print(f"- {self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {disponibilidad}")
#funcion para buscar un libro por isbn            
    def buscar(self,isbn):
        if self.isbn == isbn:
            self.mostrar()
            return True
        return False
#----------------------------------------Fin creacion de libro----------------------------------------------------------
#Funcion para agregar un libro al inventario
def agregar_libro(inventario):
    titulo = input("Ingresa el Titulo:")
    autor = input("Ingresa el Autor:")
    isbn = input("Ingresa el ISBN:")
    libro = Libro(titulo,autor,isbn)
    libro.agregar(inventario)
#Funcion para prestar un libro si esta disponible
def prestar_libro(inventario):
    isbn = input("Ingresa el ISBN:")
    for libro in inventario:
        if libro.buscar(isbn):
            libro.prestar()
#Funcion devolver para devolver un libro si su disponibilidad es false
def devolver_libro(inventario):
    isbn = input("Ingresa el ISBN:")
    for libro in inventario:
        if libro.buscar(isbn):
            libro.devolver()
#Funcion que muestra todos los libros en el inventario
def mostrar_libros(inventario):
    if not inventario:
        print("No hay libros en el inventario.")
    else:
        for libro in inventario:
            libro.mostrar()
#Funcion que busca un libro por ISBN
def buscar_libro(inventario):
    isbn = input("Ingresa el ISBN: ")
    for libro in inventario:
        if libro.buscar(isbn):
            return
#funcion que ejecuta el programa MAIN    
def main():
    inventario = []
    while True:
        print("\nBienvenido al Sistema de Gestión de Biblioteca")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Buscar libro")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_libro(inventario)
        elif opcion == "2":
            prestar_libro(inventario)
        elif opcion == "3":
            devolver_libro(inventario)
        elif opcion == "4":
            mostrar_libros(inventario)
        elif opcion == "5":
            buscar_libro(inventario)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")
#main program
if __name__ == "__main__":
    main()

