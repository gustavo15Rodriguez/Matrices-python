#-*-coding:utf-8-*-

'''34. Leer una matriz 4x6 entera y determinar cuántos de los números almacenados en ella
pertenecen a los 100 primeros elementos de la serie de Fibonacci.'''
	
if __name__ == '__main__':
	matriz = []
	fib = []

try:
	for i in range(4):
		fila = []
		for j in range(6):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)

		matriz.append(fila)
		numero = 1
		ultimo = 0
		penultimo = 0
		    
	for g in range(101):
		penultimo = ultimo
		ultimo = numero
		numero = penultimo+ultimo
		fib.append(numero)
	
	cont = 0
	for k in range(len(matriz)):
	    for l in range(len(matriz[k])):
	        num = matriz[k][l]
	        for s in range(len(fib)):
	            if fib[s] == num:
	                cont+=1
	                   
	print "Hay %d numeros que pertenecen a la serie Fibbonacci."%cont

except ValueError:
	print "Error..."
