#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from random import choice

calificacion_alumno = {}
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = ['Alonso',
            'Eduardo',
            'Gerardo',
            'Rafael',
            'Antonio',
            'Fernanda',
            'Angel',
            'Itzel',
            'Karina',
            'Esteban',
            'Alan',
            'Samuel',
            'Jose',
            'Guadalupe',
            'Angel',
            'Ulises']

def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])

##ejercicio 3 parte a
aprobados=[]
reprobados=[]

def dos_tuplas():
    for b in becarios:
        if calificacion_alumno[b] >= 8:
		aprobados.append(b)
	else:
		reprobados.append(b)
    aproba=tuple(aprobados)
    reproba=tuple(reprobados)
    return aproba,reproba

#ejercicio 3 parte b

def promedio():
    suma=0
    cont=0
    for b in becarios:
	suma+=float(calificacion_alumno[b])
	cont+=1
    total = suma/cont
    return total

#ejercicio 3 parte c

def conjunto_calif():
    conj=set()
    for b in becarios:
	conj.add(calificacion_alumno[b])
    return conj
    
    
asigna_calificaciones()
imprime_calificaciones()
print dos_tuplas()
print promedio()
print conjunto_calif()
