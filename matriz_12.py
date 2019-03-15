#-*-coding:utf-8-*-

'''12. Leer una matriz 5x5 entera y determinar en qué fila está el mayor número terminado en
6.'''

if __name__ == '__main__':
	matriz = []
	primo = []
	si = []
	mayor = 0
	pos = []

try:
	for i in range(5):
		fila = []
		for j in range(5):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)

		matriz.append(fila)

	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			num = matriz[k][l]
			if num %10 == 6:
				si.append(num)

	for g in range(len(si)):
		if si[g] > mayor:
			mayor = si[g]

	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			num = matriz[k][l]
			if mayor == num:
				pos.append(k)

	print matriz
	print mayor
	print "El numero mayor que termina en 6 esta en la fila", pos

except ValueError:
	print "Error..."
