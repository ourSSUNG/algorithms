def swapLexOrder(str, pairs):
    
    
    while(len(pairs)!=0):
        
    
        stack = 1
        dic  = {}
        dic[pairs[0][0]] = 1
    
        while(stack != 0):
            stack = 0
            i = 0
            while(i!=len(pairs)):
                if(pairs[i][0] in dic):
                    dic[pairs[i][1]] = 1
                    del pairs[i]
                    i = i -1
                    stack = stack + 1
                elif(pairs[i][1] in dic):
                    dic[pairs[i][0]] = 1
                    del pairs[i]
                    i = i - 1
                    stack = stack + 1
                i = i + 1
        klist = list(dic.keys())
        
        
        klist.sort()
        charlist = []
        for i in range(0,len(klist)):
            charlist.append(str[klist[i]-1])
        charlist.sort()
        charlist.reverse()
        
        
        for i in range(0,len(klist)):
            str = str[:klist[i]-1] + charlist[i] + str[klist[i]:]
            
        
    return str
