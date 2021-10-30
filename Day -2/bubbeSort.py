

def bubbleSort(myList):
    i = 0
    j = 0
    n = len(myList)-1
    k = n
    while(i<n):
        while(j<k):
            if(myList[j]>myList[j+1]):
                myList[j],myList[j+1] = myList[j+1],myList[j]
            j += 1
        i += 1
        j = 0
        k -=1
    return myList 
if(__name__=="__main__"):
    myList = [5,3,6,3,1]
    print(bubbleSort(myList))