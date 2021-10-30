
# O(n^2)
def insertionSort(myList):

    j = 1
    n = len(myList) - 1
    while(j<=n):
        i = j - 1 
        key = myList[j]
        while(i>=0):
            if(key<myList[i]):
                myList[i+1],myList[i] = myList[i],myList[i+1]
            i -= 1
        j += 1            
    return myList                
                

            

if(__name__=="__main__"):
    myList = [5,3,4,1,2]
    print(insertionSort(myList))