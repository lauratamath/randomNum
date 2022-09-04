from time import time
import random
from tabulate import tabulate
from colorama import Fore, Style

def gen1(x):
    a = 5**5
    m = (2**35)-1
    return ((a*x)%(m)),((a*x)%(m))/(float(m))

def gen2(x):
    return (((7**5)*x)%((2**31)-1)),(((7**5)*x)%((2**31)-1))/(2**31-1)

def calc_porcentaje(part, whole):
  return str(100 * float(part)/float(whole)) + "%"

x = time()

iteraciones = 10000
print('-----------    ' + Fore.LIGHTMAGENTA_EX ,  iteraciones, Style.RESET_ALL + ' iteraciones ------------\n')
cont1, cont2, cont3, cont4, cont5, cont6, cont7, cont8, cont9, cont10 = 0,0,0,0,0,0,0,0,0,0

# ----------------------------------
# generador 1
# ----------------------------------

for i in range(iteraciones):
    new = gen1(x)[0]
    hist = gen1(x)[1] #histogramas
    if hist <=0.1 and hist >=0.0:
        cont1 += 1
    elif hist <=0.2 and hist >0.1:
        cont2 += 1
    elif hist <=0.3 and hist >0.2:
        cont3 += 1
    elif hist <=0.4 and hist >0.3:
        cont4 += 1
    elif hist <=0.5 and hist >0.4:
        cont5 += 1
    elif hist <=0.6 and hist >0.5:
        cont6 += 1
    elif hist <=0.7 and hist >0.6:
        cont7 += 1
    elif hist <=0.8 and hist >0.7:
        cont8 += 1
    elif hist <=0.9 and hist >0.8:
        cont9 += 1
    elif hist <=1.0 and hist >0.9:
        cont10 += 1
    x = new

whole = cont1 + cont2 + cont3 + cont4 + cont5 + cont6 + cont7 + cont8 + cont9 + cont10
print('|', Fore.GREEN + ' Generador 1                               ' + Style.RESET_ALL, '|')
tabla = [["0.0 - 0.1", cont1,calc_porcentaje(cont1,whole)],
        ["0.1 - 0.2", cont2,calc_porcentaje(cont2,whole)],
        ["0.2 - 0.3", cont3,calc_porcentaje(cont3,whole)],
        ["0.3 - 0.4", cont4,calc_porcentaje(cont4,whole)],
        ["0.4 - 0.5", cont5,calc_porcentaje(cont5,whole)],
        ["0.5 - 0.6", cont6,calc_porcentaje(cont6,whole)],
        ["0.6 - 0.7", cont7,calc_porcentaje(cont7,whole)],
        ["0.7 - 0.8", cont8,calc_porcentaje(cont8,whole)],
        ["0.8 - 0.9", cont9,calc_porcentaje(cont9,whole)],
        ["0.9 - 1.0", cont10,calc_porcentaje(cont10,whole)],
]
head = ["intervalo", "no. de veces", 'porcentaje']
print(tabulate(tabla, headers= head, tablefmt="grid"))

# ----------------------------------
# generador 2
# ----------------------------------

for i in range(iteraciones):
    #print("Vino x:", x)
    new = gen2(x)[0]
    hist = gen2(x)[1]
    if hist <=0.1 and hist >=0.0:
        cont1 += 1
    elif hist <=0.2 and hist >0.1:
        cont2 += 1
    elif hist <=0.3 and hist >0.2:
        cont3 += 1
    elif hist <=0.4 and hist >0.3:
        cont4 += 1
    elif hist <=0.5 and hist >0.4:
        cont5 += 1
    elif hist <=0.6 and hist >0.5:
        cont6 += 1
    elif hist <=0.7 and hist >0.6:
        cont7 += 1
    elif hist <=0.8 and hist >0.7:
        cont8 += 1
    elif hist <=0.9 and hist >0.8:
        cont9 += 1
    elif hist <=1.0 and hist >0.9:
        cont10 += 1

whole = cont1 + cont2 + cont3 + cont4 + cont5 + cont6 + cont7 + cont8 + cont9 + cont10
print('\n|', Fore.GREEN + ' Generador 2                               ' + Style.RESET_ALL, '|')
tabla = [["0.0 - 0.1", cont1,calc_porcentaje(cont1,whole)],
        ["0.1 - 0.2", cont2,calc_porcentaje(cont2,whole)],
        ["0.2 - 0.3", cont3,calc_porcentaje(cont3,whole)],
        ["0.3 - 0.4", cont4,calc_porcentaje(cont4,whole)],
        ["0.4 - 0.5", cont5,calc_porcentaje(cont5,whole)],
        ["0.5 - 0.6", cont6,calc_porcentaje(cont6,whole)],
        ["0.6 - 0.7", cont7,calc_porcentaje(cont7,whole)],
        ["0.7 - 0.8", cont8,calc_porcentaje(cont8,whole)],
        ["0.8 - 0.9", cont9,calc_porcentaje(cont9,whole)],
        ["0.9 - 1.0", cont10,calc_porcentaje(cont10,whole)],
]
head = ["intervalo", "no. de veces", 'porcentaje']
print(tabulate(tabla, headers= head, tablefmt="grid"))
