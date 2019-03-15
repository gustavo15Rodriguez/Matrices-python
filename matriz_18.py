#-*-coding:utf-8-*-

'''18. Leer una matriz 5x5 entera y determinar en qué posición exacta se encuentra el mayor
múltiplo de 8.'''

if __name__ == '__main__':
	matriz = []
	g = []
	pos = 0
	
	
try:
	for i in range(5):
		fila = []
		for j in range(4):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)

		matriz.append(fila)

	cont = 0
	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			num = matriz[k][l]
			if num%8==0:
				g.append(num)

	mayor = 0
	for s in range(len(g)):
		if g[s] > mayor:
			mayor= g[s]

	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			num = matriz[k][l]
			if mayor==num:
				pos = k,l

	print matriz
	print mayor
	print "El mayor multiplo de 8 estan en la fila y columna ",pos

except ValueError:
	print "Error..."