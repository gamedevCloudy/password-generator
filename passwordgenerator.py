import random as r
def generate(length, hasCaps, hasSmall,hasNums, hasUnique, minNum,minUnique):
    
    #generate an array filled with all letters
    passwd= [""]*length

    if hasCaps and hasSmall:
        for i in range(length): 
            x=r.randint(65,90)
            y=r.randint(97,122)
            chance=[x,x,y,y,y] 
            #60% small letter 40% capital
            
            ch=r.randint(0,4)
            passwd[i]= chr(chance[ch])
    
    elif hasCaps and not hasSmall: 
        #onlycaps
        for i in range(length): 
            x=r.randint(65,90)
            passwd[i]= chr(x)
    
    elif hasSmall and not hasCaps: 
        #onlysmall
        for i in range(length): 
            x=r.randint(97,122)
            passwd[i]= chr(x)
    else: 
        print("No letters nigga? you should have combination of letters and numbers.")
        exit(0)
    

    if(hasNums):
        minNum=minNum+r.randint(0,length//5)
        for i in range(minNum):
            pos = r.randint(0,length-1)
            passwd[pos]= str(r.randint(0,9))
    if(hasUnique):
        minUnique=minUnique+r.randint(0,length//5)
        unique ='!@#$%^&*'

        for i in range(minUnique):
            pos = r.randint(0,length-1)

            while(passwd[pos] in "0123456789"):
                pos = r.randint(0,length-1)
            passwd[pos]= unique[r.randint(0,7)]

    password=''
    for i in passwd: 
        password+=i
    print(password)
    return password

for i in range(10): 
    generate(14, True,True,True,True, 1,1)
    generate(14, False,False,True,True, 1,1)
