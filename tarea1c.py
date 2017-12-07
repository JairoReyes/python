def primo(num):
	"""
	Verifica que un numero sea primo o no
	Recibe:
		num(int) El numero que verificaremos si es primo
	Regresa:
		False en caso de no es primo
		True en caso de que sea primo
	"""
	cont=0
	i=1
	while i <= int(num):
		valor=float(num)%i
		if valor == 0:
			cont+=1;
		i+=1
	if cont==2:
		return True
	else:
		return False

def recur(valor,cont):
	"""
	Verifica obtiene los primos n primos de forma recursiva
	Recibe:
		valor(int) el numero de primos que piden
		cont(int) el numero que ira incrementando para reconocer si es primo o no(de 1 en 1)
	Regresa:
		lista2(list) Regresa la lista con los n primeros primos
	"""
	if valor == 0:
		lista=[]
		return lista
	
	if primo(cont):
		lista2=[cont]
		return lista2 + list(recur(valor-1,cont+1))
	else:
		return recur(valor,cont+1)

numero=raw_input("Ingrese el numero de primos a mostrar\n")
print recur(int(numero),0)

