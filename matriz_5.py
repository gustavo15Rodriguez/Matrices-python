#-*-coding:utf-8-*-

'''5. Leer una matriz 4x3 entera, calcular la suma de los elementos de cada fila y determinar
cuál es la fila que tiene la mayor suma.'''

if __name__ == '__main__':
	matriz = []
	mayor = 0
	pos = 0

try:
	for i in range(4):
		fila = []
		for j in range(3):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)

		matriz.append(fila)

	
	sumas = []
	for k in range(len(matriz)):
		suma = 0
		for l in range(len(matriz[k])):
			num = matriz[k][l]
			suma+=num
		
		sumas.append(suma)

	for m in range(len(sumas)):
		if sumas[m] > mayor:
			mayor = sumas[m]
			pos = m

	print matriz
	print "La suma de cada fila es: ", sumas
	print "La fila que tiene la mayor suma es: %d"%pos


except ValueError:
	print "Error..."