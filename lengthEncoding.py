

def lengthEncoding(s):
    n = 0
    length = len(s)
    for i in range(length):
        if(i!=length-1):
            if(s[i] != s[i+1]):
                n += 1
                print(s[i],end="")
                if(n>1):
                    print(n,end="")
                n = 0
            else:
                n += 1
        else:
            if(s[i-1] == s[i] and n>1):
                n +=1
                print(s[i],end="")
                print(n,end="")    

if(__name__=="__main__"):
    s = "aaaabbcccccdeeee"
    lengthEncoding(s)