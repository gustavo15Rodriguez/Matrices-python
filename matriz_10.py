#-*-coding:utf-8-*-

'''10. Leer una matriz 5x3 entera y determinar en qué fila está el mayor número primo. '''

if __name__ == '__main__':
	matriz = []
	primo = []
	pos = []
	mayor = 0

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
			cont = 0
			for m in range(1, num+1):
				if num%m==0:
					cont += 1

			if cont ==2:
				primo.append(num)

	for n in range(len(primo)):
		if primo[n] >= mayor:
			mayor = primo[n]
			
	for g in range(len(matriz)):
		for s in range(len(matriz[g])):
			num = matriz[g][s]
			if mayor == num:
				pos.append(g)
				
	print matriz
	print primo
	print mayor
	print "El numero primo mayor se encuentra en la fila", pos

except ValueError:
	print "Error..."
