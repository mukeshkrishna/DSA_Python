# using hashing

def countingSort(myList):
    
    # find the max number int he list
    largest = -1
    for i in range(len(myList)):
       if(myList[i]>largest):
           largest = myList[i]
    
    # create a dynamic array/list with largest
    freq = [0]*(largest+1)
    
    # map the elements from myList into freq
    
    for ele in myList:
        freq[ele] +=1
    
    # update the myList with the sorted values
    j = 0 # for iterating over myList
    i = 0
    while(i<=largest):
        while(freq[i]>0):
            myList[j] = i
            freq[i] -=1
            j +=1
        i += 1
    return myList

        


if(__name__=="__main__"):
    myList = [5,4,2,3,1]
    print(countingSort(myList))