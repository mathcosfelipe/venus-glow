import math

def distance_earth_venus(psi, phi, theta, tau, upsilon, beta, gama):
    
    while True:
        try:
            distance_earth_venus = float(input('Input the value of distance between Earth and Venus, in Kilometers: '))
        except:
            print('Invalid value. Inform a float number.')
        else:
            break

    distance_earth_venus = distance_earth_venus / 10 ** 7
    psi = (math.acos((distance_earth_venus ** 2 + gama ** 2 - beta ** 2) / (2 * distance_earth_venus * gama)))
    phi = (math.acos((distance_earth_venus ** 2 + beta ** 2 - gama ** 2) / (2 * distance_earth_venus * beta)))
    theta = (math.acos((beta ** 2 + gama ** 2 - distance_earth_venus ** 2) / (2 * beta * gama)))
