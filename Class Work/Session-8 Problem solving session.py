"""
Jia was organizing her files on the computer. She created a lot of subfolders and shifted files to different folders. Suddenly she wondered whether she can create a data structure very similar to the concept of folders or not. She wants to create a class Folder and wants to add methods like addNewFolder(), addNewFile(), deleteFolder(), and deleteFile(). Also, she wants some condition while creating the new subfolder and files. The datatype of new subfolder should be Folder and  a new file should contain a period(.) in the file name to indicate the extension. Create such data structure to help Jia. 
"""

class Folder:
    def __init__(self):
        self.dict={}

    def addNewFolder(self):
        n=input("Folder name: ")
        self.dict[n]=""

    def addNewFile(self):

        flag=True
        while flag:
            f = input("file name: ")
            while "." not in f:
                f = input("file name should contain the extension (.): ")
            file_name,folder_name=f.split(".")

            if folder_name in self.dict.keys():
                self.dict[folder_name] = file_name
                flag=False
            else:
                print(f"no such folder found named as {folder_name} \nPlease enter proper ",end="")

    def deleteFolder(self):
        n = input("Which Folder to remove: ")
        self.dict.pop(n)

    def deleteFile(self):
        n = input("Which File to remove: ")
        for x in self.dict:
            if self.dict[x]==n:
                self.dict[x]=""

#lets test
a=Folder()
a.addNewFolder()
a.addNewFolder()
a.addNewFile()
a.addNewFile()
print(a.dict)
a.deleteFolder()
a.deleteFile()
print(a.dict)

"""
Dhruv just learned the Bubble sort algorithm and recursion. As the bubble sort algorithm needs the repetitive process he thinks that the bubble sort algorithm can be developed using recursion instead of loop. He tried doing this but was not able to complete the program. Write a program in python for the bubble sort algorithm and use recursion to help Dhruv in solving the problem.
"""
def B_sort(arr,end,st):
    if end==0 or st==end-1:
        return

    if arr[st]>arr[st+1]:
        arr[st],arr[st+1]=arr[st+1],arr[st]

    B_sort(arr,end,st+1)
    B_sort(arr,end-1,st=0)

list=[5,2,6,3,7,4,6,7,2]
print(list)
B_sort(list,len(list),0)
print(list)

"""
Sakshi thought that if we can use recursion for the repetitive process then definitely we can create different shapes as well with the help of recursion instead of using nested loops. Sakshi's friend Mansa said it is impossible to print patterns with the help of recursion. To prove that printing the following patterns is possible with help of recursion write a python program.
"""

def Star_square(r,c,fix):

    if r==0:
        return

    if c==0:
        print()
        c=fix
        return Star_square(r-1, c,fix)

    print("*",end=" ")
    return Star_square(r,c-1,fix)

Star_square(5,10,10)

def Inverted_Star_Triangle(r,c,fix):

    if r==0:
        return
    if c==0:
        print()
        c=fix-1
        return Inverted_Star_Triangle(r-1, c,fix-1)
    print("*",end=" ")
    return Inverted_Star_Triangle(r,c-1,fix)
Inverted_Star_Triangle(5,4,4)

#or

def Inverted_Star_Tri(r):

    if r==0:
        return
    else:
        print("* " * r)
        Inverted_Star_Tri(r - 1)
Inverted_Star_Tri(5)


def Star_Triangle(r):
#pending
    if r==0:
        return
    else:
        Star_Triangle(r - 1)
        print("* "*r)
Star_Triangle(5)