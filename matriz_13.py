#-*-coding:utf-8-*-

'''13. Leer una matriz 5x3 entera y determinar en qué columna está el mayor número que
comienza con el dígito 4. '''

if __name__ == '__main__':
	matriz = []
	primo = []
	pos = 0
	mayor = 0
	inicial = []

try:
	for i in range(5):
		fila = []
		for j in range(3):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)

		matriz.append(fila)

	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			num = matriz[k][l]
			numero = matriz[k][l]
			while num > 0:
				dig = num %10
				if num == 4:
					inicial.append(numero)

				num = num //10

	for g in range(len(inicial)):
		if inicial[g] > mayor:
			mayor = inicial[g]

	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			num = matriz[k][l]
			if num == mayor:
				pos = l

	print matriz
	print mayor
	print "El numero mayor iniciado en cuatro esta en la columna %d."%pos

except ValueError:
	print "Error..."