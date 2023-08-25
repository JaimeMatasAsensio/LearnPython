#Imports
import time

#Declaracion de variables
sep = ""
str1 = ""
str2 = ""
str3 = ""
va1 = ""
va2 = ""

#INIT
#Las variables en Python son contenedores de datos
#Estas se crean en el momento que se asigna una valor a ella
#No necesitan tener que ser declaradas de ningun tipo en particular
sep = "---*---"
str1 = "Las variables en Python son contenedores de datos\n"
str2 = "Estas se crean en el momento que se asigna una valor a ella\n"
str3 = "No necesitan tener que ser declaradas de ningun tipo en particular\n"
print (sep)
print(str1,str2,str3)
time.sleep(5) #Damos tiempo a leer

print("Creamos dos variables 'va1' y 'va2' ")

va1 = "soy un texto cualquiera"
va2 = "soy un texto pero quizas sea un numero"

print("Imprimimos las variables:\n")
print("Valor almacenado en va1: ", va1, "\n")
print("Valor almacenado en va2: ", va2, "\n")

#Podemos modificar el tipo volviendo asignar un nuevo valor
#Si tratamos de mostrar el valor de esta variable con el operador '+' fallara
#Por ello debemos usar ',' para presentar el valor

str1 = "Podemos modificar el tipo volviendo asignar un nuevo valor\n"
str2 = "Si tratamos de mostrar el valor de esta variable con el operador + fallara\n"
str3 = "Por ello debemos usar ',' para presentar el valor\n"
print (sep)
print(str1,str2,str3)
time.sleep(5) #Damos tiempo a leer

va2 = 300
print("Ahora va2 se convertira en un numero!\n")
print("Valor actualizado en va2: ", va2, "\n")

#Tambien podemos transformar o hacer casting sobre variables ya definidas, cambiando su tipo de uno a otro

str1 = "Tambien podemos transformar o hacer casting sobre variables ya definidas, cambiando su tipo de uno a otro\n"
print (sep)
print(str1)
time.sleep(5) #Damos tiempo a leer

print("Ahora la variable va2 se comportara como un string. " + str(va2) )
print("Tambien podemos seguir utilizandola como un numero. Hacemos una suma con ella misma: ", va2 + va2 , "\n")

#Podemos obtener el tipo de las variables si lo necesitamos
str1 = "Podemos obtener el tipo de las variables si lo necesitamos con la funcion type()\n"
print (sep)
print(str1)
time.sleep(5) #Damos tiempo a leer

print("Tipo de dato para la varible va1 : ", type(va1))
print("Tipo de dato para la varible va2 : ", type(va2))


#Tenemos distintos tipos de datos en Python.
# Str, int, float, complex, list. tuple, range, dict, set, frozenset, bool, bytes, bytearray, memeryview, NoneType

#Podemos obtener el tipo de las variables si lo necesitamos
str1 = "Tenemos distintos tipos de datos en Python. \n"
str2 = "Str, int, float, complex, list. tuple, range, dict, set, frozenset, bool, bytes, bytearray, memeryview, NoneType \n"
str3 = "Ahora crearemos una variable de cada tipo y las visualizaremos. \n"
print (sep)
print(str1,str2,str3)

time.sleep(5) #Damos tiempo a leer

#Tipo String
va1 = "Esta variable 'va1' es de tipo String"
print(va1,type(va1))

#Tipo int
va1 = 1234
print(va1,"Cambio de tipo -> ",type(va1))

#Tipo float
va1 = 123.4
print(va1,"Cambio de tipo -> ",type(va1))

#Tipo complex
va1 = 1j
print(va1,"Cambio de tipo -> ",type(va1))

#Tipo range
va1 = range(5) 
print("Recorremos la variable 'va1'")
print ("tenemos la funcion range(int). Esta funcion podemos ver un rago de int-1 numeros. Hay mas opciones..")

time.sleep(5) #Damos tiempo a leer

for va2 in va1:
    print(va2)
else:
    print("Fin de la variable tipo ->", type(va1))

#Tipo list
print ("Las listas pueden almacenar distintos valores, son ordenadas, modificlables y permiten valores repetidos")
va1 = ["Ananas","Banana","Platano","Ananas"]
print("Cambio de tipo -> ",type(va1))

time.sleep(5) #Damos tiempo a leer
print("Recorremos la variable 'va1'")

for va2 in va1:
    print(va2)
else:
    print("Fin de la variable tipo ->", type(va1))

#Tipo tuple
print ("Las tuplas pueden almacenar distintos valores, son ordenadas, NO modificlables y permiten valores repetidos")
va1 = ("String1","String2","String3")
print("Cambio de tipo -> ",type(va1))

time.sleep(5) #Damos tiempo a leer
print("Recorremos la variable 'va1'")

for va2 in va1:
    print(va2)
else:
    print("Fin de la variable tipo ->", type(va1))

#Tipo dict
print ("Los diccionarios pueden almacenar pares de valores key-value, son ordenadas, modificlables y NO permiten valores repetidos")
va1 = {
    "nombre": "Diccionario",
    "numero": 1234,
    "complex": 1j 
}
print ("Usamos algunos de los metodos...")
print("metodo keys", va1.keys())
print("metodo items", va1.items())

time.sleep(5) #Damos tiempo a leer

print("Iniciamos el recorrido del diccionario")
for x in va1.keys():
    print(x,va1.get(x))
else:
    print("Terminamos el recorrido del diccionario")


#Tipo set -> Pendiente

