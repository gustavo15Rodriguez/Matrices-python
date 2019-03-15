#-*-coding:utf-8-*-

'''19. Leer dos matrices 4x5 entera y determinar si sus contenidos son exactamente iguales. '''

if __name__ == '__main__':
	matriz_1 = []
	matriz_2 = []
	
try:
	for i in range(4):
		fila_1 = []
		fila_2 = []
		for j in range(5):
			num1 = int(raw_input("Digite el numero para la primer matriz: "))
			num2 = int(raw_input("Digite el numero para la segunda matriz: "))
			fila_1.append(num1)
			fila_2.append(num2)
			

		matriz_1.append(fila_1)
		matriz_2.append(fila_2)

	cont = 0
	for j in range(len(matriz_1)):
		for k in range(len(matriz_1[j])):
			if matriz_1[j][k] != matriz_2[j][k]:
				cont+=1

	if cont==0:
		print "Todos los elementos son iguales."

	else:
		print "Los elementos de las matrices son diferentes."
		
except ValueError:
	print "Error..."