#-*-coding:utf-8-*-

'''32. Leer una matriz 4x6 entera y determinar en qué posiciones están los menores primos por
fila.'''

if __name__ == '__main__':
	matriz = []
	primos = []	
	menor = 0
	pos = 0
	

try:
	for i in range(4):
		fila = []
		for j in range(6):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)

		matriz.append(fila)
		
	print "La matriz es: ",matriz
	print "\n"

	for k in range(len(matriz)):
	    primos = []
	    for l in range(len(matriz[k])):
	        numero = matriz[k][l]
	        cont = 0
	        
	        for m in range(1, numero+1):
	            if numero%m==0:
	                cont+=1
	                
	        if cont == 2:
	            primos.append(numero)
	            
	    if len(primos) != 0:
	        menor = primos[0]
	        cont2 = 0
	        
	        for n in range(len(primos)):
	            if primos[n]<menor:
	                menor = primos[n]
	                
	        for g in range(6):
	            if matriz[k][g] == menor:
	                pos = k, g
	                cont2+=1
	                
	            if cont2 == 1:
	                break;
	                
	        print "El numero primo menor de la fila %d es %d"%(k, menor)
	        
	    else:
	        print "No se ingreso ningun numero primo en la fila %d"%k
	

except ValueError:
    print "Error..."
