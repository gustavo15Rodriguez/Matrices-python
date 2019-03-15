#-*-coding:utf-8-*-

'''29. Leer una matriz 4x6 entera y determinar si alguno de sus números está repetido al menos
3 veces.'''

if __name__ == '__main__':
	matriz = []
	
try:
	for i in range(4):
		fila = []
		for j in range(6):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)

		matriz.append(fila)
	
	vec_repetidos = []
	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
		    cont = 1
		    for m in range(len(matriz)):
		        for n in range(len(matriz[m])):
		            if k != m or l != n:
		                if matriz[k][l] == matriz[m][n] and matriz[k][l] != "hola":
		                    cont+=1
		                    matriz[m][n] = "hola"
		                    
		    if cont >= 3:
		        vec_repetidos.append([matriz[k][l], cont])
		        
		    matriz[k][l] = "hola"
		    
	if len(vec_repetidos) > 0:
	    print vec_repetidos
	    
	else:
	    print "No hay numeros repetidos tres veces o mas."
			

except ValueError:
	print "Error..."
