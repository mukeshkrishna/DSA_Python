
myList = [1,2,3,4,5,6]

def printingPairs(myList):
    i = 0 
    n = len(myList) - 1
    while(i<=n):
        j = i + 1
        while(j<=n):
            print("({0},{1})".format(myList[i],myList[j]),end=" ")
            j +=1
        print()
        i +=1

if(__name__=="__main__"):
    printingPairs(myList)
