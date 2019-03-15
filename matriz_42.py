#-*-coding:utf-8-*-

'''42. Leer dos matrices 5x5 enteras y determinar si el promedio entero de los números primos
de una matriz se encuentra almacenado en la otra matriz.'''

if __name__ == '__main__':
	matriz1 = []
	matriz2 = []
	primos1 = []
	primos2 = []
	
try:
	for i in range(5):
		fila1 = []
		fila2 = []
		for j in range(5):
			num1 = int(raw_input("Digite un numero para la primer matriz: "))
			num2 = int(raw_input("Digite un numero para la segunda matriz: "))
			fila1.append(num1)
			fila2.append(num2)

		matriz1.append(fila1)
		matriz2.append(fila2)

	cont = 0
	suma1 = 0
	prom1 = 0
	for k in range(len(matriz1)):
		for l in range(len(matriz1[k])):
			num1 = matriz1[k][l]
			cont1 = 0
			for z in range(1, num1+1):
				if num1%z==0:
					cont1+=1

			if cont1 == 2:
				primos1.append(num1)
				suma1+=num1
				cont +=1

		prom1 = suma1//cont

	contador = 0
	suma2 = 0
	prom2 = 0
	for g in range(len(matriz2)):
		for s in range(len(matriz2[g])):
			num2 = matriz2[g][s]
			cont2 = 0
			for q in range(1, num2+1):
				if num2%q==0:
					cont2+=1
					
			if cont2 == 2:
				primos2.append(num2)
				suma2+=num2
				contador+=1

		prom2 = suma2//contador

	c = 0
	for a in range(len(matriz2)):
		for b in range(len(matriz2[a])):
			if prom1==matriz2[a][b]:
				c+=1

	if c>0:
		print "El promedio de la primer matriz evaluada es %d."%prom1
		print "El promedio de la primer matriz si se encuentra almacenado en la segunda matriz."

	else:
		print "El promedio de la primer matriz evaluada es %d."%prom1
		print "El promedio de la primer matriz no se encuentra almacenado en la segunda matriz."
			
except ValueError:
	print "Error..."
