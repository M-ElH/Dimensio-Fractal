import FD
import os
from PIL import Image
import easygui
from matplotlib import pyplot
import numpy
import math
import shutil


def dimensio():
    os.system("cls")
    print ("""
A continuació es calcularà la dimensió fractal de la imatge. Necessàriament ha de ser quadrada,
i preferiblement ha de ser a 2 colors o tenir-ne el mínim possible, i que els colors del contorn es puguin
diferenciar clarament de la resta. Tampoc es poden repetir fora del contorn.

Per a fer-ho, es generaran imatges de diferents mides a partir de la imatge que vol i se'n farà un anàlisi
del color dels píxels de cadascuna. S'obrirà la imatge de cada mida, la pot tancar o minimitzar per a tornar
al programa i introduir els colors que formen part del contorn.

Si interromp el programa enmig del procés, haurà d'eliminar manualment la carpeta generada abans de fer un
altre anàlisi.

***El resultat que s'obtindrà serà només una aproximació més o menys precisa***
""")

    input("Prem la tecla 'entrar' per a seleccionar la imatge> ")

    im = None
    user = os.getlogin()
    while im is None:
        try:
            dir = easygui.fileopenbox(msg = "Tria la imatge que vol", default = r"C:\Users\{}\Desktop\*".format(user))
            im = Image.open(dir)

        except:
            os.system("cls")
            print ("El fitxer no sembla ser una imatge")
            input("Prem 'entrar' per a tornar-ho a intentar")



    im2 = (im.resize((2,2))).convert("RGB")
    im4 = (im.resize((4,4))).convert("RGB")
    im8 = (im.resize((8,8))).convert("RGB")
    im16 = (im.resize((16,16))).convert("RGB")
    im32 = (im.resize((32,32))).convert("RGB")
    im64 = (im.resize((64,64))).convert("RGB")
    im128 = (im.resize((128,128))).convert("RGB")
    im256 = (im.resize((256,256))).convert("RGB")
    im512 = (im.resize((512,512))).convert("RGB")
    im1024 = (im.resize((1024,1024))).convert("RGB")

    mida_dir = len(dir)                    #mida del directori triat per l'usuar (fitxer inclòs)
    nom_arx = os.path.basename(dir)        #nom del arxiu triat per l'usuari
    mida_arx = len(nom_arx)                #mida de l'arxiu triat per l'usuari
    noudir = dir[:mida_dir - mida_arx]     #directori triat per l'usuari però sense l'arxiu (només la carpeta).
    dir_ims = noudir + r"Imatges_DF_mides"

    try:
        os.makedirs(dir_ims)
    except:
        shutil.rmtree(dir_ims)
        os.makedirs(dir_ims)


    im2.save(dir_ims + r"\im2.png", format = "PNG", quality = 95, subsampling = 0)
    im4.save(dir_ims + r"\im4.png", format = "PNG", quality = 95, subsampling = 0)
    im8.save(dir_ims + r"\im8.png", format = "PNG", quality = 95, subsampling = 0)
    im16.save(dir_ims + r"\im16.png", format = "PNG", quality = 95, subsampling = 0)
    im32.save(dir_ims + r"\im32.png", format = "PNG", quality = 95, subsampling = 0)
    im64.save(dir_ims + r"\im64.png", format = "PNG", quality = 95, subsampling = 0)
    im128.save(dir_ims + r"\im128.png", format = "PNG", quality = 95, subsampling = 0)
    im256.save(dir_ims + r"\im256.png", format = "PNG", quality = 95, subsampling = 0)
    im512.save(dir_ims + r"\im512.png", format = "PNG", quality = 95, subsampling = 0)
    im1024.save(dir_ims + r"\im1024.png", format = "PNG", quality = 95, subsampling = 0)


    dades2 = FD.analisi_pixels((im2), (dir_ims + r"\im2.png"))
    dades4 = FD.analisi_pixels((im4), (dir_ims + r"\im4.png"))
    dades8 = FD.analisi_pixels((im8), (dir_ims + r"\im8.png"))
    dades16 = FD.analisi_pixels((im16), (dir_ims + r"\im16.png"))
    dades32 = FD.analisi_pixels((im32), (dir_ims + r"\im32.png"))
    dades64 = FD.analisi_pixels((im64), (dir_ims + r"\im64.png"))
    dades128 = FD.analisi_pixels((im128), (dir_ims + r"\im128.png"))
    dades256 = FD.analisi_pixels((im256), (dir_ims + r"\im256.png"))
    dades512 = FD.analisi_pixels((im512), (dir_ims + r"\im512.png"))
    dades1024 = FD.analisi_pixels((im1024), (dir_ims + r"\im1024.png"))

    shutil.rmtree(dir_ims)
    os.system("cls")
    mides = [dades2[0], dades4[0], dades8[0], dades16[0], dades32[0], dades64[0], dades128[0], dades256[0], dades512[0], dades1024[0]]
    suma_colors = [dades2[1], dades4[1], dades8[1], dades16[1], dades32[1], dades64[1], dades128[1], dades256[1], dades512[1], dades1024[1]]

    x = []
    y = []

    for num in mides:
        x.append(math.log(num,10))


    for num in suma_colors:
        try:
            y.append(math.log(num,10))

        except ValueError:
            y.append(None)

    while None in y:
        del x[y.index(None)]
        y.remove(None)


    pendent = numpy.polyfit(x,y,1)
    df = pendent[0] - abs(pendent[1])

    os.system("cls")

    def print_dim():
        print("La dimensió fractal és {}".format(df))
        print ("""
***Aquesta és una aproximació més o menys precisa***
""")

    def final():
        os.system("cls")
        print_dim()
        decisio_final = input("""
Prem entrar sense introduir res si vol veure un gràfic de l'anàlisi fet.

Si vol analitzar una altra imatge, introdueix "1"

Si no, pot tancar el programa.
""")

        if decisio_final == "1":
            dimensio()

        else:
            pyplot.scatter(x,y)
            pyplot.xlabel("log(r) (mida de la imatge)")
            pyplot.ylabel("log(N) (píxels del contorn)")
            pyplot.title("Dimensió Fractal de {}".format(os.path.basename(dir)))
            pyplot.plot(x,y,label = "Pendent")
            pyplot.legend()
            pyplot.show()
            final()

    final()


dimensio()
