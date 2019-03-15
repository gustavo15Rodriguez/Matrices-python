#-*-coding:utf-8-*-

'''46. Leer dos matrices 5x5 enteras y determinar si el promedio entero de los números
menores cada fila de una matriz corresponde a alguno de los datos almacenados en las
“esquinas” de la otra matriz.'''

if __name__ == '__main__':
	matriz1 = []
	matriz2 = []
	m = []
	suma = 0
	cont = 0
	pprom = 0

try:
	for i in range(5):
		fila1 = []
		for j in range(5):
			num1 = int(raw_input("Digite el numero para la primer matriz: "))
			fila1.append(num1)

		matriz1.append(fila1)

	for k in range(len(matriz1)):
	    menor = matriz1[0]
	    for l in range(len(matriz1[k])):
	        if matriz1[k][l]<menor:
	            menor = matriz1[k][l]
	    suma+=menor
	    cont+=1
	    prom = suma // cont
	    m.append(menor)
	    
	print "\n"
	
	for g in range(5):
		fila2 = []
		for s in range(5):
			num2 = int(raw_input("Digite el numero para la segunda matriz: "))
			fila2.append(num2)

		matriz2.append(fila2)
	print "\n"
	cont = 0	
	suma1 = matriz2[0][0]
	print "La primer esquina de la segunda matriz es %d"%suma1
	if suma1==prom:
	    cont+=1
	suma1 = matriz2[0][len(matriz2[0])-1]
	print "La segunda esquina de la segunda matriz es %d"%suma1
	if suma1==prom:
	    cont+=1
	suma1 = matriz2[len(matriz2)-1][0]
	print "La tercer esquina de la segunda matriz es %d"%suma1
	if suma1==prom:
	    cont+=1
	suma1 = matriz2[len(matriz2)-1][len(matriz2[0])-1]
	print "La cuarta esquina de la segunda matriz es %d"%suma1
	if suma1==prom:
	    cont+=1
	print "\n"
	if cont>0:
	    print "El promedio de los numeros menores por fila es %d"%prom
	    print "El promedio de los numeros menores de la primer matriz por fila si se encuentra en una de las esquinas de la segunda matriz."
	    
	else:
	    print "El promedio de los numeros menores por fila es %d"%prom
	    print "El promedio de los numeros menores de la primer matriz por fila no se encuentra en una de las esquinas de la segunda matriz."
	    
except ValueError:
    print "Error..."
