#-*-coding:utf-8-*-

'''20. Leer dos matrices 4x5 entera, luego leer un entero y determinar si cada uno de los
elementos de una de las matrices es igual a cada uno de los elementos de la otra matriz
multiplicado por el entero leído.'''

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

	num3 = int(raw_input("Digite el numero a evaluar: "))

	cont = 0
	for j in range(len(matriz1)):
		for k in range(len(matriz1[j])):
			if matriz1[j][k]*num3 != matriz2[j][k]*num3:
				cont+=1

	if cont == 0:
		print "La multiplicacion realizada por el numero de cada matriz si es igual a los elementos de la otra matriz."

	else:
		print "La multiplicacion realizada por el numero de cada matriz no es igual a los elementos de la otra matriz."

except ValueError:
	print "Error..."