#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

from poo1 import Becario
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

asigna_calificaciones()
imprime_calificaciones()

lista=[]
def generar_lista():
    for b in becarios:
	lista.append(Becario(b,calificacion_alumno[b]))
    for nombe in lista:
	print nombe
    return lista


print generar_lista()

