#-*-coding:utf-8-*-

'''36. Leer dos matrices 4x6 enteras y determinar si el mayor número almacenado en una de
ellas que pertenezca a la Serie de Fibonacci es igual al mayor número almacenado en la otra
matriz que pertenezca a la Serie de Fibonacci.'''

if __name__ == '__main__':
	matriz1 = []
	matriz2 = []
	lista1 = []
	lista2 = []
	
try:
	for i in range(4):
		fila1 = []
		fila2 = []
		for j in range(6):
			num1 = int(raw_input("Digite un numero para la primer matriz: "))
			num2 = int(raw_input("Digite un numero para la segunda matriz: "))
			fila1.append(num1)
			fila2.append(num2)

		matriz1.append(fila1)
		matriz2.append(fila2)

	for k in range(len(matriz1)):
		for l in range(len(matriz1[k])):
			num1 = matriz1[k][l]
			num2 = matriz2[k][l]

			numero = 1
			ultimo = 0
			penultimo = 0

			for g in range(100):
				penultimo = ultimo
				ultimo = numero
				numero = penultimo+ultimo
				if num1 == numero:
					lista1.append(numero)

				if num2 == numero:
					lista2.append(numero)

	mayor1 = 0
	for g in range(len(lista1)):
		if lista1[g]>mayor1:
			mayor1 = lista1[g]
	
	mayor2 = 0
	for s in range(len(lista2)):
		if lista2[s]>mayor2:
			mayor2 = lista2[s]

	if mayor1 == mayor2:
		print "Ambos datos mayores pertenecientes a la serie Fibonacci en ambas matrices son iguales."

	else:
		print "Los datos mayores pertenecientes a la serie Fibonacci en ambas matrices son diferentes."
			
except ValueError:
	print "Error..."