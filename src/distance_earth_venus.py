import math
from datetime import timedelta
from datetime import date

def distance_earth_venus():
    
    today = None
    error = 0

    psi = 0.0 
    phi = 0.0 
    theta = 0.0 
    tau = 0.0 
    upsilon = 0.0

    beta = 10.81
    gama = 14.95

    last_inferior_conjunction = date(2020, 6, 3) 
    next_inferior_conjunction = date(2022, 1, 8)
    date_superior_conjunction = date(2021, 3, 22)

    t = 0

    date_a = 0
    date_b = 0

    inferior_conjunction_a = 0
    inferior_conjunction_b = 0
    superior_conjunction_a = 0
    superior_conjunction_b = 0
    max_conjunction_a = 0
    max_conjunction_b = 0
    
    while True:
        try:
            distance_earth_venus = float(input('Input the value of distance between Earth and Venus, in Kilometers: '))
        except:
            print('Invalid value. Inform a float number.')
        else:
            break

    distance_earth_venus = (distance_earth_venus / pow(10, 7))

    if distance_earth_venus == 25.76:
        error = 'conjsup'
    elif distance_earth_venus > 25.76:
        error = 2
    elif distance_earth_venus == 4.14:
        error = 'conjinf'
    elif distance_earth_venus < 4.14:
        error = 2
    else:
        psi = math.acos((pow(distance_earth_venus, 2) + pow(gama, 2) - pow(beta, 2)) / 2 * distance_earth_venus * gama)
        phi = math.acos((pow(distance_earth_venus, 2) + pow(beta, 2) - pow(gama, 2) / 2 * distance_earth_venus * gama))
        tau = (0.5 * (1 + math.cos(phi))) * 100
        upsilon = (2 * beta * pow(2 * distance_earth_venus, 2) + pow(beta, 2) - pow(gama, 2)) / (pow(distance_earth_venus, 3))
        t = (theta / 0.010758878950649977)
        t = round(t, 0)
        date_a = last_inferior_conjunction + timedelta(days = t)
        date_b = next_inferior_conjunction - timedelta(days = t)
        inferior_conjunction_a = (584 - t)
        inferior_conjunction_b = t
        superior_conjunction_a = (292 - t)
        superior_conjunction_b = (292 + t)
        
        if t < 36:
            max_conjunction_a = (36 - t)
            max_conjunction_b = (36 + t)
        elif t > 36:
            max_conjunction_a = (584 - 72 - t)
            max_conjunction_b = (t - 36)
            today = None
        else:
            max_conjunction_a = (584 - 72)
            max_conjunction_b = (72)
            today = 'Today is day of maximum brightness'

        result = {
            "error": error,
            "today": today
        }

        return result