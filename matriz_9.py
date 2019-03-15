#-*-coding:utf-8-*-

'''9. Leer una matriz 3x4 entera y determinar cuántos de los números almacenados son primos
y terminan en 3.'''

if __name__ == '__main__':
	matriz = []
	cont2 = 0

try:
	primo = []
	for i in range(3):
		fila = []
		for j in range(4):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)

		matriz.append(fila)

	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			num = matriz[k][l]
			cont = 0
			for m in range(1, num+1):
				if num%m==0:
					cont += 1

			if cont == 2:
				primo.append(num)


	for n in range(len(primo)):
		var = primo[n]
		if var%10==3:
			cont2+=1
			
	print matriz	
	print primo
	print "Hay %d numeros que terminan en 3."%cont2

except ValueError:
	print "Error..."