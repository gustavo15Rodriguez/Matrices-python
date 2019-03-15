#-*-coding:utf-8-*-

'''8. Leer una matriz 4x4 entera y determinar cuántos enteros terminados en 0 hay
almacenados en ella.'''

if __name__ == '__main__':
	matriz = []
	cont = 0

try:
	for i in range(4):
		fila = []
		for j in range(4):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)

		matriz.append(fila)

	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			num = matriz[k][l]
			if num%10==0:
				cont+=1

	if cont > 0:
		print matriz
		print "Hay %d numeros enteros que terminan en 0."%cont

	else:
		print matriz
		print "No hay numeros terminados en 0."



except ValueError:
	print "Error..."