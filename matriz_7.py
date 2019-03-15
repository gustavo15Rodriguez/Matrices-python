#-*-coding:utf-8-*-

'''7. Leer una matriz 4x4 entera y determinar en qué posiciones están los enteros terminados
en 0. '''

if __name__ == '__main__':
	matriz = []
	posiciones = []
	pos = 0
	cont = 0

try:
	for i in range(4):
		fila = []
		for j in range(4):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)

		matriz.append(fila)

	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			num = matriz[k][l]
			if num%10==0:
				pos = k, l
				cont+=1
				posiciones.append(pos)
	if cont > 0:
		print matriz
		print "Los numeros de la matriz anterior que terminan en 10 son", posiciones

	else:
		print matriz
		print "No hay numeros que terminen en 0."

except ValueError:
	print "Error..."