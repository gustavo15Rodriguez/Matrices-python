#-*-coding:utf-8-*-

'''3. Leer una matriz 3x4 entera y determinar en qué posiciones exactas se encuentran los
números pares.'''

if __name__ == '__main__':
	matriz = []
	mayor = 0

try:
	for i in range(3):
		fila = []
		for j in range(4):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)

		matriz.append(fila)

	posiciones = []
	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			num = matriz[k][l]
			if num%2==0:
				pos = k, l
				posiciones.append(pos)

	print "La matriz es:", matriz
	print "Las posiciones excatas donde se encuentran los numeros pares es ",posiciones

except ValueError:
	print "Error..."