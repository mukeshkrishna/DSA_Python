# for sorted list/array

myList = [1,2,3,4,5,6,7,10]
key = 9

def binarySearch(myList,key):
    left = 0
    right = len(myList)-1
    
    while(left<=right):
        median = left + (right-left)//2
        if(myList[median] == key):
            return median
        elif(myList[median]<key):
            left = median+1
        elif(myList[median]>key):
            right = median -1
    return -1

if(__name__=="__main__"):
    print(binarySearch(myList,key))
    