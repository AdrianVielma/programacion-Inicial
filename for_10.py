#Dada una lista de palabras, imprimir las palabras que comienzan y terminan con la misma letra.
contador = 0
lista_palabras = ['radar', 'somos', 'anana', 'computadora', 'perro']
for palabra in lista_palabras:
    primera_letra = palabra [0] 
    ultima_letra = palabra[-1]
    if primera_letra == ultima_letra:
      print(palabra) 