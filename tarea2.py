def contra(n1,n2,n3):
	"""
	Crea una contraseña con m minusculas, n mayusculas y j digitos de forma recursiva
	Recibe:
		n1(int) El numero de minusculas
		n2(int) El numero de mayusculas
		n3(int) El numero de digitos
	Regresa:
		(str) La contrasena concatenada por m minusculas,n mayusculas y j digitos
	"""
	if n3==0 and n2==0 and n1==0:
		return " "
	if n3 == -1:
		return " "
	
	if n2 == -1:
		return " "
	
	if n1 == -1:
		return " "
	from random import choice
	if n3 > 0:
		return str(choice([0,1,2,3,4,5,6,7,8,9])) + str(contra(n1,n2,n3-1))
	if n1 > 0:
		return str(choice(['a','b','c','d','e','f','g','h','i','j'])) + str(contra(n1-1,n2,n3))
	if n2 > 0:
		return str(choice(['A','B','C','D','E','F','G','H','I','J'])) + str(contra(n1,n2-1,n3))
	

print contra(3,4,2)
