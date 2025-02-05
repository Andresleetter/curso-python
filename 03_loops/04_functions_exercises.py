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

#Ejercicio 3: suma de numeros
#Crea una función que tome una lista de números y devuelva la suma de esos números.
#Pista: Utiliza un bucle for para iterar sobre la lista y acumular la suma.

def suma_numeros(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

print("\nEjercicio 3")
numeros = [4, 6, 7, 9, 12, 3]
print(suma_numeros(numeros))

#Ejercicio 4: Factorial de un numero
#Crea una función que calcule el factorial de un número entero no negativo. 
#Pista: Utiliza un bucle for para multiplicar los números desde 1 hasta el número dado.

def factorial(numero):
    resultado = 1
    for i in range(1 ,numero+1):
        resultado *= i
    return resultado

print("\nEjercicio 4")
numero = int(input("Ingrese un entero (POSITIVO): "))
print(f"El factorial de {numero} es: ", factorial(numero))

#Ejercicio 5: Contador de vocales
#Crea una función que tome una cadena de texto y devuelva el número de vocales en la cadena. 
#Pista: Utiliza un bucle for para iterar sobre la cadena y un condicional para verificar 
#si un carácter es una vocal.

def contador_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador

print("\nEjercicio 5")
cadena = input("Escriba una cadena de texto: ")
print(f"La cantidad de vocales que tiene {cadena} es: ", contador_vocales(cadena))