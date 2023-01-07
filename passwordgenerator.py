import random as r
def generate(length, hasCaps, hasSmall,hasNums, hasUnique, minNum,minUnique):
    
    #generate an array filled with all letters
    passwd= [""]*length

    if hasCaps and hasSmall:
        for i in range(length): 
            x=r.randint(65,90)
            y=r.randint(97,122)
            chance=[x,x,y,y,y] #60% small letter 40% capital
            ch=r.randint(0,4)
            passwd[i]= chr(chance[ch])
    elif hasCaps and not hasSmall: 
        for i in range(length): 
            x=r.randint(65,90)
            passwd[i]= chr(x)
    elif hasSmall and not hasCaps: 
        for i in range(length): 
            x=r.randint(97,122)
            passwd[i]= chr(x)
    

    if(hasNums):
        minNum=minNum+r.randint(0,length//5)
        for i in range(minNum):
            pos = r.randint(0,length)
            passwd[pos]= str(r.randint(0,9))
    if(hasUnique):
        minUnique=minUnique+r.randint(0,length//5)
        unique ='!@#$%^&*'

        for i in range(minUnique):
            pos = r.randint(0,length-1)
            while(passwd[pos] in "0123456789"):
                pos = r.randint(0,length-1)
            passwd[pos]= unique[r.randint(0,8)]

    print(passwd)
    password=''
    for i in passwd: 
        password+=i
    print(password)
    return password
generate(14, True,True,True,True, 1,1)