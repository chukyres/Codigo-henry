n = 1

while True:
	var = int(input("Ingrese un numero entero: "))
	if var > 0:
		break
	else:
		continue

for x  in range(1,var+1):
	multi = var*(var-1)
	var = var-1
	print(var)
input()