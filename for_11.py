#Dado un número entero n, imprimir la secuencia de números primos menores o iguales a n
n = int(input("ingrese un numero entero: "))
for num in range(2, n+1):
    # comprobar si el número es primo
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")