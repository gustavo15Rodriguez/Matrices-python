#-*-coding:utf-8-*-

'''21. Leer dos matrices 4x5 enteras y determinar cuántos datos tienen en común.'''

if __name__ == '__main__':
	matriz1 = []
	matriz2 = []
	repetidos = []
	cont = 0
	cont2 = 0
	
try:
	for i in range(4):
		fila1 = []
		for j in range(5):
			num1 = int(raw_input("Digite el numero para la primer matriz: "))
			fila1.append(num1)

		matriz1.append(fila1)

	print "\n"
	
	for i in range(4):
		fila2 = []
		for j in range(5):
			num2 = int(raw_input("Digite el numero para la segunda matriz: "))
			fila2.append(num2)

		matriz2.append(fila2)

	for k in range(len(matriz1)):
		for l in range(len(matriz1[k])):
		    cont = 0
		    for g in range(len(matriz2)):
		        for s in range(len(matriz2[g])):
		            if matriz1[k][l] == matriz2[g][s]:
		                cont+=1
                        
                if cont!=0:
                    cont2 = 0
                    for m in range(len(repetidos)):
                        if matriz1[k][l] == repetidos[m]:
                            cont2+=1
                            
                    if cont2 == 0:
                        repetidos.append(matriz1[k][l])
    
        if len(repetidos) != 0:
            print "Los elementos en comun de las dos matrices son ",repetidos
        
        else:
            print "Las dos matrices no tienen elementos en comun."

except ValueError:
	print "Error..."
