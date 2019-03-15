#-*-coding:utf-8-*-

'''25. Leer dos matrices 4x5 enteras y determinar si el mayor número primo de una de las
matrices es también el mayor número primo de la otra matriz.'''

if __name__ == '__main__':
	matriz1 = []
	matriz2 = []
	primos1 = []
	primos2 = []
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
			num2 = matriz2[k][l]
			cont1 = 0
			cont2 = 0
			for g in range(1, num1+1):
				if num1%g == 0:
					cont1+=1

			if cont1 == 2:
				primos1.append(num1)

			for s in range(1, num2+1):
				if num2%s == 0:
					cont2+=1

			if cont2 == 2:
				primos2.append(num2)

	mayor1 = 0
	for a in range(len(primos1)):
		if primos1[a] > mayor1:
			mayor1 = primos1[a]


	mayor2 = 0
	for b in range(len(primos2)):
		if primos2[b] > mayor2:
			mayor2 = primos2[b]

	if mayor1 == mayor2:
		print "El numero primo mayor de la primer matriz tambien es el numero primo mayor de la segunda matriz."

	else:
		print "El numero primo mayor de la primer matriz no es el numero primo mayor de la segunda matriz"
			
except ValueError:
	print "Error..."