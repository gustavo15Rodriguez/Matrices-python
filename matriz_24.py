#-*-coding:utf-8-*-

'''24. Leer dos matrices 4x5 enteras y determinar si el mayor número primo de una de las
matrices también se encuentra en la otra matriz.'''

if __name__ == '__main__':
	matriz1 = []
	matriz2 = []
	primos1 = []
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

	for k in range(len(matriz1)):
		for l in range(len(matriz1[k])):
			num1 = matriz1[k][l]
			cont1 = 0

			for g in range(1, num1+1):
				if num1%g == 0:
					cont1+=1

			if cont1 == 2:
				primos1.append(num1)

	mayor1 = 0
	for a in range(len(primos1)):
		if primos1[a] > mayor1:
			mayor1 = primos1[a]

	cont2 = 0
	for g in range(len(matriz2)):
		for s in range(len(matriz2[g])):
			if mayor1 == matriz2[g][s]:
				cont2+=1

	if cont2 > 0:
		print "El numero primo mayor de la primer matriz tambien se encuentra en la segunda matriz."

	else:
		print "El numero primo mayor de la primer matriz no se encuentra en la segunda matriz."

except ValueError:
	print "Error..."