from datetime import date

from distance_earth_venus import distance_earth_venus
from angle_sun_earth_venus import angle_sun_earth_venus
from angle_sun_venus_earth import angle_sun_venus_earth
from angle_venus_sun_earth import angle_venus_sun_earth
from date_between_the_last_inferior_conjunction import date_between_the_last_inferior_conjunction

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
        processing = distance_earth_venus() 
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