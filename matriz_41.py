#-*-coding:utf-8-*-

'''41. Leer dos matrices 5x5 enteras y determinar si el promedio entero de todos los elementos
que no están en la diagonal de una matriz es igual al promedio entero de todos los
elementos que no están en la diagonal de la otra matriz.'''

if __name__ == '__main__':
    matriz = []
    matriz2 = []

try:
	for i in range(5):
		fila1 = []
		for j in range(5):
			num1 = int(raw_input("Digite el numero para la primer matriz: "))
			fila1.append(num1)

		matriz.append(fila1)

	print "\n"
	
	for g in range(5):
		fila2 = []
		for s in range(5):
			num2 = int(raw_input("Digite el numero para la segunda matriz: "))
			fila2.append(num2)

		matriz2.append(fila2)
	
	suma=0
	cont=0
	promedio=0
	for e in range(len(matriz)):
	    for f in range(len(matriz)):
	        numero=matriz[e][f]
	        
	        if [e]!=[f]:
	            suma+=numero
	            cont+=1
	            promedio=suma//cont
	            
	suma2=0
	cont2=0
	promedio2=0
	for g in range(len(matriz2)):
	    for h in range(len(matriz2)):
	        numero2=matriz2[g][h]
	        
	        if [g]!=[h]:
	            suma2+=numero2
	            cont2+=1
	            promedio2=suma2//cont2
	
	print "Matriz 1: ",matriz
	print "Matriz 2: ",matriz2
	print "\n"
	print "Promedio de los elementos que no estan en la diagonal de la matriz 1: ",promedio
	print "Promedio de los elementos que no estan en la diagonal de la matriz 2: ",promedio2
	print "\n"
	
	if promedio==promedio2:
	    print "Ambos promedios son iguales"
	    
	else:
	    print "Los promedios son diferentes" 

except ValueError:
    print "Error..."
