#-*-coding:utf-8-*-

'''11. Leer una matriz 5x3 entera y determinar en qué columna está el menor número par.'''

if __name__ == '__main__':
	matriz = []
	primo = []
	pos = []
	pares = []
	

try:
	for i in range(5):
		fila = []
		for j in range(3):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)

		matriz.append(fila)
	menor = matriz[0]
	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			num = matriz[k][l]
			if num%2==0:
				pares.append(num)

	for m in range(len(pares)):
			if pares[m] < menor:
				menor = pares[m]
	
	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			num = matriz[k][l]
			if menor == num:
				pos.append(l)

	print matriz
	print pares
	print menor 
	print "La columna en la cual se encuentra el numero par menor es: ",pos

except ValueError:
	print "Error..."
