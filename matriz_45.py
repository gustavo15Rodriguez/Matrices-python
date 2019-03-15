#-*-coding:utf-8-*-

'''45. Leer dos matrices 5x5 enteras y determinar si el promedio entero de los números
mayores de cada fila de una matriz es igual al promedio de los números mayores de cada fila
de la otra matriz. '''

if __name__ == '__main__':
	matriz1 = []
	matriz2 = []
	mayores1 = []
	mayores2 = []
	suma1 = 0
	cont1 = 0
	prom1 = 0
	suma2 = 0
	cont2 = 0
	PROM2 = 0
	
try:
	for i in range(5):
		fila1 = []
		mayor1 = 0
		for j in range(2):
			num1 = int(raw_input("Digite un numero para la primer matriz: "))
			fila1.append(num1)
			if mayor1<num1:
			    mayor1 = num1
		suma1+=mayor1
		cont1+=1
		prom1 = suma1//cont1    
		mayores1.append(mayor1)
			    
		matriz1.append(fila1)
	
	print "\n"
		
	for g in range(5):
		fila2 = []
		mayor2 = 0
		for s in range(2):
			num2 = int(raw_input("Digite un numero para la segunda matriz: "))
			fila2.append(num2)
			if mayor2<num2:
			    mayor2 = num2
		suma2+=mayor2
		cont2+=1
		prom2 = suma2//cont2    
		mayores2.append(mayor2)
			    
		matriz2.append(fila2)
		
	if prom1 == prom2:
	    print "Los numeros mayores de cada fila de la primer matriz son: ",mayores1
	    print "El promedio de los numeros mayores de cada fila de la primer matriz es: %d"%prom1
	    print "\n"
	    print "Los numeros mayores de cada fila de la segunda matriz son: ",mayores2
	    print "El promedio de los numeros mayores de cada fila de la segunda matriz es: %d"%prom2
	    print "El promedio de los numeros mayores de cada fila en ambas matrices es igual."
	    
	else:
	    print "Los numeros mayores de cada fila de la primer matriz son: ",mayores1
	    print "El promedio de los numeros mayores de cada fila de la primer matriz es: %d"%prom1
	    print "\n"
	    print "Los numeros mayores de cada fila de la segunda matriz son: ",mayores2
	    print "El promedio de los numeros mayores de cada fila de la segunda matriz es: %d"%prom2
	    print "El promedio de los numeros mayores de cada fila en mabas matrices no es igual."

	
			
except ValueError:
	print "Error..." 
