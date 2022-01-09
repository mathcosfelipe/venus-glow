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
        pass