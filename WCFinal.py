archivo=open("storage/emulated/0/qpython/python/estelorem.txt", "r")
for texto1 in archivo.readlines():
	print(texto1)   #Va aparecer el texto en pantalla.


def finalwc():        #se define el archivo.
	try:               
		estelorem=input("Introduce el nombre del archivo: ")   #estelorem alude al nombre elegido del txt de prueba
		print()
		print(" El archivo es: ",estelorem)
		
				
		def contador_palabras():
		    archivo = open(estelorem, "r")
		    lee = archivo.read()
		    palabras = lee.split()
		    cantidadpalabras = len(palabras)
		    print(" El archivo tiene: ", cantidadpalabras, "palabras")
	
		def contador_caracteres():
		    archivo = open(estelorem, "r")
		    carac = archivo.read()
		    caracteres = len(carac)	
		    print(" El archivo tiene: ", caracteres, "caracteres")
		
		def contador_lineas():
		    archivo = open(estelorem, "r")
		    lineas = archivo.readlines()
		    cantidadlineas=len(lineas)
		    print(" El archivo tiene: ", cantidadlineas, "líneas")		
		
		def contador_parrafos():
		    archivo =open(estelorem, "r")
		    leer_texto= archivo.read()
		    cant_parrafos = leer_texto.split(".\n")
		    parrafos= len(cant_parrafos)
		    print(" El archivo tiene:", parrafos, "párrafos")
		
		def contador_oraciones2():
		    archivo = open(estelorem, "r")
		    oraciones1 = archivo.read()
		    oraciones2 =oraciones1.count(".")
		    print ("La cantidad de oraciones es:", oraciones2)
		
		def busca_palabra():
		    archivo = open(estelorem,"r")
		    contenido = archivo.read()
		    string = input("Ingrese que palabra buscar: ")
		    veces = contenido.count(string)
		    print('La palabra "{}" aparece {} vez/veces.'.format(string,veces))	
			
		def remplaza_1palabra():
		    archivo = open(estelorem,"r")
		    contenido1 = archivo.read()
		    remplazar = contenido1.replace('Lorem', 'hola', 1)
		    print("Texto remplazado:", remplazar)
		
		def ubicacion_find():
		    archivo =open(estelorem, "r")
		    buscador = archivo.read()
		    buscador2= buscador.find("ipsum")
		    print ("Aparece:", buscador2)
		
		def posicion_index():
		    archivo =open(estelorem, "r")
		    posicion = archivo.read()
		    encontrar = posicion.index("ipsum")
		    print ("Aparece:", encontrar)
		
		def oracioness():
		    archivo =open(estelorem, "r")
		    textoo=archivo.read()
		    punto="."
		    punto2="./n"
		    cant_oraciones=0
		    if (punto or punto2):
		       cant_oraciones=+1
		       cant_oraciones=textoo.count(punto)
		    print("La cantidad de oraciones presente en el texto es de: ", cant_oraciones, "oracion/es")

			
		def remplazar_vocales():
		    archivo = open(estelorem,"r")
		    contenido1 = archivo.read()
		    remplazar = contenido1.replace('e', 'a')
		    print("Texto remplazado:", remplazar)
		archivo.close()
		contador_palabras()
		contador_caracteres()
		contador_lineas()
		contador_parrafos()
		contador_oraciones2()
		busca_palabra()
		remplaza_1palabra()
		ubicacion_find()
		posicion_index()
		oracioness()
		remplazar_vocales()
		
		
		
		
	except:
		print(" El nombre del archivo es incorrecto") 
		print(" Pruebe con ingresar la ruta del archivo, por ejemplo: storage/emulated/0/qpython/python/estelorem.txt")
#el ejemplo es la ruta desde una tablet


finalwc()



