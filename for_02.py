#Dada una lista de palabras, imprimir la palabra más larga de la lista
flag = 0
palabra_larga = ""
lista_palabras = ["zapatillas", "ojotas", "zapatos", "sandalias", "pantuflas"]

for palabra in lista_palabras:
    if (len(palabra) > len(palabra_larga) or flag == 0):
        palabra_larga = palabra
        flag = 1
print(palabra_larga)       