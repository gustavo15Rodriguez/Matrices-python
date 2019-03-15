#-*-coding:utf-8-*-

'''40. Leer dos matrices 5x5 enteras y determinar si el promedio entero de los elementos de la
diagonal de una matriz es igual al promedio de los elementos de la diagonal de la otra matriz.'''

if __name__ == '__main__':
	matriz1 = []
	matriz2 = []

try:
	for i in range(5):
		fila1 = []
		for j in range(5):
			num1 = int(raw_input("Digite el numero para la primer matriz: "))
			fila1.append(num1)

		matriz1.append(fila1)
		
	diagonal1 = []
	suma1 = 0
	cont1 = 0
	prom1 = 0
	for i in range(len(matriz1)):
	    diagonal1.append(matriz1[i][i])
	    
	for g in range(len(diagonal1)):
	    suma1+=diagonal1[g]
	    cont1+= 1
	
	prom1 = suma1//cont1
	
	print "\n"
	for l in range(5):
	    fila2 = []
	    for m in range(5):
	        num2 = int(raw_input("Digite el numero para la segunda matriz: "))
	        fila2.append(num2)
	    
	    matriz2.append(fila2)
		
	diagonal2 = []
	suma2 = 0
	cont2 = 0
	prom2 = 0
	for l in range(len(matriz2)):
	    diagonal2.append(matriz2[l][l])
	    
	for s in range(len(diagonal2)):
	    suma2+=diagonal2[s]
	    cont2+= 1
	
	prom2 = suma2//cont2
	
	print "La diagonal de la primer matriz es: ",diagonal1
	print "El promedio de la diagonal de la primer matriz es: %d"%prom1
	print "\n"
	print "La diagonal de la segunda matriz es: ",diagonal2
	print "El promedio de la diagonal de la segunda matriz es: %d"%prom2
	
	if prom1 == prom2:
	    print "El promedio de la diagonal de ambas matrices es igual."
	    
	else:
	    print "El promedio de la diagonal de ambas matrices es diferente."
	    
except ValueError:
	print "Error..."
