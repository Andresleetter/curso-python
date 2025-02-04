# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.

def numeros_pares():
    print("\nEjercicio 1")
    for i in range (2, 21, 2):
        print(i)
        
numeros_pares()

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.

def calcular_media():
    print("\nEjercicio 2")
    numeros = [10, 20, 30, 40, 50]
    suma = 0
    for numero in numeros:
        suma += numero
    media = suma / len(numeros)
    print(f"la media de los numeros es: {media}")

calcular_media()

