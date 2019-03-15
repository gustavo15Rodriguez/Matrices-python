#-*-coding:utf-8-*-

'''26. Leer dos matrices 4x5 enteras y determinar si la cantidad de números pares almacenados
en una matriz es igual a la cantidad de números pares almacenados en la otra matriz.'''

if __name__ == '__main__':
	matriz1 = []
	matriz2 = []
	
try:
	for i in range(4):
		fila1 = []
		fila2 = []
		for j in range(5):
			num1 = int(raw_input("Digite el numero para la primer matriz: "))
			num2 = int(raw_input("Digite el numero para la segunda matriz: "))
			fila1.append(num1)
			fila2.append(num2)

		matriz1.append(fila1)
		matriz2.append(fila2)


	cont1 = 0
	cont2 = 0
	for k in range(len(matriz1)):
		for l in range(len(matriz1[k])):
			num1 = matriz1[k][l]
			num2 =matriz2[k][l]

			if num1%2==0:
				cont1+=1

			if num2%2 == 0:
				cont2+=1

	if cont1 == cont2:
		print "La cantidad de elementos pares de la primer matriz es igual a la cantidad de elementos pares la segunda matriz."

	else:
		print "La cantidad de elementos pares de la primer matriz no es igual a la cantidad de elementos pares de la segunda matriz."
			
except ValueError:
	print "Error..."