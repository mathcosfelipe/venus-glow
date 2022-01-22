from copy import error
import math
from datetime import timedelta

def angle_venus_sun_earth(psi, phi, theta, tau, upsilon, beta, gama, date_a, date_b, last_inferior_conjunction, next_inferior_conjunction, date_superior_conjunction, inferior_conjunction_a, inferior_conjunction_b, superior_conjunction_a, superior_conjunction_b, max_conjunction_a, max_conjunction_b):

    error = None
    today = None
    
    while True:
        try:
            theta = float(input("Input the value of the Venus-Sun-Earth angle, in radians (up to 15 decimal places, and 3.141592653589793 for π (180°)): "))
        except:
            print("Invalid value. Try again!")
        else:
            break

    if theta == 3.141592653589793:
        error = "conjsup"
    elif theta == 0:
        error = "conjinf"
    elif theta > 3.141592653589793:
        error = 3
    elif theta < 0: 
        error = 3.2
    else: 
        r = (math.sqrt(pow(beta, 2) + pow(gama, 2) - 2 * beta * gama * (math.cos(theta))))
        psi = (math.acos((pow(gama, 2) + pow(r, 2) - pow(beta, 2)) / (2 * gama * r)))
        phi = (math.acos((r**2+s**2-S**2)/(2*r*s)))
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
        else:
            cmax1 = (584-36-36)
            cmax2 = (36+36)
            hoje = "Hoje é dia de brilho máximo! "