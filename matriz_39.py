#-*-coding:utf-8-*-

'''39. Leer dos matrices 4x6 enteras y determinar si el promedio de las “esquinas” de una
matriz es igual al promedio de las “esquinas” de la otra matriz.'''

if __name__ == '__main__':
	matriz1 = []
	matriz2 = []

try:
	for i in range(4):
		fila1 = []
		fila2 = []
		for j in range(6):
			num1 = int(raw_input("Digite el numero para la primer matriz: "))
			num2 = int(raw_input("Digite el numero para la segunda matriz: "))
			fila1.append(num1)
			fila2.append(num2)

		matriz1.append(fila1)
		matriz2.append(fila2)

	for k in range(len(matriz1)):
	    for l in range(len(matriz2[k])):
	        num1 = matriz1[k][l]
	        num2 = matriz2[k][l]
	
	suma1 = matriz1[0][0]
	suma1 += matriz1[0][len(matriz1[0])-1]
	suma1 += matriz1[len(matriz1)-1][0]
	suma1 += matriz1[len(matriz1)-1][len(matriz1[0])-1]
	
	suma2 = matriz2[0][0]
	suma2 += matriz2[0][len(matriz2[0])-1]
	suma2 += matriz2[len(matriz2)-1][0]
	suma2 += matriz2[len(matriz2)-1][len(matriz2[0])-1]
	
	print "Promedio1 ",(suma1/4)
	print "Promedio2 ",(suma2/4)
	
	if (suma1/4) == (suma2/4):
	    print "El promedio de las esquinas de ambas matrices son iguales."
	    
	else:
	    print "El promedio de las esquinas de ambas matrices son diferentes."
			
except ValueError:
	print "Error..."
