

def selectionSort(myList):
    i = 0
    n = len(myList) - 1
    while(i < n):
        low = myList[i]
        for j in range(i+1,n+1):
            if(low>myList[j]):
                low = myList[j]
                index = j
        myList[index],myList[i] = myList[i],low
        i += 1
    return myList    
            

if(__name__=="__main__"):
    myList = [5,3,4,2,1]
    print(selectionSort(myList))