#-*-coding:utf-8-*-

'''22. Leer dos matrices 4x5 enteras y determinar si el número mayor almacenado en la
primera está en la segunda.'''

if __name__ == '__main__':
	matriz_1 = []
	matriz_2 = []
	mayor1 = 0
	
try:
	for i in range(4):
		fila_1 = []
		fila_2 = []
		for j in range(5):
			num1 = int(raw_input("Digite el numero para la primer matriz: "))
			num2 = int(raw_input("Digite el numero para la segunda matriz: "))
			fila_1.append(num1)
			fila_2.append(num2)

		matriz_1.append(fila_1)
		matriz_2.append(fila_2)

	for j in range(len(matriz_1)):
		for k in range(len(matriz_1[j])):
			if matriz_1[j][k] > mayor1:
				mayor1 = matriz_1[j][k]

	cont = 0
	for j in range(len(matriz_1)):
		for k in range(len(matriz_1[j])):
			if mayor1 == matriz_2[j][k]:
				cont+=1

	if cont > 0:
		print "El numero mayor de la primer matriz si esta en la matriz 2."

	else:
		print "El numero mayor de la primer matriz no esta en la matriz 2."

except ValueError:
	print "Error..."