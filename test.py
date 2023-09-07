from operator import length_hint
from pickletools import read_unicodestring1
from ssl import CERT_REQUIRED


def tests(parametrs):
    a = parametrs # darbības ar parametriem.
    return a # funkcijas rezultāts.

# print(tests("kaķis"))


def pirmais(par1, par2):
    reizinajums = par1*par2
    summa = par1+par2
    if reizinajums<1000 :
        return reizinajums
    else:
        return summa


# print("The result is", pirmais(40,30))

def otrais(sakums = 0, beigas = 10, solis = 1) :
    esosais = 0
    ieprieksejais = 0
    for i in range(sakums, beigas, solis):
        ieprieksejais = esosais
        esosais = i
        summa = ieprieksejais + esosais
        print ("Current Number", esosais, "Previous Number", ieprieksejais, "Sum", summa)
    return

# otrais(0, 10, 1)


def tresais(string) :
    print("Sākotnējais teksts ir", string)
    print("Tikai pāra indeksa burti")
    for i in range(0, len(string), 2):
        print (string[i])
    return

# tresais("pynative")


def ceturtais(string2, n) :
    print ("Teksts:", string2)
    print ("Noņemot pirmos", n, "burtus sanāk:", string2[n:])

# ceturtais("pynative", 2)


def piektais(list) :
    print("Dotais saraksts", list)
    print("Rezultāts ir", list[0] == list[-1])
    return


skaitli1 = [10, 20, 30, 40, 10]
skaitli2 = [75, 65, 35, 75, 30]

piektais(skaitli2)