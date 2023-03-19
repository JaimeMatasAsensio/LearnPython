import time
#Las variables en Python son contenedores de datos
#Estas se crean en el momento que se asigna una valor a ella
#No necesitan tener que ser declaradas de ningun tipo en particular

str1 = "Las variables en Python son contenedores de datos\n"
str2 = "Estas se crean en el momento que se asigna una valor a ella\n"
str3 = "No necesitan tener que ser declaradas de ningun tipo en particular\n"

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

print(str1,str2,str3)
time.sleep(5) #Damos tiempo a leer

va2 = 300
print("Ahora va2 se convertira en un numero!\n")
print("Valor actualizado en va2: ", va2, "\n")

