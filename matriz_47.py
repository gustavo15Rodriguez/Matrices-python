#-*-coding:utf-8-*-

'''47. Leer dos matrices 5x5 enteras y determinar si el promedio de los mayores números
primos por cada fila de una matriz es igual al promedio de los mayores números primos por
cada columna de la otra matriz.'''

if __name__ == '__main__':
	matriz = []
	matriz2 = []
	suma = 0
	suma1 = 0

try:
	primos = []
	for i in range(5):
		fila = []
		for j in range(5):
			num = int(raw_input("Digite el numero para la primer matriz: "))
			fila.append(num)
		matriz.append(fila)

	print"\n"

	for a in range(len(matriz)):
		var = 0
		for b in range(len(matriz[a])):
			numero = matriz[a][b]
			con = 0

			for c in range(1,numero + 1):
				if numero % c == 0:
					con += 1

			if con == 2:
				numero = matriz[a][b]
				if numero > var:
					var = numero

		suma += var

	promedio = suma / 5

	for d in range(5):
		fila2 = []
		for e in range(5):
			num2 = int(raw_input("Digite el numero para la segunda matriz: "))
			fila2.append(num2)
		matriz2.append(fila2)

	for f in range(len(matriz2)):
		mayor = 0
		con3 = 0
		for g in range(len(matriz2[f])):
			numero2 = matriz2[g][f]
			con2 = 0

			for h in range(1,numero2 + 1):
				if numero2 % h == 0:
					con2 += 1

			if con2 == 2:
				numero2 = matriz2[g][f]
				if numero2 > mayor:
					mayor = numero2
					 
		suma1 += mayor
				
	promedio1 = suma1 / 5
	
	print "La primer matriz es: ",matriz
	print "La segunda matriz es: ",matriz2
	print "\n"
	print "El promedio de los mayores numeros primos de la primera matriz por cada fila es"
	print promedio
	print "El promedio de los numeros primos de la segunda matriz es"
	print promedio1
	if promedio == promedio1:
		print "Por lo tanto los promedios son iguales"
		
	else:
		print "Por lo tanto los promedios no son iguales"

except ValueError:
    print "Error..."

