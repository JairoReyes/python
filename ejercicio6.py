#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT




var = [{1,(bin(n),hex(n))} for n in range(50) if bin(n).count('1')%2!=0 ]
print var
	


