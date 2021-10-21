
myList = [1,2,3,4,5,6]


def subArray(myList): 
    i = 0 
    n = len(myList) - 1
    while(i<n):
        j = i + 1
        print(myList[i:i+1],end= "")
        while(j<=n):
            print(myList[i:j+1],end="")
            j +=1
        print()
        i +=1
            

if(__name__=="__main__"):
    subArray(myList)