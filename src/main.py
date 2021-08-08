import math
import datetime
from datetime import date
from datetime import timedelta

s = 10.81
S = 14.95
r = 0
psi = 0
phi = 0
theta = 0
p = 0
b = 0

ultimacinf = date(2020, 6, 3) 
proximacinf = date(2022, 1, 8)
datacsup = date(2021, 3, 22)

t = 0
data1 = 0
data2 = 0
cinf1 = 0
cinf2 = 0
csup1 = 0
csup2 = 0
cmax1 = 0
cmax2 = 0

erro = 0

def main():
    
    while True:
        try:
            informacao = int(input("De qual informação você dispõe? \n1) distância Terra-Vênu \n2) ângulo Sol-Terra-Vênus \n3) ângulo Sol-Vênus-Terra \n4) ângulo Vênus-Sol-Terra \n5) data - entre a última conjunção inferior (03 de junho de 2020) e a próxima (08 de janeiro de 2022) \nDigite apenas o número correspondente: "))
        except:
            print("Erro! Opção inválida.")
        else:
            if informacao < 0 and informacao > 5:
                print("Erro! Opção inválida.")
            else:
                break

    if informacao == 1: 
        r = float(input("Entre com o valor da distância Terra-Vênus, em quilômetros: "))
        r = (r/(10**7))
        if r == 25.76:
            erro = "conjsup"
        elif r > 25.76:
            erro = 2
        elif r == 4.14:
            erro = "conjinf"
        elif r < 4.14:
            erro = 2
    else:
        psi = (math.acos((r**2+S**2-s**2)/(2*r*S)))
        phi = (math.acos((r**2+s**2-S**2)/(2*r*s)))
        theta = (math.acos((s**2+S**2-r**2)/(2*s*S)))
        p = (0.5*(1+math.cos(phi)))*100
        b = ((2*s*r+r**2+s**2-S**2)/r**3)
        t = (theta/0.010758878950649977)
        t = round(t,0) 
        data1 = ultimacinf + timedelta(days = t)
        data2 = proximacinf - timedelta(days = t)
        cinf1 = (584-t)
        cinf2 = (t)
        csup1 = (292-t)
        csup2 = (292+t)
        if t < 36: 
            cmax1 = (36-t)
            cmax2 = (36+t)
            hoje = ""
        elif t > 36: 
            cmax1 = (584-36-36-t) 
            cmax2 = (t-36)
            hoje = ""
        else: #t = 36
            cmax1 = (584-36-36)
            cmax2 = (36+36)
            hoje = "Hoje é dia de brilho máximo! "            

main()