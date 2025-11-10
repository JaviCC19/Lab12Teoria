
print("\nEJERCICIO 1: Ordenar lista de diccionarios")

D = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Apple', 'model': 2, 'color': 'Silver'},
    {'make': 'Huawei', 'model': 50, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

print("Lista original:")
for item in D:
    print(item)

key = input("\nIngresa la key por la que deseas ordenar (make/model/color): ").strip()

# Ordenar con lambda
try:
    D_ordenado = sorted(D, key=lambda x: x[key])
    print("\nLista ordenada por", key + ":")
    for item in D_ordenado:
        print(item)
except KeyError:
    print("Error: la key ingresada no existe.")



print("\nEJERCICIO 2: Calcular potencias")

lista = list(range(1, 11))
print("Lista original:", lista)

n = int(input("Ingresa el valor de n para calcular x^n: "))

# Calcular potencia
resultado = list(map(lambda x: x ** n, lista))
print("Resultado:", resultado)



print("\nEJERCICIO 3: Matriz transpuesta")
print("Ejemplo de matriz: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")

filas = int(input("Ingresa el número de filas: "))
columnas = int(input("Ingresa el número de columnas: "))

# Crear matriz leyendo valores
X = []
for i in range(filas):
    fila = input(f"Ingrese los {columnas} elementos de la fila {i+1} separados por espacio: ").split()
    fila = list(map(int, fila))
    X.append(fila)

# Calcular transpuesta con lambda
transpuesta = lambda m: [list(fila) for fila in zip(*m)]
Y = transpuesta(X)

print("\nMatriz original:")
for fila in X:
    print(fila)
print("\nMatriz transpuesta:")
for fila in Y:
    print(fila)



print("\nEJERCICIO 4: Eliminar elementos de una lista")

lista_inicial = input("Ingresa los elementos de la lista separados por coma: ").replace(" ", "").split(",")
a_eliminar = input("Ingresa los elementos a eliminar separados por coma: ").replace(" ", "").split(",")

resultado = list(filter(lambda x: x not in a_eliminar, lista_inicial))

print("\nLista resultante después de eliminar los elementos indicados:")
print(resultado)
