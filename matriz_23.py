#-*-coding:utf-8-*-

'''23. Leer dos matrices 4x5 enteras y determinar si el número mayor de una de las matrices es
igual al número mayor de la otra matriz. '''

if __name__ == '__main__':
	matriz1 = []
	matriz2 = []
	mayor1 = 0
	mayor2 = 0
	
try:
	for i in range(4):
		fila1 = []
		fila2 = []
		for j in range(5):
			num1 = int(raw_input("Digite el numero para la primer matriz: "))
			num2 = int(raw_input("Digite el numero para la segunda matriz: "))
			fila1.append(num1)
			fila2.append(num2)

		matriz1.append(fila1)
		matriz2.append(fila2)

	for k in range(len(matriz1)):
		for l in range(len(matriz1[k])):
			if matriz1[k][l] > mayor1:
				mayor1 = matriz1[k][l]

			if matriz2[k][l] > mayor2:
				mayor2 = matriz2[k][l]

	if mayor1 == mayor2:
		print "El numero mayor de la primer matriz si esta en la segunda matriz."

	else:
		print "El numero mayor de la primer matriz no esta en la segunda matriz."

except ValueError:
	print "Error..."