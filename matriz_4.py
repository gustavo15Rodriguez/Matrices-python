#-*-coding:utf-8-*-

'''4. Leer una matriz 4x3 entera y determinar en qué posiciones exactas se encuentran los
números primos. '''

if __name__ == '__main__':
	matriz = []
	pos = 0
	posiciones = []

try:
	for i in range(4):
		fila = []
		for j in range(3):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)

		matriz.append(fila)

	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			num = matriz[k][l]
			cont = 0
			for m in range(1, num+1):
				if num%m==0:
					cont+=1

			if cont == 2:
				pos = k, l
				posiciones.append(pos)

	if cont == 2:
		print "Las posiciones exactas donde se encuentranlos numeros primos es ",posiciones

	else: 
		print "No hay numeros primos"

except ValueError:
	print "Error..."
