'''
    Blog de Notas de Jorge
    ----------------------
    v1.0
    ======================
    Ejercicio 3Puntos para el examen final del módulo
    Sin internet
    Solo Evernote
    No hay Slack
    #Para terminal
    #Pensar bien las opciones que tendrá el blog de notas
    #Diagramación en www.lucidchart.com (diagrama de flujo)
    #Entorno virtual Python 3.7.4
    #Git local
    #Finalizar 16:15 enviar enlace por Github
'''

# Escritura
'''
with open('archivo.txt', 'a') as f:
    for i in range(5):
        f.write(f'{txt}\n')
    f.close()
'''
    
# Lectura
'''
with open('archivo.txt', 'r') as f:
    for line in f:
        print(line)
'''
blog_de_jorge = {}

def añadir():
    dia = input('¿Para qué día es la nota?\n')
    nota = input('Escribe la nota: \n')
    blog_de_jorge[dia] = nota
    print(blog_de_jorge)
    f = open('archivo.txt', 'a')
    f.write(f'{dia}: ')
    f.write(f'{nota}\n')
    f.close()

def borrar():
    diaBorrar = input('¿Qué día quieres eliminar?\n')
    del(blog_de_jorge[diaBorrar])

def update():
    diaUpdate = input('¿Qué día quieres modificar?\n')
    notaUpdate = input('Escribe la nota: \n')
    blog_de_jorge[diaUpdate] = notaUpdate

def mostrar():
    print(blog_de_jorge)
    with open('archivo.txt', 'r') as f:
        for line in f:
            print(line)

def formatear():
    seguridad = input('¿Seguro que quieres formatear el bloc de notas? [S] / [N]\n').lower()
    if seguridad == 's':
        blog_de_jorge.clear()
        print(blog_de_jorge)
        run()
    else:
        run()
    
def run():
    pregunta = str(input('''
                Bienvenido al Blog de Notas
                ---------------------------
                    ¿Qué quiere hacer?
                    +++++++++++++++++
                    |[A]ñadir       |
                    |[B]orrar       |
                    |[U]pdatear     |
                    |[M]ostrar notas|
                    |[F]ormatear    |
                    |[S]alir        |
                    +++++++++++++++++
                ''').lower())
    if pregunta == 'a':
        añadir(), run()
    elif pregunta == 'm':
        mostrar(), run()
    elif pregunta == 'b':
        borrar()
        print(blog_de_jorge)
        run()
    elif pregunta == 'u':
        update()
        print(blog_de_jorge)
        run()
    elif pregunta == 'f':
        formatear()
    elif pregunta == 's':
        print('¡¡Adiós companyero!!')

run()