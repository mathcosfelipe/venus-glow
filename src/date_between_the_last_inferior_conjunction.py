import math
import datetime

def date_between_the_last_inferior_conjunction():

    today = None
    error = 0

    psi = 0.0 
    phi = 0.0 
    theta = 0.0 
    tau = 0.0 
    upsilon = 0.0

    beta = 10.81
    gama = 14.95

    last_inferior_conjunction = datetime.date(2020, 6, 3) 
    next_inferior_conjunction = datetime.date(2022, 1, 8)
    date_superior_conjunction = datetime.date(2021, 3, 22)

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
        phi = (math.acos((pow(r, 2) + pow(beta, 2) - pow(gama, 2)) / (2 * r * beta)))
        tau = ((0.5 * (1 + math.cos(phi))) * 100) 
        beta = ((2 * beta * r + pow(r, 2) + pow(beta, 2) - pow(gama, 2)) / pow(r, 3))
        date = date
        inferior_conjunction = 584 - t
        if t < 292: 
            superior_conjunction = 292 - t
        else:
            superior_conjunction = 876 - t
        if t == 36: 
            max_conjunction = 512
            today = "Today is day of maximum brightness"
        elif t == 548: 
            cmax = 72
            today = "Today is day of maximum brightness"
        elif t < 36: 
            max_conjunction = (36-t)
            today = None
        else:
            max_conjunction = 584 - 36 - 36 - t 
            today = None

        result = {
            "error": error,
            "today": today
        }

        return result