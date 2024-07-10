'''Lumines: Puzzle Fusion,1,14.95,Sony PSP,2004
WarioWare Touched!,2,22.95,Nintendo DS,2004
Hot Shots Golf: Open Tee,1,12.95,Sony PSP,2004'''
'''nombre del juego,cantidad de jugadores, precio, consola, año'''

import csv
arch =open("juegos.csv","r",newline= '')
contenido_darchivo = csv.reader(arch)

def menu():
    print("1 Filtro jugador:")
    print("2 Filtro precio:")
    print("3 Filtro consola y año:")
    print("4 Escribir archivo:")
    print("5 salir")

def escribir_archivo(lista):
    try:

        contenido = ""
        archivo = open("filtro_juegos.txt","w")
        for i in lista:
            contenido += i+"\n"
            
        
        archivo.write(contenido)
        print("archivo creado ")
        archivo.close()
    except:
        print("a ocurrido un error, asegurese de buscar juegos primero ")


            


def buscar_player(indice,coincidencia):
    

    lista = []
    cont = 0
    for i in contenido_darchivo:

        if i[indice] == coincidencia:
            lista.append(i[0])
            
            cont+=1
            if cont == 10 :
                break
       
    return lista 
def filtro_precio(indice_maximo, indice_minimo ):
    lista = []
    cont = 0

    for i in contenido_darchivo:
        if float(i[2]) >= indice_minimo and float(i[2]) <= indice_maximo:
            lista.append(i[0])
            
            cont +=1  
            if cont == 10 :
                break
    return lista
def filtro_consola_año(indice,indice2,consola,año):
    lista = []
    
    cont = 0
    for i in contenido_darchivo:
        if i[indice] == consola and i[indice2] == año:
            lista.append(i[0])
            
            cont +=1
            if cont == 10:
                break
    return lista

def menu_archivo():
    print("*menu*\n ¿que desea guardar en archivo?")
    print("1 Filtro jugador:")
    print("2 Filtro precio:")
    print("3 Filtro consola y año:")



    



#main
op = ""
while op != "5":
    menu()
    op = input("ingrese una opcion ")

    if op == "1":
        lista_player = []
        indice = 1
        cantidad_jugadores = input("ingrese cantidad de jugadores ")
        lista_player = buscar_player(indice,cantidad_jugadores)
        if len(lista_player) == 0:
            print("no se han encontrado coincidencias ")
        else :
            print(lista_player)
        
    elif op == "2":
        lista_precios = []
        precio_mimino = float(input("ingrese precio minimo "))
        precio_maximo = float(input("ingrese precio maximo "))
        
        

        lista_precios = filtro_precio(precio_maximo  , precio_mimino )
        if len(lista_precios) == 0 :
            print("no se encontraron coincidencias ")
        else:
            print(lista_precios)

    elif op =="3":
        lista_consola_año = []
        indice_consola = 3
        indice_año = 4
        consola = input("ingrese consola a buscar ")
        año = input("ingrese año de busqueda ")
        lista_consola_año = filtro_consola_año(indice_consola,indice_año,consola,año)
        if len(lista_consola_año) == 0 :
            print("no se encontraron coincidencias ")
        else:
            print(lista_consola_año)

    elif op == "4":
        while True:
            menu_archivo()
            op2 = input("ingrese una opcion ")
            if op2 == "1":
                
                    escribir_archivo(lista_player)
                    break
            elif op == "2":
                
                    escribir_archivo(lista_precios)
                    break
            elif op2 == "3":
               
                
                    escribir_archivo(lista_consola_año)
                    break
            
if op == "5":
    print("saliendo del programa... .. . ")



arch.close
        
    







