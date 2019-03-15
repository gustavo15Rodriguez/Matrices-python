#-*-coding:utf-8-*-

'''44. Leer dos matrices 5x5 enteras y determinar si el promedio entero de los números
terminados en 4 de una matriz se encuentra al menos 3 veces en la otra matriz. '''

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

	suma = 0
	prom = 0
	cont = 0
	for k in range(len(matriz1)):
		for l in range(len(matriz1[k])):
			num1 = matriz1[k][l]
			if num1%10==4:
				suma+=num1
				cont+=1

	if suma>0:
		prom = suma//cont

	else:
		print "No hay numeros terminados en 4."

	cont = 0
	for g in range(len(matriz2)):
		for s in range(len(matriz2[k])):
			num2 = matriz2[g][s]
			if prom==num2:
				cont+=1

	if cont >=3:
		print "El promedio de los numeros terminados en 4 es: %d"%prom
		print "El promedio de los numeros terminados en 4 se repite %d veces en la otra matriz."%cont

	else:
		print "El promedio de los numeros terminados en 4 es: %d"%prom
		print "El promedio de los numeros terminados en 4 no se repite en la otra matriz."

except ValueError:
	print "Error..."