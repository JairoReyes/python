#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
import re
from re import search

patron=r"^((([1][0-9][0-9]|[2][0-5][0-5]|[0-9][0-9]|[0-9]|)\.){3}([1][0-9][0-9]|[2][0-5][0-5]|[0-9][0-9]|[0-9]|))$"

numero = raw_input("Ingrese la ipv4\n")
if re.match(patron,numero):
	print "Ip valida"
else:
	print "ip invalida"




patron2=r"^([A-Za-z][A-Za-z_\.]+@[A-Za-z\._-]+)$"

correo=raw_input("Ingrese el correo\n")
print correo

if re.match(patron2,correo):
	print "correo valido"
else:
	print "correo invalido"