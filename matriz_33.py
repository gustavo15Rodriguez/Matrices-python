#-*-coding:utf-8-*-
'''Leer una matriz 4x6 entera y determinar en qué posiciones están los menores pares por fila'''
matriz = []
try:
	listanumero = []
	for i in range(4):
		fila = []
		for j in range(6):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)
		matriz.append(fila)

	print matriz
	
	for t in range(len(matriz)):
		menor = matriz[0]
		for l in range(len(matriz[t])):
			numero = matriz[t][l]
			if numero % 2 == 0:
				numero = matriz[t][l]
				if numero < menor:
					menor = numero
					fila = t
					columna = l

		print "El numero par menor de la fila %d es %d"%(t, menor)














except ValueError:
	print "Error..."
