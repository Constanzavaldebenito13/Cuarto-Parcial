#Sin parametros sin retorno
def saludo():
    print("Hola amistad")

saludo()

#Sin Parametros con retorno
def obtener_mensaje():
    return ("Hoy aprendemos def")

mensaje = obtener_mensaje()
print(mensaje)

#Con parametros sin retorno
def saludo(nombre):
    print(f"Hola,{nombre}, Bienvenido")

saludo ("Carlos")
saludo ("Maria")

#Con Argumento y con parametros
def suma (a,b): #Parametro
    return a + b
resultado = suma (1, 4) #Argumento

print ("Resultado: ",resultado)