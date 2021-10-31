
def largestString():
    n = int(input("number of times to enter input string: "))
    largest_length = 0
    largest_string = ""
    while(n>0):
        s = input()
        length = len(s)
        if(length>largest_length):
            largest_length = length
            largest_string = s
        n -= 1
    return "largest string is  == > {0} == {1}".format(largest_string,largest_length)   
if(__name__=="__main__"):
    print(largestString())