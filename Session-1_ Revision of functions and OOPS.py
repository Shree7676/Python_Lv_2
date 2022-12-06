#In-class exercise
"""
Shubham wants to know the current mileage ( distance traveled in km in 1 ltr of petrol )
of his car and for that decided to create a function in python where he can pass distance
traveled by his car and amount of petrol consumed by the car.
"""

def checkMilage(distance,petrolUsed):
    mileage = distance/petrolUsed
    return mileage 


distance = int(input("Enter the distance"))
petrolUsed = int(input("Enter the petrol used"))

mileage = checkMilage(distance,petrolUsed)
print(mileage)

"""
Sharma loves to travel in different countries and he uses different currencies in different countries. 
Sometimes he gets confused related to the conversion of the money. So to help Sharma write a program in python
with functions that can take three parameters: amount, from_currency ( currency that has to be converted ), 
to_currency ( Currency in which it has to be converted). The function should return the amount after conversion.
The program should contain at least four different types of currencies.
"""
conversionCurrency = {
    "rupees" : {
        "dollars" : 1/80,
        "pounds" : 1/96,
        "euros" : 1/82
    },
    "dollars" : {
        "rupees" : 80,
        "pounds" : 5/4,
        "euros:" : 51/50
    },
    "pounds" : {
        "rupees" : 96,
        "dollars" : 4/5,
        "euros" : 1.17,
    },
    "euros" : {
        "rupees" : 82,
        "dollars" : 50/51,
        "pounds" : 0.85
    }

}

def convertCurrency(amount, from_currency, to_currency):
    for i in conversionCurrency.keys():
        if i == from_currency:
            for j in conversionCurrency[i].keys():
                if j == to_currency:
                    ratio = conversionCurrency[i][j]
                    converted_ammount = amount*ratio
                    return converted_ammount, to_currency


convertedAmount = convertCurrency(96, "rupees", "pounds")
convertedAmount = str(convertedAmount[0]) + " " + convertedAmount[1]
print(convertedAmount)

"""
Anil wants to calculate the tax to be paid on his earnings. 
He doesn’t remember the amount charged on the earnings. 
So he decided to create a program in python with functions to 
calculate the tax to be paid on his earnings. He collected the 
information and started creating the program and now he is happy to use the calculator. 
Create the same kind of program so that you can use it in the future.
"""


"""
Chris loves open-world games. He wants to create an open-world game 
in python where initially he wants to put random vehicles like trucks, cars, 
vans, ambulances, police cars, SUVs, taxis, etc. on the street. He decided to 
create a class vehicle and then different child classes for different types of vehicles. 
Help Chris in doing the same.
"""

