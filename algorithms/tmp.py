def swapLexOrder(str, pairs):
    
    str2 = list(str)
    
    while(len(pairs)!=0):
        
        stack = 1
        dic  = {}
        dic[pairs[0][0]] = 1
        dec = {}
        dec[pairs[0][0]] = 1
    
        while(stack != 0):
            stack = 0
            i = 0
            dell = list(dic.keys())
            while(i!=len(pairs)):
                
                if(pairs[i][0] in dic):
                    dic[pairs[i][1]] = 1
                    dec[pairs.pop(i)[1]] = 1
                    stack +=1
                    i= i-1
                elif(pairs[i][1] in dic):
                    dic[pairs[i][0]] = 1
                    dec[pairs.pop(i)[0]] = 1
                    
                    stack +=1
                    i= i-1
                i += 1
            for j in range(0,len(dell)):
                del dic[dell[j]]
        klist = list(dec.keys())
        
        klist.sort()
        charlist = []
        for i in range(0,len(klist)):
            charlist.append(str[klist[i]-1])
        
        charlist.sort()
        charlist.reverse()
        
        for i in range(0,len(klist)):
            str2[klist[i]-1] = charlist[i]
            
    return ''.join(str2)

