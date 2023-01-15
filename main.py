def encriptar(texto):
    encriptado = ""
    for letra in texto:
        ascii = ord(letra)
        ascii += 4
        encriptado += chr(ascii)
    return encriptado

def desencriptar(archivo_encriptado):
    desencriptado = ""
    for caracteres in archivo_encriptado:
        ascii = ord(caracteres)
        ascii -=4
        desencriptado += chr(ascii)
    return desencriptado

def encriptarArchivos(rutaArchivo):
    try:
        archive = open(rutaArchivo, "r") 
        text = archive.read() 
        archive.close() 
        archivo_encriptado = encriptar(text) 
        archive = open(rutaArchivo, "w") 
        archive.write(archivo_encriptado) 
        archive.close() 
        print("Exito! El archivo se ha encriptado correctamente")
    except:
        print('Lo siento, el archivo que estamos buscando no existe.')
        exit()


def desencriptarArchivos(rutaArchivo):
    try:
        archive = open(rutaArchivo, "r")
        text = archive.read()
        archive.close()
        archivoDesencriptado = desencriptar(text)
        archive = open(rutaArchivo, "w")
        archive.write(archivoDesencriptado)
        archive.close()
        print("Exito! El archivo se ha desencriptado correctamente")
    except:
        print('Lo siento, el archivo que estamos buscando no existe.')
        exit()

accion = input('Para ENCRIPTAR un archivo presione la tecla "E" \n' 'Para DESENCRIPTAR un archivo presione la tecla "D" \n' '...')
rutaArchivo = input("Ingrese la ruta del archivo: ")

if accion.lower() == "e":
    encriptarArchivos(rutaArchivo)
else:
    desencriptarArchivos(rutaArchivo)