from time import sleep
from sys import exit

def equation(grid):
    return grid / 2 + 12

def roundup(load):
    if load >= 750:
        load = 750
        return load
    else:
        return load

def loop():
    while True:
        try:
            demand = int(input("insert grid demand: "))
            if demand > 1500:
                print("demand cant go over 1500")
            elif demand < 950:
                print("demand cant go below 950")
            else:
                load = equation(demand)
                break
        except ValueError:
            print("enter a number")
    return roundup(load)

last_load = int(loop())
print(f"turbine A&B auto bypass setpoint: {last_load}")
sleep(1)

while True:
    try:
        next_step = int(input("\n"
            "type 1 to calculate again\n"
            "type 2 to close program\n"
            "\n"))
        if next_step == 1:
            last_load = int(loop())
            print(f"turbine A&B auto bypass setpoint: {last_load}")
            sleep(1)
        elif next_step == 2:
            print(f"turbine A&B auto bypass setpoint: {last_load}")
            break
        else:
            print("command not found. try again")
    except ValueError:
        print("enter a number")

sleep(5)
exit()