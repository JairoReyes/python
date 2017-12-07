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


#numero=raw_input("Ingrese el numero\n")
if primo(71):
	print "Es primo"
else:
	print "No es primo"
