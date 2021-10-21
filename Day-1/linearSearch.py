
val = [1,2,3,4,5,6,7,8,9]
key = 6

def linearSearch(val,key):
    for index,value in enumerate(val):
        if(value==key):
            return index
    return -1
if(__name__=="__main__"):
    print(linearSearch(val,key))
    