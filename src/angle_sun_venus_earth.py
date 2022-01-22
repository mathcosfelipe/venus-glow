import math
from datetime import timedelta

def angle_sun_venus_earth(psi, phi, theta, tau, upsilon, beta, gama, date_a, date_b, last_inferior_conjunction, next_inferior_conjunction, date_superior_conjunction, inferior_conjunction_a, inferior_conjunction_b, superior_conjunction_a, superior_conjunction_b, max_conjunction_a, max_conjunction_b):

    error = None
    today = None

    while True:
        try:    
            phi = float(input("Input the value of the Sun-Venus-Earth angle, in radians (up to 15 decimal places, and 3.141592653589793 for π (180°)): "))
        except:
            print("Invalid value. Try again!")
        else:
            break

    if phi == 3.141592653589793:
        error = "conjinf"
    elif phi == 0:
        error = "conjsup"
    elif phi > 3.141592653589793:
        error = 3
    elif phi < 0: 
        error = 3.2
    else: 
        psi = (math.asin(((math.sin(phi) * beta) / gama)))
        theta = (3.141592653589793-phi-psi)
        r = ((beta * math.sin(theta)) / math.sin(psi))
        tau = ((0.5 * (1 + math.cos(phi))) * 100)
        beta = ((2 * beta * r + pow(r, 2) + pow(beta, 2) - pow(gama, 2)) / pow(r, 3))
        t = (theta/0.010758878950649977)
        t = round(t,0)
        date_a = last_inferior_conjunction + timedelta(days = t)
        date_b = next_inferior_conjunction - timedelta(days = t)
        inferior_conjunction_a = 584 - t
        inferior_conjunction_b = t
        superior_conjunction_a = 292 - t
        superior_conjunction_b = 292 + t

        if t < 36: 
            max_conjunction_a = 36 - t
            max_conjunction_b = 36 + t
            today = None
        elif t > 36: 
            max_conjunction_a = 584 - 36 - 36 - t 
            max_conjunction_b = t - 36
            today = None
        else:
            max_conjunction_a = 584 - 36 - 36
            max_conjunction_b = 36 + 36
            today = 'Today is day of maximum brightness!'

        result = {
            "error": error,
            "today": today
        }

        return result