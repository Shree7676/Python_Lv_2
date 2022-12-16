"""
Nidhi is working on a big project and she wants a getIndex(givenList , element) function. getIndex(givenList , element) function should return the index number of a value present inside a list of numbers and remove that value as well. She told her friend Himanshi to create this function. Also, Nidhi told she wants binary search algorithm to be used for this. Himanshi tried to create the function but she is not able to return the value. Write a program in python for the same to help Himanshi.
# Note: Use binary search algorithm to search the element in the list.
"""
def binarySearch(givenList , element):
    
    low = 0
    high = len(lst) - 1
    
    while ( high > low ):
        
        mid = (high+low)//2
        
        if element == givenList[mid]:
            return mid
        
        elif element > givenList[mid]:
            low = mid + 1
            
        else :
            high = mid - 1
            
    return -1 # Element not present
            

def getIndex(givenList , element):
    position = binarySearch(givenList , element)
    if position == -1 :
        return "Element not present"
    givenList.pop(position) 
    return position 


lst = [2,3,54,64,76,78,81,88,91]
element = 54

index = getIndex(lst , element)

print("Index value of element was : " , index)
print("New List : " , lst)




"""
Chirag is preparing for his board examinations. He is worried about his maths examination. He started noting down the topics that he has already covered. Soon the total number of topics covered by Chirag was more than 50. Now, whenever he wants to confirm whether he has covered any topic or not, it takes a lot of time to search it in a normal list. To save his time he thought of creating a program in python where he can give the input of covered topics that will get added to a list. And he also has one option in the program to search for the topic that will just say whether the entered topic is already covered or not. To search the topics he used a binary search algorithm. Write the same program to store the topics that you have covered in python then search the topics to check what you have covered and what is remaining. 
Note: 
Use binary search algorithm to search the topic.
Sort the list using sort() method everytime you add new topic.
( As binary search algorithm can be applied to only sorted list. )
"""
topics = [] # list of topics covered 


def checkTopic(topic):
    pass

    low = 0
    high = len(topics) - 1
    
    while ( high > low ):
        
        mid = (high+low)//2
        
        if topic == topics[mid]:
            return True
        
        elif topic > topics[mid]:
            low = mid + 1
            
        else :
            high = mid - 1
            
    return 0 # Element not present


while True:
    print("1 - Add new topic to list :")
    print("2 - Check for topic")
    print("3 - Display all topics ")
    print("4 - Exit program ")
    
    ch = int(input("Enter your choice : "))

    if ch == 1 :
        topic = input("Enter new topic : ")
        topics.append(topic)
        topics.sort()
        
    elif ch == 2 :
        topic = input("Enter a topic to check :")
        if checkTopic(topic):
            print("You have already covered given topic.")
        else:
            print("You still need to learn this")

    elif ch == 3 :
        print("Topics covered :")
        for i in topics :
            print(i)
            
    elif ch == 4 :
        print("Thank you!")
        break
    
    else:
        print("Invalid input")
 