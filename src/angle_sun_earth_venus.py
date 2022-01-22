import math
from datetime import timedelta

def angle_sun_earth_venus(psi, phi, theta, tau, upsilon, beta, gama, date_a, date_b, last_inferior_conjunction, next_inferior_conjunction, date_superior_conjunction, inferior_conjunction_a, inferior_conjunction_b, superior_conjunction_a, superior_conjunction_b, max_conjunction_a, max_conjunction_b):

    error = None

    while True:
        try:
            psi = float(input("Inform the value of angle Sun-Earth-Venus, in radians, with the maximum 15 decimal places: "))
        except:
            print('Error! Invalid value. Inform a float number. Try again.')
        else:
            break

    if psi == 0:
        error = 'conj'
    elif psi == 3.141592653589793:
        error = 3.1
    elif psi > 3.141592653589793:
        error = 3
    elif psi > 0.8082463510273271:
        error = 4
    elif psi < 0:
        error = 3.2
    else:
        a = 1
        upsilon = - 2 * gama * (math.cos(psi))
        c = pow(gama, 2) - pow(beta, 2)
        delta = (pow(upsilon, 2)) - (4 * a * c) 
        ra = ((- upsilon + pow(delta, 0.5)) / (2 * a))
        rb = (( - upsilon - pow(delta, 0.5)) / (2 * a))
        phi = (math.acos((pow(ra, 2) + pow(beta, 2) - pow(gama, 2)) / (2 * ra * beta)))
        theta = (math.acos((pow(beta, 2) + pow(gama, 2) - pow(ra, 2)) / (2 * beta * gama)))
        pa = ((0.5 * ( 1 + math.cos(phi))) * 100)
        ba = ((2 * beta * ra + pow(ra, 2) + (beta, 2) - pow(gama, 2)) / pow(ra, 3))
        ta = (theta / 0.010758878950649977)
        ta = round(ta, 0)
        data_a = last_inferior_conjunction + timedelta(days = ta) 
        data_b = next_inferior_conjunction - timedelta(days = ta)
        inferior_conjunction_a = 584 - ta
        inferior_conjunction_b = ta
        superior_conjunction_a = 292 - ta
        superior_conjunction_b = 292 + ta

        if ta < 36: 
            max_conjunction_a = 36 - ta
            max_conjunction_b = 36 + ta
            today = None
        elif ta > 36: 
            max_conjunction_a = 584 - 36 - 36 - ta 
            max_conjunction_a = ta - 36
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