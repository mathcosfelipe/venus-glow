import math
from datetime import timedelta

def distance_earth_venus(psi, phi, theta, tau, upsilon, beta, gama, date_a, date_b, last_inferior_conjunction, next_inferior_conjunction, date_superior_conjunction, inferior_conjunction_a, inferior_conjunction_b, superior_conjunction_a, superior_conjunction_b, max_conjunction_a, max_conjunction_b):
    
    error = None
    today = None
    
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

        result = []

        if today != None:
            result.append(today)
        
        if error != None:
            result.append(error)

        if(len(result == 0)):
            return False
        else:
            return result
