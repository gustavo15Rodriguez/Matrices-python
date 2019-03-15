#-*-coding:utf-8-*-

'''1. Leer  una matriz 4x4 entera y determinar en qué fila y en qué columna se encuentra el
número mayor. '''

if __name__ == '__main__':
	matriz = []
	mayor = 0
	pos = 0

try:
	for i in range(4):
		fila = []
		for j in range(4):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)

		matriz.append(fila)

	for k in range(len(matriz)):
		for l in range(len(matriz)):
			num = matriz[k][l]
			if num > mayor:
				mayor = num
				pos = k, l

	print "La matriz es ",matriz
	print "El numero mayor es: %d"%mayor
	print "La fila y columna donde se encuentra el numero mayor es: ",pos

except ValueError:
	print "Error..."
