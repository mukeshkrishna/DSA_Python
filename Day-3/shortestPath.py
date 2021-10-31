# find the displacement from the largest given path

def shortestPath(path):
    x = 0
    y = 0
    
    for i in range(len(path)):
        if(path[i]=="N"):
            y += 1
        elif(path[i]=="S"):
            y -= 1
        elif(path[i]=="E"):
            x += 1
        elif(path[i]=="W"):
            x -= 1
    if(x>0 and y>0):
        while(x>0):
            print("E",end="")
            x -=1
        while(y>0):
            print("N",end="")
            y -=1
    elif(x>0 and y<0):
        while(x>0):
            print("E",end="")
            x -=1
        while(y<0):
            print("S",end="")    
            y +=1
    elif(x<0 and y>0):
        while(x<0):
            print("W",end="")
            x +=1
        while(y>0):
            print("N",end="")    
            y -=1          
    elif(x<0 and y<0):
        while(x>0):
            print("W",end="")
            x +=1
        while(y<0):
            print("S",end="")    
            y +=1            




if(__name__=="__main__"):
    path = "SNNNEWE"
    shortestPath(path)
