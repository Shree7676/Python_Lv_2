#Sample code for bubble sort 

sampleList = [3,5,99999,15,48,2,69,420]
for i in range(len(sampleList)-1):
    for j in range((len(sampleList)-1)-i):
        if sampleList[j]>sampleList[j+1]:
            sampleList[j], sampleList[j+1] = sampleList[j+1], sampleList[j]
print(sampleList)

#Sample code for selection sort 

# Selection sort 

sampleLst = [4,2,6,1,0,9,3]

for i in range(len(sampleLst)):
    smallest = i 
    for j in range( i+1 , len(sampleLst)) :
        if sampleLst[j] < sampleLst[smallest] :
            smallest = j 
    sampleLst[i] , sampleLst[smallest] = sampleLst[smallest] , sampleLst[i]

print(sampleLst)

"""
Abhinav is the sports captain of his school. He is selecting players for the different sports. He made a list of players and also he has to assign the chest number to each player in alphabetical order of their names. To simplify the work of Abhinav write a program in python where you can append the names of the players inside a list. Then sort the entire list using the bubble sort algorithm. Then by using the index number of the list, assign the chest number to each player. 
Hint: The chest number of the players is index + 1 of the list.
"""
players = []
numberOfStudents = int(input("How many students do you have"))
for i in range(numberOfStudents):
    player = input("Enter the name of the player:")
    players.append(player)

for i in range(len(players)-1):
    for j in range(len(players)-1-i):
        if players[j] > players[j+1]:
            players[j], players[j+1] = players[j+1], players[j]

for i in range(len(players)):
    print(i +1, players[i])


"""
Rahul and his friends were measuring their heights in random order. They created the list of heights of all the students. Rahul wanted to know the range of the height in his class.  i.e lowest height, biggest height, and the difference between lowest height and biggest height. Write a python program to get the answer.
Hint: Create a list. Enter all the heights inside the list in any order. Apply selection sort algorithm and arrange it in ascending order. Then the first element of the list will be the lowest height, the last element of the list will be the biggest height and the difference between these two values will be the range.
"""
heights = [110,130,160,100,120,140,190]

for i in range(len(heights)):
    lowest = i 
    for j in range(i+1,len(heights)):
        if heights[j] < heights[lowest]:
            lowest = j
    heights[i], heights[lowest] = heights[lowest], heights[i]

print("Lowest height:",heights[0]) 
print("Tallest height:",heights[-1]) 
print("Range:",heights[-1]-heights[0])


