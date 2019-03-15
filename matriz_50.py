#-*-coding:utf-8-*-

'''50. Leer una matriz 5x5 y determinar si el promedio de los elementos que se encuentran en
su diagonal está almacenado en ella. Mostrar en pantalla en qué posiciones exactas se
encuentra dicho dato.'''

if __name__ == '__main__':
	matriz1 = []
	pos = 0
	p = []

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
	    
	for k in range(len(diagonal1)):
	    suma1+=diagonal1[k]
	    cont1+= 1
	
	prom1 = suma1//cont1
	
	cont = 0
	for g in range(len(matriz1)):
	    for s in range(len(matriz1)):
	        if prom1 == matriz1[g][s]:
	            cont+=1
	            pos = g, s
	            p.append(pos)
	        
	if cont>0:
	    print "La matriz es:", matriz1
	    print "El promedio de la diagonal de la matriz es: %d"%prom1
	    print "El promedio de la diagonal de la matriz si se encuentra dentro de la matriz y su posicion exacta es: ",p
	    
	else:
	    print "La matriz es:", matriz1
	    print "El promedio de la diagonal de la matriz es: %d"%prom1
	    print "El promedio de la diagonal de la matriz anterior no se encuantra dentro de la misma matriz."

except ValueError:
    print "Error..."
