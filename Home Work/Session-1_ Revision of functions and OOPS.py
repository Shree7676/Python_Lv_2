# Home Work

"""
Anil wants to calculate the tax to be paid on his earnings. 
He doesn’t remember the amount charged on the earnings. 
So he decided to create a program in python with functions to 
calculate the tax to be paid on his earnings. He collected the 
information and started creating the program and now he is happy to use the calculator. 
Create the same kind of program so that you can use it in the future.
"""

def Tax_calculator(amount,tax_rate):
    return amount*(tax_rate/100)

amt=int(input("What is your salary"))
tax=int(input("what is the tax rate "))

a=Tax_calculator(amt,tax)
print(f"Your tax amount is {a}")

"""
Chris loves open-world games. He wants to create an open-world game 
in python where initially he wants to put random vehicles like trucks, cars, 
vans, ambulances, police cars, SUVs, taxis, etc. on the street. He decided to 
create a class vehicle and then different child classes for different types of vehicles. 
Help Chris in doing the same.
"""

class vehicle:
    def __init__(self,brand,colour):
        self.brand=brand
        self.colour=colour
        self.tyre=4
        self.headlight="OFF"
        self.engine="OFF"

    def start(self):
        self.engine = "ON"
        print("Engine Started")
    def stop(self):
        self.engine = "OFF"
        print("Engine Stoped")
    def headlight_ON(self):
        self.headlight = "ON"
        print("Engine Started")
    def headlight_OFF(self):
        self.headlight = "OFF"
        print("Engine Stoped")

class trucks(vehicle):
    def __init__(self,brand,colour):
        super(trucks, self).__init__(brand,colour)
        self.tyre=8

class cars(vehicle):
    pass

class police_cars(cars):
    def __init__(self,brand,colour):
        super(police_cars, self).__init__(brand,colour)
        self.siren="OFF"
        self.Beep=("RED","BLUE")
    def siren_ON(self):
        self.siren = "ON"
        print("'siren on' on high volume ")
    def siren_OFF(self):
        self.siren = "OFF"
        print("siren off")
    def Beep_ON(self):
        self.Beep = "ON"
        print("red blue light beep display...")
    def Beep_OFF(self):
        self.Beep = "OFF"
        print("red blue light stop blinking...")

class ambulances(police_cars):
    pass

#No check as per need in main pgm