#-*-coding:utf-8-*-

'''17. Leer una matriz 5x4 entera y determinar cuántos múltiplos de 5 hay almacenados en ella.'''

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
			if num%5==0:
				cont+=1

	print "Hay %d numeros que terminan son multiplos de 5."%cont

except ValueError:
	print "Error..."