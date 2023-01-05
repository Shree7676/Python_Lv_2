# Tickets numbered 1 to 20 are mixed up and then a ticket is drawn at random. What is the probability that the ticket drawn has a number which is a multiple of 3 or 5?

def probability(total,P_of):
    return f"{round((P_of/total)*100,2)} %"

factor=set()
for x in range(1,21):
    if x%3==0 or x%5==0:
        factor.add(x)

print("Probability = ",probability(20,len(factor)))

# A bag contains 4 red, 5 green and 2 blue balls. Two balls are drawn at random. What is the probability that none of the balls drawn is blue?


# In a box, there are 10 red, 7 blue and 6 green balls. One ball is picked up randomly. What is the probability that it is neither blue nor green?
