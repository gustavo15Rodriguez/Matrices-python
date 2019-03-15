#-*-coding:utf-8-*-

'''48. Leer dos matrices 5x5 entera y determinar si el promedio de los mayores elementos que
pertenecen a la serie de Fibonacci de cada fila de una matriz es igual al promedio de los
mayores elementos que pertenecen a la serie de Fibonacci de cada fila de la otra matriz.'''

if __name__ == '__main__':
	matriz1 = []
	matriz2 = []
	

try:
	for i in range(5):
		fila1 = []
		fila2 = []
		for j in range(5):
			num1 = int(raw_input("Digite el numero para la primer matriz: "))
			num2 = int(raw_input("Digite el numero para la segunda matriz: "))
			fila1.append(num1)
			fila2.append(num2)

		matriz1.append(fila1)
		matriz2.append(fila2)
		numero = 1
		ultimo = 0
		penultimo = 0
	
	fib = []	    
	for g in range(101):
		penultimo = ultimo
		ultimo = numero
		numero = penultimo+ultimo
		fib.append(numero)
	
	
	m = []
	for k in range(len(matriz1)):
	    mayor = 0
	    for l in range(len(matriz1[k])):
	        num = matriz1[k][l]
	        for s in range(len(fib)):
	            num1 = fib[s]
	            
	            if num == num1:
	                if num>mayor:
	                    mayor = num
	    
	    m.append(mayor)
	    
	m1 = []
	for g in range(len(matriz2)):
	    mayor1 = 0
	    for s in range(len(matriz2[g])):
	        num2 = matriz2[g][s]
	        for y in range(len(fib)):
	            num3 = fib[y]
	            
	            if num2 == num3:
	                if num2>mayor1:
	                    mayor1 = num2
	    
	    m1.append(mayor1)
	    
	suma = 0
	cont = 0
	prom = 0
	
	for a in range(len(m)):
	    suma+=m[a]
	    cont+=1
	    prom = suma//cont
	    
	suma1 = 0
	cont1 = 0
	prom1 = 0
	
	for b in range(len(m1)):
	    suma1+=m1[b]
	    cont1+=1
	    prom1 = suma1//cont1
	    
	print "La primer matriz es: ",matriz1
	print "La segunda matriz es: ",matriz2
	print "\n"
	
	print "Mayores de todas las filas de la primer matriz que pertenecen a la serie fibonacci", m
	print "Mayores de todas las filas de la segunda matriz que pertenecen a la serie fibonacci", m1
	print "\n"
	
	print "Promedio de los mayores elementos de la serie fibonacci en la matriz 1: %d"%prom
	print "Promedio de los mayores elementos de la serie fibonacci en la matriz 2: %d"%prom1
	print "\n"
	
	if prom == prom1:
	    print "Los promedios de ambas matrices son iguales."
	    
	else:
	    print "Los promedios de ambas matrices son direfentes."

except ValueError:
    print "Error..."
