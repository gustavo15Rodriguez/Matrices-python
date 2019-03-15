#-*-coding:utf-8-*-

'''14. Leer una matriz 5x5 entera y determinar cuántos números almacenados en ella tienen
mas de 3 dígitos. '''

if __name__ == '__main__':
	matriz = []
	cont2 = 0

try:
	for i in range(5):
		fila = []
		for j in range(5):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)

		matriz.append(fila)

	
	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			num = matriz[k][l]
			cont = 0
			while num>0:
				dig = num%10
				num=num//10
				cont+=1
			
			if cont>3:
				cont2+=1

	print "Hay %d numeros que tienen mas de 3 digitos."%cont2

except ValueError:
	print "Error..."