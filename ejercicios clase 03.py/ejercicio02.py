import random

var1 = "hola"

var2 = "Mundo"

var3 = 2

var4 = 5

lista = [var1,var2,var3,var4]

v1 = random.choice(lista)

v2 = random.choice(lista)

if type(v1) != type(v2):
	print("Los tipos de datos",v1," y ",v2,"son distintos")
else:
	print("Los tipos de datos",v1," y ",v2,"son iguales")