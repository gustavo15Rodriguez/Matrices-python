#-*-coding:utf-8-*-

'''30. Leer una matriz 4x6 entera y determinar cuántas veces está en ella el número menor. '''

if __name__ == '__main__':
	matriz = []
	
try:
	for i in range(4):
		fila = []
		for j in range(6):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)

		matriz.append(fila)

	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			num = matriz[k][l]

	menor = matriz[k][l]
	for g in range(len(matriz)):
		for s in range(len(matriz[k])):
			if matriz[g][s] < menor:
				menor = matriz[g][s]
				
	cont = 0
	for r in range(len(matriz)):
		for z in range(len(matriz[r])):
			if menor == matriz[r][z]:
				cont+=1

	if cont > 1:
		print "El numero menor se repite %d veces en la matriz anterior."%cont

	else:
		print "El numero menor no esta repetido en la matriz anterior."
			
except ValueError:
	print "Error..."
