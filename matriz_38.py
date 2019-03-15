#-*-coding:utf-8-*-

'''38. Leer dos matrices 4x6 enteras y determinar si el mayor número primo de una matriz está
repetido en la otra matriz. '''

if __name__ == '__main__':
	matriz1 = []
	matriz2 = []
	primos1 = []
	primos2 = []
	
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
			cont1 = 0
			for z in range(1, num1+1):
				if num1%z==0:
					cont1+=1

			if cont1 == 2:
				primos1.append(num1)

	for g in range(len(matriz2)):
		for s in range(len(matriz2[g])):
			num2 = matriz2[g][s]
			cont2 = 0
			for q in range(1, num2+1):
				if num2%q==0:
					cont2+=1

			if cont2 == 2:
				primos2.append(num2)

	mayor = 0
	for a in range(len(primos1)):
		if primos1[a]>mayor:
			mayor = primos1[a]

	cont = 0
	for b in range(len(primos2)):
		if mayor == primos2[b]:
			cont+=1

	if cont>0:
		print primos1
		print primos2
		print "El numero primo mayor de la primer matriz si esta repetido en la segunda matriz."

	else:
		print primos1
		print primos2
		print "El numero primo mayor de la primer matriz no esta repetido en la segunda matriz."

except ValueError:
	print "Error..."
