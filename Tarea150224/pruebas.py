def ordenar_por_nombre(datos):
    # Utilizar la función sorted para ordenar los datos por el primer elemento de cada subarreglo (nombre)
    datos_ordenados = sorted(datos, key=lambda x: x[0])
    return datos_ordenados

# Ejemplo de uso
arreglos = [
    ["Juan", 170, 65],
    ["Maria", 160, 55],
    ["Carlos", 175, 70],
    # Agrega más datos si es necesario
]

arreglos_ordenados = ordenar_por_nombre(arreglos)

# Mostrar los datos ordenados
for arreglo in arreglos_ordenados:
    print(arreglo)
