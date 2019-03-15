#-*-coding:utf-8-*-

'''28. Leer una matriz 4x6 entera y determinar en qué posiciones se encuentran los números
cuyo penúltimo dígito sea el 5. '''

if __name__ == '__main__':
	matriz = []
	digito = []
	pos = []
	p = 0
	
try:
	for i in range(4):
		fila = []
		for j in range(6):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)

		matriz.append(fila)

	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			num = matriz[k][l]
			num1 = matriz[k][l]
			while num > 0:
				num = num//10
				dig = num%10
				if dig==5:
					digito.append(num1)
				num = 0

	for g in range(len(matriz)):
		for s in range(len(matriz[g])):
			num = matriz[g][s]

			for r in range(len(digito)):
				if num==digito[r]:
					p = g, s
					pos.append(p)

	print matriz
	print "Las posiciones de los numeros con penultimo numero en 5 son:", pos

except ValueError:
	print "Error..."
