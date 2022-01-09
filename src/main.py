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

    processing = None

    if information == 1:
        processing = distance_earth_venus(psi, phi, theta, tau, upsilon, beta, gama, date_a, date_b, last_inferior_conjunction, next_inferior_conjunction, date_superior_conjunction, inferior_conjunction_a, inferior_conjunction_b, superior_conjunction_a, superior_conjunction_b, max_conjunction_a, max_conjunction_b) 
    elif information == 2:
        processing = angle_sun_earth_venus()
    elif information == 3:
        processing = angle_sun_venus_earth()
    elif information == 4:
        processing = angle_venus_sun_earth()
    else:
        processing = date_between_the_last_inferior_conjunction()

    print(processing)

main()