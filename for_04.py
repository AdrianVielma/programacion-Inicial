#Dado un número entero n, imprimir la suma de los números impares menores o iguales a n.
# num = input('ingrese un numero entero.')
# num = int(num)
# acumulador = 0
# lista_numero = list(range(1, num+1, 2))
# for suma in lista_numero:
#    acumulador = acumulador + suma
# print(acumulador)
n = int(input("Ingrese un número entero: "))
suma = 0

for i in range(1, n+1, 2):
    suma += i

print("La suma de los números impares menores o iguales a", n, "es", suma)