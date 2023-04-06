# -*- coding: utf-8 -*-
"""
BIBLIOTECA DE FUNCIONES - JUEGO DE PALABRAS
AUTOR: YEISSON RICARDO CASTILLO BUSTOS
VERSIÓN: 25
FECHA: 01/01/2022

INSTRUCCIONES:
    Para el funcionamiento de esta biblioteca el usuario debe tener acceso al módulo colorama y al módulo random.
    
    Además, en el mismo directorio que este archivo "biblioteca_yeisson_castillo.py" debe tener los archivos de texto que encontrá adjunto: 
        ---funcionamiento_puntaje.txt 
        ---jugadores.txt 
        ---palabras_rae.txt 
        ---puntajes_jugadores.txt 
        ---reglamento.txt
        
    Para más información sobre el módulo Colorama por favor diríjase a: https://pypi.org/project/colorama/
    
    Este juego fue diseñado en Spyder 5 (Spyder(spyder-cf)) y requiere que el jugador esté ingresando constantemente respuestas así que por favor lea las intrucciones del juego para ingresar una respuesta válida.
"""
######################### MÓDULOS IMPORTADOS

import colorama
from colorama import Fore, Back, Style
import random

######################### VARIABLES GLOBALES

# Variables Sección Funciones Apertura
Dificultad = 0
Nombre = 0

# Variables Sección Funciones Para Adminsitrar y Seleccionar las Palabras
PalabraAdivinar = 0
RespuestaPropuesta = 0
Intento = 0
PuntajePalabraNoExacta = 0
PuntajePalabraExacta=0
PuntajeAcumulado = 0

######################### LISTAS Y TUPLAS

Programacion = ["paradigma","variable","lenguaje","compilado","interpretado","función","clase","usuario","interfaz","booleano","ciclo","biblioteca","modulo","abstracción","algoritmo","análisis","aplicación","funcional","lógica","argumento","asignación","binario","bloque","cliente","usuario","comentario","compilador","número","excepción","error","interfaz","intérprete","método","palabra","parámetro","imperativa","datos","local","global","anidado","red","objeto","paquete","lista","tupla","programa","programador","ejecutar","software","código","especificación","flujo","sintaxis","unicode","operador","cáracter","símbolo","signo","diagrama","documentación","estructura","control","problema","python","java","operador","prueba","pseudocódigo","informática","aritmética","procesador","eficiencia","bit","sintaxis","semántica","memoria","modularidad","encapsulación","jerarquía","ingeniería","planificación","definición","precondición","resultado","requisitos","diseño","mantenimiento","validación","archivo","ambiente","desarrollo","matemáticas","codificar","digital","consola","programación","framework","acoplamiento","ámbito","asignación","librería","compilación","declaración","depuración","depurador","encapsulamiento","entero","herencia","instancia","máquina"]
Numeros = ("1","2","3","4","5","6","7","8","9","0")
ProgramacionFacil = []
ProgramacionMedio = []
LetrasRespuestaPropuesta = []
LetrasPalabraAdivinar = []
ListasPalabrasIncorrectas = []
ListaNombreJugadores = []
ListaPuntajeJugadores = []
UnionJugadorPuntaje = []

######################### FUNCIONES

def JuegoDePalabras():
    """
    Juego de palabras que permite al jugador adivinar palabras sobre una temática, asignar puntaje corresponiente a la precisión de su respuesta y guardar un puntaje.
    PRE:
        • Existencia funciones RecolectarNombreJugador(), Menu().
    POS:
        • Juego de palabras que:
            ---Pide nombre del jugador.
            ---Permite seleccionar entre dos níveles.
            ---Asigna Puntaje.
            ---Tiene conteo de intentos.
            ---Muestra lista con los mejores 10 jugadores.
    """
    RecolectarNombreJugador()
    Menu()
                
def RecolectarNombreJugador():
    """
    Solicita al jugador que ingrese su nombre para almacenarlo en la variable "Nombre" e imprime un mensaje de agradecimiento al usuario.
    PRE:
        • Existencia variable global Nombre.
        • Módulo colorama importado.
    POS:
        • Variable global "Nombre" con un valor distinto a 0.
        • Si no se ingresa ningún nombre, variable Nombre toma valor "Jugador Sin Nombre".
        • Mensaje de agradecimiento impreso con el nombre ingresado.
    """
    global Nombre
    print(Fore.YELLOW, Style.BRIGHT + """
        *************************************************
        ¡Bienvenid@ a Juego de Palabras de PROGRAMACIÓN!
        *************************************************
        """+ Fore.RESET, Style.RESET_ALL)
    Nombre = input("Por favor ingrese su nombre: ")
    if len(Nombre) == 0:
        Nombre = "Jugador Sin Nombre"
    print(Fore.YELLOW, Style.BRIGHT + """
            ¡Muchas gracias,""", Nombre + "!\n"+ Fore.RESET, Style.RESET_ALL)
    return Nombre

def Menu():
    """
    Solicita al jugador que seleccione entre ver el reglamento, ver cómo funciona la asignación del puntaje e iniciar el juego. 
    PRE:
        • Existencia funciones MostrarReglamento, MostrarFuncionamientoPuntaje y SeleccionarDificultad.
        • Módulo colorama importado.
    POS:
        • Jugador selecciona dificultad del juego si ingresó número 1.
        • Jugador ve reglamento si ingresó número 2.
        • Jugador ve cómo funciona la asignación del puntaje si ingresó número 3.
        • Jugador ve mensaje de error si ingresa número diferente de 1, 2 o 3 y se le solicita que ingrese una opción válida nuevamente.
    """
    print(Fore.BLUE, Style.BRIGHT +"""¿QUÉ LE GUSTARÍA HACER? """+ Fore.RESET, Style.RESET_ALL + """
Ingrese el número TRES (1) para INICIAR EL JUEGO.
Ingrese el número UNO (2) para VER el REGLAMENTO.
Ingrese el número DOS (3) para FUNCIONAMIENTO ASIGNACIÓN del PUNTAJE.
        """)
    Preguntar = input("Respuesta: ")
    if Preguntar == "1":
        SeleccionarDificultad()
    elif Preguntar == "2":
        MostrarReglamento()
    elif Preguntar == "3":
        MostrarFuncionamientoPuntaje()
    else:
        print(Fore.RED, Style.BRIGHT + "Selección incorrecta, por favor ingrese una opción válida."+ Fore.RESET, Style.RESET_ALL)
        Menu()
        
def MostrarReglamento():
    """
    Imprime en la pantalla reglamento del juego al usuario para, posteriormente, mostrar la función Menu().
    PRE:
        • Existencia archivo texto reglamento.txt en el mismo directorio que archivo biblioteca_yeisson_castillo.py.
        • Módulo colorama importado.
        • Existencia función Menu().
    POS:
        • Jugador ve el reglamento del juego en la pantalla.
        • Solicita al jugador que seleccione entre ver el reglamento, ver cómo funciona la asignación del puntaje e iniciar el juego.
    """
    with open("reglamento.txt","r",encoding="utf-8") as reglamento:
        file = reglamento.readlines()
        print("")
        print(Fore.BLUE, Style.BRIGHT + "REGLAMENTO" + Fore.RESET, Style.RESET_ALL)
        for i in file:
            print(i, end="")
    print("")
    Menu()

def MostrarFuncionamientoPuntaje():
    """
    Imprime en la pantalla funcionamiento de la asignación del puntaje en el juego al usuario para, posteriormente, mostrar la función Menu().
    PRE:
        • Existencia archivo texto funcionamiento_puntaje.txt en el mismo directorio que archivo biblioteca_yeisson_castillo.py.
        • Módulo colorama importado.
        • Existencia función Menu().
    POS:
        • Jugador ve el funcionamiento de la asignación del puntaje en la pantalla.
        • Solicita al jugador que seleccione entre ver el reglamento, ver cómo funciona la asignación del puntaje e iniciar el juego.
    """
    with open("funcionamiento_puntaje.txt","r",encoding="utf-8") as puntaje:
        file = puntaje.readlines()
        print("")
        print(Fore.BLUE, Style.BRIGHT + "FUNCIONAMIENTO PUNTAJE" + Fore.RESET, Style.RESET_ALL)
        for i in file:
            print(i, end="")
    print("")
    Menu()

def SeleccionarDificultad():
    """
    Solicita al jugador seleccionar la dificultad del juego y se asegura de que sea la temática y la dificultad deseada por el jugador.
    PRE:
        • Existencia variables globales Tematica, Dificultad.
        • Módulo colorama importado.
        • Existencia función MostrarDificultad().
    POS:
        • Nivel de dificultad fácil si usuario ingresó número 1 en segunda pregunta.
        • Nivel de dificultad medio si usuario ingresó número 2 en segunda pregunta.
        • Pantalla confirmatoria con la elección del usuario.
        • Jugador ve mensaje de error si ingresa número diferente de 1, 2 o 3 y se le solicita que ingrese una opción válida nuevamente.
    """
    global Dificultad
    print(Fore.BLUE, Style.BRIGHT+ """
****************************************************
A continuación, seleccionará el nivel.
Por favor INGRESE ÚNICAMENTE EL NÚMERO 1 o 2.
****************************************************""" + Fore.RESET, Style.RESET_ALL)
    print("""
Seleccione la dificultad con la que desea jugar.

Ingrese 1 para FÁCIL (Palabras de 8 o menos de 8 letras).
Ingrese 2 para MEDIO (Palabras de más de 8 letras).         
                  """)
    Dificultad = input("Respuesta: ")
    if Dificultad == "1":
        Dificultad = "FÁCIL"
    elif Dificultad == "2":
        Dificultad = "MEDIO"
    else:
        print(Fore.RED, Style.BRIGHT+"Selección incorrecta, seleccione otra vez"+ Fore.RESET, Style.RESET_ALL)
        SeleccionarDificultad()
    MostrarDificultad()
    return Dificultad 
    
def MostrarDificultad():
    """
    Imprime un mensaje en la pantalla con el nombre del jugador, el nivel de dificultad y la temática seleccionada.
    PRE:
        • Existencia función Jugar().
        • Existencia variables Nombre y Dificultad.
        • Módulo colorama importado.
    POS:
        • Mensaje con: nombre usuario, temática y dificultad seleccionada.
    """
    print("")
    print(Fore.GREEN, Style.BRIGHT+"""****************************************************
""",Nombre+", temática PROGRAMACIÓN, dificultad:", Dificultad, """
****************************************************"""+ Fore.RESET, Style.RESET_ALL)
    Jugar()
    
def Jugar():
    """
    Permite al jugador llevar a cabo una partida de Juego de Palabras de cinco intentos y al final pregunta si desea jugar nuevamente.
    PRE:
        • Existencia función RespuestaPropuestaJugador(),ValidarRespuestaPropuesta(), AsignarPuntaje(), ConteoIntentos(), ImprimirResultados(), JugarNuevo(), InformarJugadorPalabraAdivinar().
        • Existencia variables Puntaje y PuntajeAcumulado.
        • Existencia listas: ListasPalabrasIncorrectas, LetrasRespuestaPropuesta, LetrasPalabraAdivinar.
        • Módulo colorama importado.
    POS:
        • Iteración de 5 veces en las que se le pregunta al usuario que ingrese una palabra para poder validar si es la palabra por adivinar. Se evalúa cada palabra ingresada para asignar un puntaje. 
        • Intento igual a 5 si la respuesta propuesta es igual a la palabra por adivinar y el puntaje ganado por las palabras no exactas y las palabras exactas se acumulan y guardan en la variable Puntaje acumulado.
        • Si en la iteración número cinco la respuesta propuesta es diferente de la palabra por adivinar muestra mensaje indicando que agotó todos los intentos, imprime la palabra que era e informa que no ganó ningún punto por esa palabra.
        • Mensaje preguntando si desea jugar nuevamente o si desea terminar la partida.
    """
    global Puntaje
    global PuntajeAcumulado
    ListasPalabrasIncorrectas.clear()
    InformarJugadorPalabraAdivinar()
    LetrasRespuestaPropuesta.clear()
    LetrasPalabraAdivinar.clear()
    while Intento != 5:
        RespuestaPropuestaJugador()
        ValidarRespuestaPropuesta()
        AsignarPuntaje()
        ConteoIntentos()
        ImprimirResultados()
    if RespuestaPropuesta != PalabraAdivinar:
        if Intento == 5:
            print("")
            print(Fore.YELLOW, Style.BRIGHT+"Agotó todos sus intentos. La palabra era:",str(PalabraAdivinar)+ Fore.RESET, Style.RESET_ALL)
            print(Fore.YELLOW, Style.BRIGHT+"Perdió todo los puntos ganados por esta palabra"+ Fore.RESET, Style.RESET_ALL)
            PuntajeAcumulado += 0
            ListasPalabrasIncorrectas.clear()
    elif RespuestaPropuesta == PalabraAdivinar:
        print("")
        print(Fore.GREEN, Style.BRIGHT+"Correcto. La palabra era:",str(PalabraAdivinar)+ Fore.RESET, Style.RESET_ALL)
        PuntajeAcumulado += PuntajePalabraNoExacta+PuntajePalabraExacta
        print("")
        ListasPalabrasIncorrectas.clear()
    JugarNuevo()

def ClasificarPalabrasProgramacion():
    """
    Clasifica los elementos de la lista Programación en otras dos listas dependiendo de su longitud.
    PRE:
        • Existencia listas Programacion, ProgramacionMedio y ProgramacionFacil.
    POS:
        • Lista ProgramacionFacil con todas las palabras de lista Programación con menos de ocho letras.
        • Lista ProgramacionMedio con todas las palabras de lista Programación con más de ocho letras.
    """
    for e in Programacion:
        if len(e) <= 8:
            ProgramacionFacil.append(e)
        elif len(e) > 8:
            ProgramacionMedio.append(e)

def InformarJugadorPalabraAdivinar():
    """
    Llama función SeleccionarPalabraAdivinar() para seleccionar la palabra que adivinará el usuario e imprime en la pantalla mensaje con la cantidad de letras que contiene la palabra por adivinar.
    PRE:
        • Existencia variable global PalabraAdivinar.
        • Existencia función SeleccionarPalabraAdivinar()
        • Módulo Colorama importado.
    POS:
        • Función SeleccionarPalabraAdivinar() llamada.
        • Mensaje en la pantalla con la cantidad de letras de la palabra por adivinar.
        • Una barra al piso "_" por cada letra que contiene la palabra por adivinar.
    """
    global PalabraAdivinar
    SeleccionarPalabraAdivinar()
    print(Fore.BLUE, Style.BRIGHT + """
La palabra por adivinar tiene""",str(len(PalabraAdivinar)),"""letras."""+ Fore.RESET, Style.RESET_ALL)
    for letra in PalabraAdivinar:
        print("_ ", end="")

def SeleccionarPalabraAdivinar():
    """
    Obtiene una palabra de listas (ProgramacionFacil o ProgramacionMedio o EmprendimientoFacil o EmprendimientoMedio) dependiendo de las elecciones del jugador.
    PRE:
        • Existencia listas ProgramacionFacil, ProgramacionMedio, EmprendimientoFacil, EmprendimientoMedio.
        • Existencia variable global PalabraAdivinar
        • Existencia funciones ClasificarPalabrasProgramacion y ClasificarPalabrasEmprendimiento.
        • Módulo random importado.
    POS:
        • Devuelve palabra aleatoria de lista ProgramacionFacil si usuario seleccionó temática Programación y dificultad Fácil.
        • Devuelve palabra aleatoria de lista ProgramacionMedio si usuario seleccionó temática Programación y dificultad Medio.
        • Devuelve palabra aleatoria de lista EmprendimientoFacil si usuario seleccionó temática Emprendimiento y dificultad Fácil.
        • Devuelve palabra aleatoria de lista EmprendimientoMedio si usuario seleccionó temática Emprendimiento y dificultad Medio.
    """
    ClasificarPalabrasProgramacion()
    global PalabraAdivinar
    if Dificultad == "FÁCIL":
        PalabraAdivinar = random.choice(ProgramacionFacil)
    if Dificultad == "MEDIO":
        PalabraAdivinar = random.choice(ProgramacionMedio)
    return PalabraAdivinar

def RespuestaPropuestaJugador():
    """
    Informa al jugador el número de letras que tiene la palabra por adivinar y solicita al jugador ingresar una palabra.
    PRE:
        • Existencia variable global RespuestaPropuesta.
        • Módulo colorama importado.
    POS:
        • Mensaje con el número de letras que tiene la palabra por adivinar.
        • Variable RespuestaPropuesta con la respuesta del usuario.
    """
    global RespuestaPropuesta
    global Intento
    print("")
    print(Fore.BLUE,Style.BRIGHT+"""
La palabra por adivinar tiene""",str(len(PalabraAdivinar)),"""letras.
""""Por favor ingrese su palabra propuesta: "+ Fore.RESET, Style.RESET_ALL, end="")
    RespuestaPropuesta = str(input())
    print("")
    return RespuestaPropuesta
    
    
def ValidarRespuestaPropuesta():
    """
    Valida que la palabra del jugador no contenga números, sea real y tenga la misma cantidad de letras que la palabra por adivinar y arroja un error en caso de que no cumpla algunos de los requerimientos.
    PRE:
        • Existencia variable global RespuestaPropuesta.
        • Existencia variable global PalabraAdivinar.
        • Existencia función AsignarPuntaje().
        • Existencia del archivo de texto "palabras_rae.txt" en el mismo directorio que esta biblioteca.
        • Existencia listas ListasPalabrasIncorrectas y Programacion.
        • Módulo colorama importado.
    POS:
        • Mensaje de error relacionada con la lóngitud de la palabra si la respuesta propuesta no tiene la misma longitud que la palabra por adivinar y solicita al jugador ingresar una nueva palabra propuesta.
        • Mensaje de error si la palabra ingresada tiene algún número y solicita al jugador ingresar una nueva palabra propuesta.
        • Mensaje de error si la palabra ingresada no se encuentra en el archivo "palabras_rae.txt" y solicita al jugador ingresar una nueva palabra.
        • Mensaje de error si la palabra ingresada no se encuentra en la lista "programación" y solicita al jugador ingresar una nueva palabra.
        • Mensaje de error si la palabra ingresada es incorrecta, y se ingresó anteriormente por lo que se encuentra en la lista "ListasPalabrasIncorrectas" y solicita al jugador ingresar una nueva palabra que no haya intentado.
        • Si la palabra tiene la misma longitud de la palabra que se está pidiendo y se encuentra en el archivo "palabras_rae.txt" o lista programacion se llama a la función AsignarPuntaje() para asignar puntaje a la palabra ingresada.
        
        palabras_rae.txt tomado de Jorge Duenas Lerin https://github.com/JorgeDuenasLerin/diccionario-espanol-txt
    """
    if len(RespuestaPropuesta) != len(PalabraAdivinar):
        print(Fore.RED,Style.BRIGHT+"La palabra ingresada NO TIENE LA MISMA LONGITUD. MÍNIMO",str(len(PalabraAdivinar)),"LETRAS. Ingrese una nueva palabra, por favor."+ Fore.RESET, Style.RESET_ALL)
        RespuestaPropuestaJugador()
        ValidarRespuestaPropuesta()
    elif any(i.isdigit() for i in RespuestaPropuesta):
        print(Fore.RED,Style.BRIGHT+"INGRESÓ NÚMEROS, por favor ingrese letras. MÍNIMO",str(len(PalabraAdivinar)),"LETRAS. Ingrese una nueva palabra, por favor."+ Fore.RESET, Style.RESET_ALL)
        RespuestaPropuestaJugador()
        ValidarRespuestaPropuesta()
    elif len(RespuestaPropuesta) == len(PalabraAdivinar):
        with open("palabras_rae.txt","r",encoding="utf-8") as rae:
            if RespuestaPropuesta in ListasPalabrasIncorrectas:
                print(Fore.RED,Style.BRIGHT+"La palabra ingresada ya fue ingresada y es incorrecta. Ingrese una nueva palabra que cumpla las características"+ Fore.RESET, Style.RESET_ALL)
                RespuestaPropuestaJugador()
                ValidarRespuestaPropuesta()
            elif RespuestaPropuesta in rae.read():
                AsignarPuntaje()
            elif RespuestaPropuesta in Programacion:
                AsignarPuntaje() 
            elif RespuestaPropuesta not in rae.read():
                print(Fore.RED,Style.BRIGHT+"La palabra ingresada no se considera válida, ingrese otra palabra, por favor asegúrese de que sea una palabra real y evite cualquier palabra inventada. Recuerde que son palabras en español o en algunos casos anglisismos típicos del mundo de la tecnología o programación. Las TILDES afectan: balon no se considera válida pero balón sí."+ Fore.RESET, Style.RESET_ALL)
                RespuestaPropuestaJugador()
                ValidarRespuestaPropuesta()
                
def AsignarPuntaje():
    """
    Asigna un puntaje a la respuesta propuesta del usuario de acuerdo con su precisión y de las reglas establecidas en archivo txt "funcionamiento_puntaje.txt" y si la palabra ingresada no es la palabra por adivinar la añade a la lista ListasPalabrasIncorrectas.
    PRE:
        • Existencia variables globales PuntajePalabraNoExacta y PuntajePalabraExacta.
        • Existencia función ListarPalabras().
        • Existencia lista ListasPalabrasIncorrectas.
    POS:
        • Si la palabra ingresada no es igual a la palabra por adivinar: 
            --Variable PuntajePalabraNoExacta tendrá +1 por cada letra de la palabra ingresada que esté en la palabra por adivinar. 
            --PuntajePalabraNoExacta tendrá +1 extra por cada letra de la palabra propuesta que esté en la misma posición de las letras de la palabra por adivinar.
            --La palabra propuesta se añadirá a la lista "ListasPalabrasIncorrectas".
        • Si la palabra ingresada es igual a la palabra por adivinar: 
            --Variable PuntajePalabraExacta aumentará x 4 por cada palabra dentro de la palabra
            --Lista "ListasPalabrasIncorrectas" vacía.
    """
    global PuntajePalabraNoExacta
    global PuntajePalabraExacta
    ListarPalabras()
    CantidadLetrasenPalabra = 0
    if RespuestaPropuesta != PalabraAdivinar:
        for letra in RespuestaPropuesta:
            if letra in PalabraAdivinar:
                CantidadLetrasenPalabra += 1
        CantidadLetrasenPalabra = CantidadLetrasenPalabra / 2
        CantidadLetrasenPalabra = int(CantidadLetrasenPalabra)
        PuntajePalabraNoExacta = PuntajePalabraNoExacta + (1 * CantidadLetrasenPalabra)
        for l1, l2 in zip(LetrasRespuestaPropuesta,LetrasPalabraAdivinar):
            for ConjuntoListaRPPA in zip(l1, l2):
                if ConjuntoListaRPPA[0] == ConjuntoListaRPPA[1]:
                    PuntajePalabraNoExacta += 1
        ListasPalabrasIncorrectas.append(RespuestaPropuesta)
    elif RespuestaPropuesta == PalabraAdivinar:
        PuntajePalabraExacta = (4 * len(RespuestaPropuesta))
        ListasPalabrasIncorrectas.clear()
    return PuntajePalabraNoExacta
    return PuntajePalabraExacta

def ListarPalabras():
    """
    Asigna cada uno de los carácteres por separados en variable RespuestaPropuesta a la lista LetrasRespuestaPropuesta. Asigna cada uno de los carácteres por separados en variable PalabraAdivinar a la lista LetrasPalabraAdivinar.
    PRE:
        • Existencia variable global RespuestaPropuesta y PalabraAdivinar.
        • Existencia listas LetrasRespuestaPropuesta y LetrasPalabraAdivinar.
    POS:
        • Lista LetrasRespuestaPropuesta con cada una de las letras de RespuestaPropuesta por separado.
        • Lista LetrasPalabraAdivinar con cada una de las letras de PalabraAdivinar por separado.
    """
    for letra in RespuestaPropuesta:
        LetrasRespuestaPropuesta.append(letra)
    for letra in PalabraAdivinar:
        LetrasPalabraAdivinar.append(letra)

    
def ConteoIntentos():
    """
    Lleva el conteo con los intentos de palabras propuestas que lleva el jugador.
    PRE:
        • Existencia variables globales Intento, RespuestaPropuesta y PalabraAdivinar.
    POS:
        • Variable Intento +1 por cada palabra incorrecta que ingrese el jugador.
        • Variable Intento igual a 5 si la palabra ingresada por el jugador es la misma que la palabra por adivinar.
    """
    global Intento
    if RespuestaPropuesta != PalabraAdivinar:
        Intento = Intento +1
    elif RespuestaPropuesta == PalabraAdivinar:
        Intento = 5
    return Intento


def ImprimirResultados():
    """
    Imprime resultados relacionados con la palabra ingresada dependiendo de su similitud con la palabra por adivinar. Entre la información que puede mostrar está: palabra ingresada, letras en posición correcta, letras en posición incorrecta, número de intento, puntaje por esa palabra, puntaje acumulado por todas las palabras.
    PRE:
        • Existencia variables globales Intento, RespuestaPropuesta, PalabraAdivinar, PuntajePalabraNoExacta, PuntajePalabraExacta y PuntajeAcumulado.
        • Existencia listas LetrasRespuestaPropuesta, LetrasPalabraAdivinar y ListasPalabrasIncorrectas.
        • Módulo colorama importado.
    POS:
        • Si la palabra propuesta es diferente a la palabra por adivinar mensaje en la terminal con: 
            ---Palabra ingresada.
            ---Letras en posición correcta. 
            ---Letras en posición incorrecta. 
            ---Lista con palabras ingresadas que son incorrectas. 
            ---Número de intento. 
            ---Puntaje por esa palabra.
            ---Puntaje acumulado por todas las palabras.
        • Si la palabra propuesta es igual a la palabra por adivinar mensaje en la terminal con:
            ---Palabra ingresada.
            ---Puntaje por esa palabra.
            ---Puntaje acumulado por todas las palabras.
        • Listas LetrasPosicionCorrecta, LetrasPosicionIncorrecta, LetrasRespuestaPropuesta, LetrasPalabraAdivinar vacias.
    """
    LetrasPosicionCorrecta = []
    LetrasPosicionIncorrecta = []
    print(Fore.MAGENTA,Style.BRIGHT+"***************************************"+Fore.RESET,Style.RESET_ALL)
    print("Palabra ingresada:",Fore.BLUE,Style.BRIGHT+RespuestaPropuesta+Fore.RESET, Style.RESET_ALL)
    if RespuestaPropuesta != PalabraAdivinar:
        print("\nLetras en posición correcta (2 puntos):")
        for l1, l2 in zip(LetrasRespuestaPropuesta,LetrasPalabraAdivinar):
            for ConjuntoListaRPPA in zip(l1, l2):
                if ConjuntoListaRPPA[0] == ConjuntoListaRPPA[1]:
                    LetrasPosicionCorrecta.append(l1)
        for letra in LetrasPosicionCorrecta:
            if LetrasPosicionCorrecta.count(letra) > 1:
                LetrasPosicionCorrecta.remove(letra)
        for letra in LetrasPosicionCorrecta:
            print(Fore.GREEN, Style.BRIGHT+letra+Fore.RESET, Style.RESET_ALL,end="")
        print("\nLetras en posición incorrecta (1 punto):")
        for l1, l2 in zip(LetrasRespuestaPropuesta,LetrasPalabraAdivinar):
            for ConjuntoListaRPPA in zip(l1, l2):
                if ConjuntoListaRPPA[0] != ConjuntoListaRPPA[1]:
                    LetrasPosicionIncorrecta.append(l1)
        print(Fore.YELLOW, Style.BRIGHT+" ".join(set(LetrasPosicionIncorrecta)&set(LetrasPalabraAdivinar))+Fore.RESET, Style.RESET_ALL,end="")
        print("\nPalabras ingresadas que son incorrectas:")
        print(" ".join(set(ListasPalabrasIncorrectas)))
        print("")
        print(Fore.YELLOW, Style.BRIGHT+"Intento número:", str(Intento)+Fore.RESET, Style.RESET_ALL)
    print("\nPUNTAJE POR ESTA PALABRA:",Fore.MAGENTA, Style.BRIGHT+str(PuntajePalabraNoExacta+PuntajePalabraExacta)+Fore.RESET, Style.RESET_ALL, "puntos.")
    print("\nPUNTAJE ACUMULADO TODAS PALABRAS:",Fore.MAGENTA, Style.BRIGHT+str(PuntajeAcumulado)+Fore.RESET, Style.RESET_ALL, "puntos.")
    LetrasPosicionCorrecta.clear()
    LetrasPosicionIncorrecta.clear()
    LetrasRespuestaPropuesta.clear()
    LetrasPalabraAdivinar.clear()
    
def JugarNuevo():
    """
    Pregunta al jugador si desea jugar otra partida o quiere terminar el juego y guardar su puntaje acumulado.
    PRE:
        • Existencia variables globales Intento, PuntajePalabraNoExacta y PuntajePalabraExacta.
        • Existencia lista ListasPalabrasIncorrectas.
        • Existencia funciones SeleccionarDificultad(), AsignarProcesarMejoresDiezPuntajes() y ArgumentoCierreIncorrecto()
        • Módulo colorama importado.
    POS:
        • Si respuesta igual a 1:
            ---Variables Intento, PuntajePalabraNoExacta y PuntajePalabraExacta iguales a 0.
            ---Lista ListasPalabrasIncorrectas vacia.
            ---Llama función SelccionarDificultad().
        • Si respuesta igual a 2:
            --- Mensaje de agradecimiento con puntaje total.
            ---Lista con los diez mejores puntajes hasta ahora.
        • Si respuesta distinta de 1 o 2:
            ---Mensaje de error solicitándole ingresar una respuesta válida.
    """
    global Intento
    global PuntajePalabraNoExacta
    global PuntajePalabraExacta
    print("")
    print(Fore.BLUE, Style.BRIGHT+"¿Desea jugar con otra palabra?"+ Fore.RESET, Style.RESET_ALL)
    print("""
Ingrese 1 para jugar de nuevo.
Ingrese 2 para terminar y guardar su puntaje acumulado.
Respuesta: """, end="")
    print("")
    Respuesta = input()
    if Respuesta == "1":
        Intento = 0
        PuntajePalabraNoExacta = 0
        PuntajePalabraExacta = 0
        ListasPalabrasIncorrectas.clear()
        SeleccionarDificultad()
    elif Respuesta == "2":
        print("")
        print("Muchas gracias por jugar, su puntaje total fue",Fore.YELLOW, Style.BRIGHT+str(PuntajeAcumulado)+ Fore.RESET, Style.RESET_ALL)
        AsignarProcesarMejoresDiezPuntajes()
    else:
        print(Fore.RED, Style.BRIGHT+"Selección incorrecta, seleccione una opción válida"+ Fore.RESET, Style.RESET_ALL)
        JugarNuevo()
        

def AsignarProcesarMejoresDiezPuntajes():
    """
    Crea una lista con los 10 mejores puntajes históricos del juego y los imprime en la pantalla.
    PRE:
        • Existencia funciones GuardarNombreJugador, GuardarPuntajeJugador, CrearListaJugadores, CrearListaPuntajeJugadores, CrearListaMejoresDiezPuntajes y ImprimirListaMejoresDiezPuntajes.
    POS:
        • Lista impresa con los diez mejores puntajes históricos.
    """
    GuardarNombreJugador()
    GuardarPuntajeJugador()
    CrearListaJugadores()
    CrearListaPuntajeJugadores()
    CrearListaMejoresDiezPuntajes()
    ImprimirListaMejoresDiezPuntajes()
    
def GuardarNombreJugador():
    """
    Guarda el nombre del jugador en archivo txt.
    PRE:
        • Existencia variable Nombre.
        • Existencia archivo txt "jugadores" en el mismo directorio que esta biblioteca.
    POS:
        • Nombre del jugador añadido al final del archivo jugadores.txt
    """
    with open("jugadores.txt","a",encoding="utf-8") as ListaJugadores:
        ListaJugadores.write(Nombre)
        ListaJugadores.write("\n") 

def GuardarPuntajeJugador():
    """
    Guarda el puntaje del jugador en archivo txt.
    PRE:
        • Existencia variable PuntajeAcumulado.
        • Existencia archivo txt "puntajes_jugadores" en el mismo directorio que esta biblioteca.
    POS:
        • Puntaje del jugador añadido al final del archivo puntajes_jugadores.txt
        • Variable PuntajeAcumulado en formato int.
    """
    global PuntajeAcumulado
    PuntajeAcumulado = str(PuntajeAcumulado)
    with open("puntajes_jugadores.txt","a",encoding="utf-8") as PuntajeJugadores:
        PuntajeJugadores.write(PuntajeAcumulado)
        PuntajeJugadores.write("\n")
    PuntajeAcumulado = int(PuntajeAcumulado)
    
def CrearListaJugadores():
    """
    Añade los nombres del archivo "jugadores.txt" en la lista ListaNombreJugadores.
    PRE:
        • Existencia lista ListaNombreJugadores.
        • Existencia archivo txt "jugadores.txt" en el mismo directorio que esta biblioteca.
    POS:
        • Lista ListaNombreJugadores con todos los nombres presentes en el archivo jugadores.txt eliminando items vacios y código de nueva línea "\n".
    """
    with open("jugadores.txt","r",encoding="utf-8") as ListaJugadores:
        archivo = ListaJugadores.readlines()
        for Jugadores in archivo:
            ListaNombreJugadores.append(Jugadores)
        for i,n in enumerate(ListaNombreJugadores):
            ListaNombreJugadores[i] = n.strip()     
        while "" in ListaNombreJugadores:
            ListaNombreJugadores.remove("")
        while "\n" in ListaNombreJugadores:
            ListaNombreJugadores.remove("\n")
            
def CrearListaPuntajeJugadores():
    """
    Añade los puntajes del archivo "puntajes_jugadores.txt" en la lista ListaPuntajeJugadores.
    PRE:
        • Existencia lista ListaPuntajeJugadores.
        • Existencia archivo txt "puntajes_jugadores.txt" en el mismo directorio que esta biblioteca.
    POS:
        • Lista ListaPuntajeJugadores con todos los puntajes presentes en el archivo puntajes_jugadores.txt en formato int.
    """
    DummyList = []
    with open("puntajes_jugadores.txt","r",encoding="utf-8") as PuntajeJugadores:
        archivo = PuntajeJugadores.readlines()
        for Puntajes in archivo:
            DummyList.append(Puntajes)
        for i,n in enumerate(DummyList):
            DummyList[i] = n.strip()
        while "" in DummyList:
            DummyList.remove("")
        for Puntajes in DummyList:
            ListaPuntajeJugadores.append(int(Puntajes))
            
def LlaveOrganizarMayoresPuntajes(Jugador):
    """
    Llave para identificar el puntaje por jugador en la lista de tuplas.
    PRE:
        • True.
    POS:
        • Índice del segundo item de una lista.
    """
    return Jugador[1]

def CrearListaMejoresDiezPuntajes():
    """
    Une los nombres y los puntajes para crear una lista con los diez mejores puntajes.
    PRE:
        • Existencia lista ListaPuntajeJugadores, ListaNombreJugadores y UnionJugadorPuntaje.
        • Existencia función LlaveOrganizarMayoresPuntajes()
    POS:
        • Lista UnionJugadorPuntaje con los diez mejores puntajes.
    """
    global UnionJugadorPuntaje
    UnionJugadorPuntaje = list(zip(ListaNombreJugadores,ListaPuntajeJugadores))
    UnionJugadorPuntaje.sort(key=LlaveOrganizarMayoresPuntajes, reverse=True)
    while len(UnionJugadorPuntaje) > 10:
        UnionJugadorPuntaje.pop()
    return UnionJugadorPuntaje

def ImprimirListaMejoresDiezPuntajes():
    """
    Imprime los diez mejores puntajes.
    PRE:
        • Existencia lista UnionJugadorPuntaje.
        • Módulo colorama importado. 
    POS:
        • Diez mejores puntajes impresos en el terminal.
    """
    print(Fore.MAGENTA, Style.BRIGHT+"""
******************************
Los 10 Mejores Jugadores son:
******************************
"""+ Fore.RESET, Style.RESET_ALL)
    if len(UnionJugadorPuntaje) == 0:
        print(Fore.BLUE, Style.BRIGHT+"Todavía no hay jugadores"+ Fore.RESET, Style.RESET_ALL)
    else:
        for e in UnionJugadorPuntaje:
            print(Fore.BLUE, Style.BRIGHT+"Jugador:"+ Fore.RESET, Style.RESET_ALL,e[0],Fore.BLUE, Style.BRIGHT+"Puntaje:"+ Fore.RESET, Style.RESET_ALL,e[1])
