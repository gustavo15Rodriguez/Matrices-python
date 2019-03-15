#-*-coding:utf-8-*-

'''6. Leer una matriz 4x4 entera y calcular el promedio de los números mayores de cada fila.'''

if __name__ == '__main__':
	matriz = []
	suma = 0
	prom = 0
	cont = 0
	

try:
	for i in range(4):
		fila = []
		for j in range(4):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)

		matriz.append(fila)

	for k in range(len(matriz)):
		mayor = 0
		for l in range(len(matriz[k])):
			num = matriz[k][l]
			if num > mayor:
				mayor = num

		suma+=mayor
		cont+=1
		prom = suma//cont

	print matriz
	print "La suma de los numeros mayores de cada fila es igual a: %d"%suma
	print "El promedio de los numeros mayores de cada fila es: %d"%prom
	
except ValueError:
	print "Error..."
