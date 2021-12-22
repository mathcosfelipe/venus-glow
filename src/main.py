from datetime import date

from distance_earth_venus import distance_earth_venus
from angle_sun_earth_venus import angle_sun_earth_venus
from angle_sun_venus_earth import angle_sun_venus_earth
from angle_venus_sun_earth import angle_venus_sun_earth
from date_between_the_last_inferior_conjunction import date_between_the_last_inferior_conjunction

error = 0

psi = 0.0 
phi = 0.0 
theta = 0.0 
tau = 0.0 
upsilon = 0.0

beta = 10.81
gama = 14.95

ultimacinf = date(2020, 6, 3) 
proximacinf = date(2022, 1, 8)
datacsup = date(2021, 3, 22)

t = 0

date_a = 0
date_b = 0

inferior_conjunction_a = 0
inferior_conjunction_b = 0
superior_conjunction_a = 0
inferior_conjunction_b = 0
max_conjunction_a = 0
max_conjunction_b = 0

def main():

    while True:
        try:
            information = int(input('Wich information do you have? \n 1) distance Earth-Venus \n 2) angle Sun-Earth-Venus \n 3) angle Sun-Venus-Earth \n 4) angle Venus-Sun-Earth \n 5) date between the last inferior conjunction (2020-06-03) and the next (2022-01-08) \n Input the corresponding number: '))
        except:
            print('Invalid option. Try again.')
        else:
            if information < 1 or information > 5:
                print('Invalid option. Try again.')
            else:
                break

    if information == 1:
        distance_earth_venus(psi, phi, theta, tau, upsilon, beta, gama)
    elif information == 2:
        angle_sun_earth_venus()
    elif information == 3:
        angle_sun_venus_earth()
    elif information == 4:
        angle_venus_sun_earth()
    else:
        date_between_the_last_inferior_conjunction()

main()