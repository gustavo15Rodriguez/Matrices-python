#-*-coding:utf-8-*-

'''27. Leer dos matrices 4x5 enteras y determinar si la cantidad de números primos
almacenados en una matriz es igual a la cantidad de números primos almacenados en la otra
matriz. '''
	
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

	cant1 = 0
	cant2 = 0

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
				cant1+=1

			for s in range(1, num2+1):
				if num2%s == 0:
					cont2+=1

			if cont2 == 2:
				primos2.append(num2)
				cant2+=1

	if cant1 == cant2:
		print primos1
		print primos2
		print "La cantidad de numeros primos de la primer matriz si es igual a la cantidad de numeros primos de la segunda matriz."

	else:
		print primos1
		print primos2
		print "La cantidad de numeros primos de la primer matriz no es igual a la cantidad de numeros primos de la segunda matriz."

			
except ValueError:
	print "Error..."