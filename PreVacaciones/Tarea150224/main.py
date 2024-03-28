import os

class lector_archivoTexto:
    def __init__(self, archivo):
        self.archivo = archivo

    def ordenar_por_nombre(self):
    # Utilizar la función sorted para ordenar los datos por el primer elemento de cada subarreglo (nombre)
        datos = self.texto_Arreglo(self.leer())
        datos_ordenados = sorted(datos, key=lambda x: x[0])
        return datos_ordenados


    def leer(self):
        texto = ""
        with open(self.archivo, 'r') as file:
            #print(file.read())
            texto += file.read()
        return texto
    
    def anadir(self, texto):
        with open(self.archivo, 'a') as file:
            file.write(texto)
        print("Texto añadido")
    
    def separador(self,texto):
        return texto.split("|")
    
    def texto_Arreglo(self, texto):
        arreglo = texto.split("\n")
        arreglo2 = []
        for elemento in arreglo:
            arreglo2.append(self.separador(elemento))
        return arreglo2

def saludo():
    print("Hola mundo")

def sobrescribir_archivo(self, nuevo_contenido):
    ruta_archivo = self.archivo;
    try:
        with open(ruta_archivo, 'w') as archivo:
            archivo.write(nuevo_contenido)
        print(f'Se ha sobrescrito el contenido del archivo "{ruta_archivo}" con éxito.')
    except Exception as e:
        print(f'Ocurrió un error al sobrescribir el archivo: {str(e)}')



"""
def seleccion():
    print("1.- Leer archivo")
    print("2.- Añadir texto")
    print("3.- Ordenar por nombre")
    print("4.- Salir")
    return input("Opción: ")

def opciones():
    seleccion = seleccion()
    if seleccion == "1":
        archivo = lector_archivoTexto("Tarea150224/archivo.txt")
        print(archivo.leer())
    elif seleccion == "2":
        archivo = lector_archivoTexto("Tarea150224/archivo.txt")
        archivo.anadir("\nTexto añadido")
    elif seleccion == "3":
        archivo = lector_archivoTexto("Tarea150224/archivo3.txt")
        hola = archivo.ordenar_por_nombre()
        for arreglo in hola:
            print(arreglo)
    elif seleccion == "4":
        print("Adios")
    else:
        print("Opción no válida")
"""
#saludo()
archivo = lector_archivoTexto("Tarea150224/archivo3.txt")
hola = archivo.ordenar_por_nombre()

for arreglo in hola:
    print(arreglo)
