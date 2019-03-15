#-*-coding:utf-8-*-

'''37. Leer dos matrices 4x6 enteras y determinar si el número mayor de una matriz se
encuentra en la misma posición exacta en la otra matriz. '''

if __name__ == '__main__':
	matriz1 = []
	matriz2 = []
	pos1 = 0
	pos2 = 0
	
try:
	for i in range(4):
		fila1 = []
		fila2 = []
		for j in range(6):
			num1 = int(raw_input("Digite un numero para la primer matriz: "))
			num2 = int(raw_input("Digite un numero para la segunda matriz: "))
			fila1.append(num1)
			fila2.append(num2)

		matriz1.append(fila1)
		matriz2.append(fila2)

	mayor1 = 0
	mayor2 = 0
	for k in range(len(matriz2)):
		for l in range(len(matriz2[k])):
			num1 = matriz1[k][l]
			num2 = matriz2[k][l]
			if num1>mayor1:
				mayor1 = num1
				pos1 = k, l

			if num2>mayor2:
				mayor2 = num2
				pos2 = k, l

	if pos1 == pos2:
		print "La matriz 1 es:", matriz1
		print "La matriz 2 es:", matriz2
		print "La posicion exacta del numero mayor de la primer matriz es:", pos1
		print "La posicion exacta del numero mayor de la segunda matriz es:", pos2
		print "El numero mayor de ambas matrices se encuentra en la misma posicion."

	else:
		print "La matriz 1 es:", matriz1
		print "La matriz 2 es:", matriz2
		print "La posicion exacta del numero mayor de la primer matriz es:", pos1
		print "La posicion exacta del numero mayor de la segunda matriz es:", pos2
		print "El numero mayor de ambas matrices se encuentra en posiciones diferentes."

except ValueError:
	print "Error..."