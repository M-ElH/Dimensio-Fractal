from PIL import Image
from colornames import ColorNames
import Traducció_Colors
import easygui
import math
import webcolors
import os

def DFractal(im, path):
    os.system("cls")
    pixel_values = [] #conté els colors format RGB originals de la imatge per píxel, encara que es repeteixin

    size1 = im.size[0]
    size2 = im.size[1]

    def xvalue():
        x = 0
        while x <= size1:
            z = im.getpixel((x,y))
            pixel_values.append(z)
            x = x + 1
            if x == size1:
                break
    y = 0

    while y <= size2:
        xvalue()
        y = y + 1
        x =  0
        if y == size2:
            break

    print ("""
A continuació es farà l'anàl·lisi de la imatge {} X {}.
En total hi ha {} pixels en la imatge"


A continuació s'obtindran els colors de la imatge i s'obrirà la imatge com a referència.
Els noms poden ser una aproximació més o menys precisa, però fan referència a colors presents
en la imatge.

Obtenint colors... (pot tardar una mica)
    """.format(im.size[0], im.size[1], len(pixel_values)))

    name_of_colors = [] #igual que pixel_values però enlloc d'RGB, són els noms, encara que es repeteixin

    for pixel in pixel_values:
        try:
            color_name = webcolors.rgb_to_name(pixel)
            name_of_colors.append(Traducció_Colors.trad_i_simp(color_name))

        except ValueError:
            a = pixel[0]
            b = pixel[1]
            c = pixel[2]
            name_of_colors.append(ColorNames.findNearestImageMagickColorName(a,b,c))
            #Si no reconeix el color, trobarà el més proper. Per a fer-ho, reconeix el codi RGB com una llista
            #i separa els 3 valors, per a poder utilitzar ColorNames

    cleansedcolors = list(dict.fromkeys(name_of_colors))
    #dict.fromkeys crea un diccionari, on les claus són els valors de name_of_colors, i els valors són None
    #list(dict.fromkeys) converteix les claus del diccionari en una nova llista, convertint-les en els seus valors, i així s'eliminen repeticions. En altres paraules:
    #noms dels colors sense repetir-se

    os.startfile(path)
    print ("")

    a = 0
    for color in cleansedcolors:
        a = a + 1
        print ("{}: {}    ({} píxels d'aquest color)".format(a, color, name_of_colors.count(color)))


    print ("\nIntrodueix els números dels colors de dalt que siguin del contorn, un cada cop")
    print ("Exemple: 2")
    print ("\nPer a acabar d'escriure colors introdueix 'atura'")
    print ("Si vol eliminar un dels colors que ha introduït, introdueix 'elimina número'")
    print ("Exemple: elimina 1")

    color_contorn = None    #Variable per a què l'usuari introdueixi els noms de color del contorn de la seva imatge
    contorn = []

    while True:
        color_contorn = input("\n>> ")
        color_contorn = color_contorn.lower() #converteix txt en minúscules
        eliminar = color_contorn.split()

        if color_contorn == "":
            print ("Introdueix algun número o acció")

        elif eliminar[0] == "elimina":
            try:
                num_eliminat = int(eliminar[1])

                if contorn.count(cleansedcolors[num_eliminat - 1]) == 1:
                    contorn.remove(cleansedcolors[num_eliminat - 1])
                elif contorn.count(cleansedcolors[num_eliminat - 1]) == 0:
                    print ("No ha introduit el color {}".format(cleansedcolors[num_eliminat - 1]))

            except IndexError:
                print("No ha intentat eliminar un número correcte")
            except ValueError:
                print("No ha intentat eliminar un número")

        elif color_contorn == "atura":
                break

        elif color_contorn == "0": #si introdueix 0, es treballaria amb -1, que és l'últim número d'una llista
            print ("No s'ha introduït un número correcte")


        else:
            try:
                color_contorn = int(color_contorn)

                if contorn.count(cleansedcolors[color_contorn - 1]) == 0:
                    contorn.append(cleansedcolors[color_contorn - 1])
                elif contorn.count(cleansedcolors[color_contorn - 1]) == 1:
                    print ("Ja ha introduit aquest color, introdueix-ne un altre")


            except ValueError:
                print("No ha introduït un número/paraula vàlid")
            except IndexError:
                print ("No s'ha introduït un número correcte")


    suma_colors = 0
    for color in contorn:
        suma_colors = suma_colors + name_of_colors.count(color)


    return size1, suma_colors
