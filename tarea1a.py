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

def palindromo_mas_grande(cadena):
    """
    Crea subcadenas de la cadena original(todas las combianciones posibles) y las ingresa a la
 funcion palindromo para saber si son palindromos o no, en dado casi de que si sea palindromo,
 compara el tamano y si es mayor al que tenemos, lo modifica y guarda la palabra en una variable,
 que es la que se va a regresar
    Recibe:
	cadena(str) La cadena que se va a comparar
    Regresa:
	palin(str) Que es el palindromo mas grande

    """
    longitud=len(cadena)
    j=0
    tam=0
    while j<=longitud:
        i=1
        while i <= longitud:
	    if palindromo(cadena[j:i]):
		if len(cadena[j:i]) > tam:
	            tam=len(cadena[j:i])
		    palin=cadena[j:i]
	    i+=1
        j+=1
    return palin

var = raw_input("Ingresa la cadena\n")
print palindromo_mas_grande(var)
