#-*-coding:utf-8-*-

'''31. Leer una matriz 4x6 entera y determinar en qué posiciones están los menores por fila.'''

if __name__ == '__main__':
	matriz = []
	pos = 0
	
try:
	for i in range(4):
		fila = []
		for j in range(6):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)

		matriz.append(fila)

	print matriz

	for k in range(len(matriz)):
		menor = matriz[0]
		for l in range(len(matriz[k])):
			if matriz[k][l]<menor:
				menor = matriz[k][l]
				pos = k
 
		print "El menor de la fila %d es %d "%(pos, menor)


			
except ValueError:
	print "Error..."
