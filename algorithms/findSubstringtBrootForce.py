def findSubstrings(words, parts):
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    for i in range(0,len(parts)):
        
        if len(parts[i]) == 1:
            l1.append(parts[i])
        elif len(parts[i]) == 2:
            l2.append(parts[i])
        elif len(parts[i]) == 3:
            l3.append(parts[i])
        elif len(parts[i]) == 4:
            l4.append(parts[i])
        else:
            l5.append(parts[i])
    print(l3)
    flag = False
    for i in range(0,len(words)):
        flag = False
        if len(words[i]) >4:
            for j in range(0,len(words[i])-4):
                flag = False
                for k in range(0,len(l5)):
                    flag = True
                    for l in range(0,5):
                        if l5[k][l] != words[i][j+l]:
                            flag = False
                    if flag == True:
                        words[i] = words[i][:j] + "[" + words[i][j:j+5] + "]" + words[i][j+5:]
                        break
                if flag == True:
                    break
            if flag == True:
                continue
        flag = False
        if len(words[i]) >3:
            
            for j in range(0,len(words[i])-3):
                flag = False
                for k in range(0,len(l4)):
                    flag = True
                    for l in range(0,4):
                        if l4[k][l] != words[i][j+l]:
                            flag = False
                    if flag == True:
                        words[i] = words[i][:j] + "[" + words[i][j:j+4] + "]" + words[i][j+4:]
                        break
                if flag == True:
                    break
            if flag == True:
                continue
        flag = False
        if len(words[i]) >2:
            
            for j in range(0,len(words[i])-2):
                flag = False
                for k in range(0,len(l3)):
                    flag = True
                    for l in range(0,3):
                        if l3[k][l] != words[i][j+l]:
                            flag = False
                    if flag == True:
                        words[i] = words[i][:j] + "[" + words[i][j:j+3] + "]" + words[i][j+3:]
                        break
                if flag == True:
                    break
            if flag == True:
                continue
        flag = False
        if len(words[i]) >1:
            for j in range(0,len(words[i])-1):
                flag = False
                for k in range(0,len(l2)):
                    flag = True
                    for l in range(0,2):
                        if l2[k][l] != words[i][j+l]:
                            flag = False
                    if flag == True:
                        words[i] = words[i][:j] + "[" + words[i][j:j+2] + "]" + words[i][j+2:]
                        break
                if flag == True:
                    break
            if flag == True:
                continue
        flag = False
        if 1==1:
            for j in range(0,len(words[i])):
                flag = False
                for k in range(0,len(l1)):
                    flag = True
                    for l in range(0,1):
                        if l1[k] != words[i][j+l]:
                            flag = False
                    if flag == True:
                        words[i] = words[i][:j] + "[" + words[i][j:j+1] + "]" + words[i][j+1:]
                        break
                if flag == True:
                    break
    return words
            
