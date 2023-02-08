# Tickets numbered 1 to 20 are mixed up and then a ticket is drawn at random. What is the probability that the ticket drawn has a number which is a multiple of 3 or 5?
"""
def probability(total,P_of):
    return f"{round((P_of/total)*100,2)} %"

factor=set()
for x in range(1,21):
    if x%3==0 or x%5==0:
        factor.add(x)

print("Probability = ",probability(20,len(factor)))
"""
# A bag contains 2 red, 3 green and 2 blue balls. Two balls are drawn at random. What is the probability that none of the balls drawn is blue?

def factorial(num):
    if num<=0:return 1
    return factorial(num-1)*num
#Total no of chances to draw 2 balls at random from 7 coloured balls,
def none_of_the_balls(total,drawn):
    return factorial(total)/(factorial(total-drawn)*drawn)
n=none_of_the_balls(7,2)
#let E be an event to draw 2 balls other than blue.
#Number of chances to draw two balls other than blue are,
def number_of_chances():
    pass

print((factorial(2)/(factorial(0)*factorial(2)))+(factorial(3)/(factorial(1)*factorial(2)))+(factorial(2)/(factorial(1)*factorial(1)))*(factorial(3)/(factorial(1)*factorial(2)))/n)

# In a box, there are 10 red, 7 blue and 6 green balls. One ball is picked up randomly. What is the probability that it is neither blue nor green?
print(10/23)