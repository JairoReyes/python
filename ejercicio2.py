def palindromo(nombre):
    """
    Verifica que una cadena sea igual a su inversa
    Recibe:
	nombre(str) La cadena que se va a comparar
    Regresa:
	True en dado caso que de ambas la cadena como su inversa sean iguales
	False si la cadena y su inversa son diferentes

    """
    if(nombre[::-1]==nombre):
	return True
    return False

if palindromo("anitalavalatinaS"):
	print "PALINDROMA"
else:
	print "NO PALINDROMA"
