#Escribir una función que reciba un string y devuelva el mismo string todo en mayúsculas.
def recibidor_strings (texto):
   respuesta = texto.upper()  
   return respuesta
respuesta_mayus = recibidor_strings("algo en mayusculas")
print(respuesta_mayus)

#Escribir una función que reciba un string y devuelva el mismo string todo en minúsculas.
def recibidor_strings (texto):
   respuesta = texto.lower()  
   return respuesta
respuesta_mayus = recibidor_strings("ALGO EN MINUSCULAS")
print(respuesta_mayus)
#Escribir una función que tome dos strings y devuelva un nuevo string que contenga ambos strings concatenados, separados por un espacio.
def tomador_strings (texto1,texto2): 
   respuesta = texto1 + " " + texto2
   return respuesta
respuesta_concatenada = tomador_strings("texto","concatenado")
print(respuesta_concatenada)
#Escribir una función que tome un string y devuelva el número de caracteres que tiene el string.
def contador_caracteres (texto):
   respuesta = len(texto)
   return respuesta
respuesta_contada = contador_caracteres("texto")
print(respuesta_contada)
#Escribir una función que tome un string y un carácter y devuelva el número de veces que aparece ese carácter en el string.
def contar_caracter(texto,caracter):
   respuesta = texto.count(caracter)
   return respuesta
respuesta_caracter_contado = contar_caracter("manzana","a")
print(respuesta_caracter_contado)
#Escribir una función que tome un string y un carácter y devuelva una lista con todas las palabras en el string que contienen ese carácter.
def enlistar_palabras(texto,caracter):
   lista=[]
   respuesta = texto.split()
   for palabra in respuesta:
    if (caracter in palabra):
       lista.append(palabra)
   return lista
respuesta_palabras_enlistadas = enlistar_palabras("las manzanas cayeron de los arboles", "o")
print(respuesta_palabras_enlistadas)
#Escribir una función que tome un string y devuelva el mismo string con los espacios eliminados
def eliminar_espacios (texto):
   respuesta = texto.replace(" ", "")  
   return respuesta
respuesta_sin_espacios = eliminar_espacios("algo con espacios")
print(respuesta_sin_espacios)
#Escribir una función que reciba dos string (nombre y apellido) y devuelva un diccionario con el nombre y apellido, 
# eliminando los espacios del comienzo y el final y colocando la primer letra en mayúscula
def creador_diccionarios (nombre, apellido):
   diccionario = {}
   respuesta_nombre = nombre.strip().capitalize()
   respuesta_apellido = apellido.strip().capitalize()
   diccionario ["Name"]= respuesta_nombre
   diccionario ["Surname"]= respuesta_apellido
   return diccionario
respuesta_diccionario_capitalizar = creador_diccionarios(" juan "," perez ") 
print(respuesta_diccionario_capitalizar)
#Escribir una función que tome una lista de nombres y los una en una sola 
#cadena separada por un salto de línea, por ejemplo: ["Juan", "María", "Pedro"] -> "Juan\nMaría\nPedro".
def saltar_linea (lista):
   cadena = "\n"
   cadena = cadena.join(lista)
   return cadena
lista = ["Juan", "María", "Pedro"]
respuesta_salteado_linea = saltar_linea(lista)
print(respuesta_salteado_linea)
#Escribir una función que tome un nombre y un apellido y devuelva un email en formato "inicial_nombre.apellido@utn-fra.com.ar"
def creador_mail (nombre, apellido):
   mail = "{0}_{1}.{2}@utn-fra.com.ar".format(nombre[0], nombre, apellido)
   return mail
respuesta_mail_creado = creador_mail("juan","perez") 
print(respuesta_mail_creado)
#Escribir una función que tome una lista de palabras y devuelva un string que contenga todas las palabras concatenadas con comas
#  y "y" antes de la última palabra. Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"], el string resultante debería ser
#  "manzanas, naranjas y bananas"..
def concatenar_listas (lista):
    if (len(lista) == 1):
        return lista[0]
    elif (len(lista) == 2):
       return lista[0] + "y" + lista[1]
    else: 
       return  ", ".join(lista[:-1]) + " y " + lista[-1]
lista = ["manzanas", "naranjas", "bananas"]
print(len(lista))
respuesta_lista_concatenada = concatenar_listas(lista)
print(respuesta_lista_concatenada)
#Escribir una función que tome un número de tarjeta de crédito como input, verificar que todos los caracteres sean numéricos
#  y devolver los últimos cuatro dígitos y los primeros dígitos como asteriscos, por ejemplo: "**** **** **** 1234". 
def tarjeta_de_credito_ultimos_nums(string):
    """
    - Verifica que los caracteres sean numericos y muestra los ultimos 4
    - Recibe un string
    - Retorna una string con los ultimos 4 numeros visibles
    """
    string_sin_espacios = string.replace(" ", "")  # Elimina todos los espacios
    if string_sin_espacios.isdigit():
        return "**** **** **** {}".format(string_sin_espacios[-4:])
    else:
        return "No es el numero de una tarjeta"

string =(input("ingrese el numero de la tarjeta"))

print(tarjeta_de_credito_ultimos_nums(string))