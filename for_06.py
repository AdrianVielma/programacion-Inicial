#Dada una lista de palabras, imprimir la cantidad total de vocales en la lista
contador = 0
lista = ('manzana', 'cielo', 'computadora', 'montana', 'jirafa')

for palabra in lista: 
    for letra in palabra:
        if letra in ('a', 'e', 'i', 'o', 'u'):
            contador= contador + 1 
print(contador)