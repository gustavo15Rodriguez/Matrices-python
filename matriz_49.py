#-*-coding:utf-8-*-

'''49. Leer una matriz 3x3 entera y determinar si el promedio de todos los datos almacenados
en ella se encuentra también almacenado. '''

if __name__ == '__main__':
	matriz = []
	suma = 0
	cont = 0
	prom = 0
	
try:
	for i in range(3):
		fila = []
		for j in range(3):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)
			suma+=num
			cont+=1

		prom = suma//cont
		matriz.append(fila)

	cont2 = 0
	for k in range(len(matriz)):
		for l in range(len(matriz)):
			num = matriz[k][l]
			if prom ==num:
				cont2+=1

	if cont2>0:
		print matriz
		print "El promedio de los numeros que es %d, si esta almacenado en la lista."%prom

	else:
		print matriz
		print "El promedio de los numeros que es %d, no esta almacenado en la lista."%prom
	
except ValueError:
	print "Error..."