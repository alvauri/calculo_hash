# Titulo: Ejemplo de calculo de hash con python
# AUTOR: Uriel Alvarez

"""
El prestente código es un ejemplo de como usar la libreria hashlib. Intentare hacer un código limpio
y documentado de como hacer un generador de contraseñas seguras usando python.
"""
# Importamos la libreria hashlib
import hashlib

# Creamos una funición para crear contraseña seguras
def generar_contraseña(usuario, contraseña):
    salt = "cadenasalunicaparacadausuario" # cadena de sal
    entrada = f"{usuario}:{contraseña}:{salt}"
    hash_obj = hashlib.sha256()
    hash_obj.update(entrada.encode('utf-8'))
    return hash_obj.hexdigest()
    
# Programa principal que interactua con el usuario

usuario = input("Por favor, ingrese nombre de usuario: ")
contraseña = input("Por favor, ingrese contraseña: ")

hash_contraseña = generar_contraseña(usuario, contraseña)
print(f"\033[92mLa contraseña segura para el usuario: \033[0m'{usuario}' \033[92mes:\033[0m '{hash_contraseña}'")


# En la salida cambié los colores pero esto No es necesario lo usé solo para resasltar la salida
# La forma para hacer  \033[92mEste texto es verde.\033[0m