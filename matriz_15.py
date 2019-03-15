#-*-coding:utf-8-*-

'''15. Leer una matriz 5x4 entera y determinar cuántos números almacenados en ella terminan
en 34.'''

if __name__ == '__main__':
	matriz = []
	
try:
	for i in range(5):
		fila = []
		for j in range(4):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)

		matriz.append(fila)

	cont = 0
	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			num = matriz[k][l]
			if num%100==34:
				cont+=1

	print "Hay %d numeros que terminan en 34."%cont

except ValueError:
	print "Error..."