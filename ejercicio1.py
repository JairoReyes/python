#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#Jairo Alan Reyes Aldeco

aprobados = []

def aprueba_becario(nombre_completo):
    """
    Guarda el nombre del alumno en letras mayusculas en la lista aprobados en dado caso de que
 su nombre no se encuentre en la lista que se esta comparando  y los ordena.
    Recibe:
        nombre_completo(str) El nombre del alumno que se comparara
    Regresa:
	False en caso de que encuentre alguno de los nombres de la lista
        True en caso de el nombre no se encuentre el nombre
    """
    nombre_separado = nombre_completo.split()
    for n in nombre_separado:
        if n.upper() in ['Gerardo', 'Alan', 'Guadalupe', 'Rafael', 'Karina']:
            return False
    #nombre_completo=nombre_completo.upper()
    aprobados.append(nombre_completo.upper())
    aprobados.sort()
    #print aprobados
    return True


becarios = ['Becerra Alvarado Hugo Alonso',
            'Cabrera Balderas Carlos Eduardo',
            'Corona Lopez GeRArdo',
            'Diez Gutierrez Gonzalez Rafael'
            'Disner Lopez Marco Antonio',
            'Garcia Romo Claudia Fernanda',
            'Gonzalez Ramirez Miguel Angel',
            'Gonzalez Vargas Andrea Itzel',
            'Orozco Avalos Aline Karina',
            'Palacio Nieto Esteban',
            'ReYEs Aldeco Jairo Alan',
            'Santiago Mancera Arturo Samuel',
            'Sarmiento Campos Jose',
            'Sarmiento Campos Maria Guadalupe',
            'Valle Juarez Pedro Angel',
            'Viveros Campos Ulises']

for b in becarios:
    if aprueba_becario(b.upper()):
        print 'APROBADOO: ' + b
    else:
        print 'REPROBADO: ' + b


def eliminar(nombre):
    """
    Elimina el nombre del alumno de la lista de aprobados
    Recibe:
        nombre(str) El nombre del alumno que se eliminara
    Regresa:
	False en caso de no se encuentre el alumno en la lista
        True en caso de que el alumno se haya eliminado de la lista
    """
    if nombre in aprobados:
	aprobados.remove(nombre)
	print aprobados
	return True
    else:
	return False

if eliminar('REYES ALDECO JAIRO ALAN'):
	print "TRUE"
else:
	print "FALSE"

#print becarios
