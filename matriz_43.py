#-*-coding:utf-8-*-

'''43. Leer dos matrices 5x5 enteras y determinar si el promedio entero de los números pares
de una matriz es igual al promedio de los números pares de la otra matriz.'''

if __name__ == '__main__':
	matriz1 = []
	matriz2 = []
	
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

	suma1 = 0
	cont1 = 0
	prom1 = 0
	for k in range(len(matriz1)):
		for l in range(len(matriz1[k])):
			num1 = matriz1[k][l]
			if num1%2==0:
				suma1+=num1
				cont1+=1

		prom1 = suma1//cont1

	suma2 = 0
	cont2 = 0
	prom2 = 0
	for g in range(len(matriz2)):
		for s in range(len(matriz2[g])):
			num2 = matriz2[g][s]
			if num2%2==0:
				suma2+=num2
				cont2+=1

		prom2 = suma2//cont2

	if prom1==prom2:
		print "El promedio de los numeros pares de la primer matriz es: %d"%prom1
		print "El promedio de los numeros pares de la segunda matriz es: %d"%prom2
		print "El promedio de los numeros pares de ambas matrices es igual."

	else:
		print "El promedio de los numeros pares de la primer matriz es: %d"%prom1
		print "El promedio de los numeros pares de la segunda matriz es: %d"%prom2
		print "El promedio de los numeros pares de ambas matrices es diferente."

except ValueError:
	print "Error..."