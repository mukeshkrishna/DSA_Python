
myList = [1,2,3,4,5,6]



def subArraySum(myList): 
    i = 0 
    n = len(myList) - 1
    sumList = dict()
    while(i<n):
        j = i + 1
        print(myList[i:i+1],end= "")
        sumList[str(myList[i:i+1])] = sum(myList[i:i+1])
        while(j<=n):
            print(myList[i:j+1],end="")
            sumList[str(myList[i:j+1])] = sum(myList[i:j+1])
            j +=1
        print()
        i +=1
    return sumList
        
def sum(mylist):
    sum = 0
    for i in mylist:
        sum = sum + i
    return sum

# BruteForce
def findLargestSum(mydict):
    largest = -1
    largestKey = None
    for key,value in mydict.items():
        if(largest<value):
            largest = value
            largestKey = key
    print("Largest value is {0}: {1}".format(largestKey,largest))

# Prefix Sum
def findLargestSumPrefix(myList):
    #prefix sums
    prefixSum = list()
    sum = 0
    for e in range(len(myList)):
        sum = sum + myList[e]
        prefixSum.append(sum)
    sumList = dict()    
    i = 0 
    n = len(myList) - 1
    largest = prefixSum[0]
    for e in prefixSum:
        if(e>largest):
            largest = e
            
    return largest
 
# Maximum subarry using kadane's algorithm

def maxSubArrayKandens(myList):
    currentSum = 0
    maxSum = 0
    for i in range(len(myList)):
        currentSum = currentSum + myList[i]
        if(currentSum<0):
            currentSum = 0
        maxSum = max(currentSum,maxSum)
    return maxSum 
    
if(__name__=="__main__"):
    findLargestSum(subArraySum(myList))
    print("largest Sum is {0}".format(findLargestSumPrefix(myList)))
    print("Max sum using kadane's is {0}".format(maxSubArrayKandens(myList)))