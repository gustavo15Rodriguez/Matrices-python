#-*-coding:utf-8-*-

'''2. Leer una matriz 4x4 entera y determinar cuántas veces se repita en ella 
el número mayor.'''

if __name__ == '__main__':
	matriz = []
	mayor = 0
	cont = 0

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

	for k in range(len(matriz)):
		for l in range(len(matriz)):
			num = matriz[k][l]
			if mayor == num:
				cont+=1

	print "El numero mayor se repite %d veces en la matriz anterior."%cont

except ValueError:
	print "Error..."