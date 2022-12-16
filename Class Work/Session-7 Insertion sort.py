
#Sample code for insertion sort

# Insertion sort 


sampleLst = [4,2,6,1,0,9,3]

for i in range(1 , len(sampleLst)):
    key = sampleLst[i]
    j = i-1
    while j >= 0 and key < sampleLst[j] :
        sampleLst[j+1] = sampleLst[j]
        j -= 1
    sampleLst[j+1]= key 

print(sampleLst)




"""
Juhi wants to save the contact number of her friends on her mobile phone so she created a list of her friends 
with numbers. She decided to sort the list in alphabetical order first then save the number. Write a program 
in python to sort a list using insertion sort.
"""
def sortIt(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1   
        while j>=0 and key<lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst


slist = ["Moksha", "Vishesh", "Joe", "Robbie", "Panth", "Sahaij"]
srt = sortIt(slist)
print(srt)



"""
A school teacher was writing different words on the board in random order. Then he told the students to write the words in the correct order as written in the dictionary. Write a python program and use the insertion sort algorithm to sort the list of words. Then print all the words of the list in the correct order.
"""
def sortit(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j>=0 and key<lst[j]:
            lst[j+1] = lst[j]
            j-=1
        lst[j+1] = key
    return lst


slist = ["one","two","three","four","five","six","seven","eight","nine","ten"]
sortd = sortit(slist)
print(sortd)

