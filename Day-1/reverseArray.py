
myList = [1,2,3,4,5,6,7,10]

def reverseArray(myList):
    newlist = list()
    n = len(myList)-1
    while(n>=0):
        newlist.append(myList[n])
        n-=1
    return newlist

def reverseArraySwap(myList):
    i = 0 
    j =  len(myList) - 1
    while(i<=j):
        tmp = myList[i]
        myList[i] = myList[j]
        myList[j] = tmp
        i +=1
        j -=1
    
if(__name__=="__main__"):
    print(reverseArray(myList))
    reverseArraySwap(myList)
    print(myList)