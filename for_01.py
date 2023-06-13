#Dada una lista de números, imprimir el número más grande de la lista.
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
flag = 0 
num_max = 0
lista_numeros.append(99)
for num in lista_numeros:
    if (num > num_max or flag == 0):
        flag = 1
        num_max = num 

print(num)