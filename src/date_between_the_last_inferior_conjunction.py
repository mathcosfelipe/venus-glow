import math
import datetime

def date_between_the_last_inferior_conjunction(psi, phi, theta, tau, upsilon, beta, gama, date_a, date_b, last_inferior_conjunction, next_inferior_conjunction, date_superior_conjunction, inferior_conjunction_a, inferior_conjunction_b, superior_conjunction_a, superior_conjunction_b, max_conjunction_a, max_conjunction_b):

    error = None
    today = None
   
    while True:
        try:
            year = int(input("Input the year: "))
        except:
            print("Invalid input. Try again")
        else:
            break

    while True:
        try:
            month = int(input("Input the month: "))
        except:
            print("Invalid input. Try again")
        else:
            break

    while True:
        try:
            day = int(input("Input the day: "))
        except:
            print("Invalid input. Try again")
        else:
            break

    date = datetime.date(year, month, day)

    if date > next_inferior_conjunction: 
        error = 5
    elif date == next_inferior_conjunction: 
        error = "conjinf_prox"
    elif date < last_inferior_conjunction: 
        error = 5
    elif date == last_inferior_conjunction:
        error = "conjinf_ult"
    elif date == last_inferior_conjunction:
        error = "conjsup_data"
    else:
        t = date - next_inferior_conjunction
        t = t.days
        if t < 292: 
            days = t
        else:
            days = 584 - t
        theta = 0.010758878950649977 * days
                          
                          
        r = (math.sqrt(pow(beta, 2) + pow(gama, 2) - 2 * beta * gama * (math.cos(theta))))
        psi = (math.acos((pow(gama, 2) + pow(r, 2) - pow(beta, 2)) / (2 * gama * r)))
        phi = (math.acos((r**2+s**2-S**2)/(2*r*s)))
        p = (0.5*(1+math.cos(phi)))*100 
        b = ((2*s*r+r**2+s**2-S**2)/r**3)
        data = date
        cinf = (584-t)
        if t < 292: 
            csup = (292-t)
        else:
            csup = (876-t)
        if t == 36: 
            cmax = 512
            hoje = "Hoje é dia de brilho máximo! "
        elif t == 548: 
            cmax = 72
            hoje = "Hoje é dia de brilho máximo! "
        elif t < 36: 
            cmax = (36-t)
            hoje = ""
        else:
            cmax = (584-36-36-t) 
            hoje = ""