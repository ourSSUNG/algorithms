class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def findSubstrings(words, parts):
    dic = {}
    dic[0] = []
    dic[1] = []
    dic[2] = []
    dic[3] = []
    dic[4] = []
    flag = False
    for i in range(0,len(parts)):
        k = len(parts[i])
        hasher = 0
        for j in range(0,k):
            hasher = hasher + ord(parts[i][j])
        dic[k-1].append([parts[i],hasher])
    treelist = []
    for i in range(0,5):
        treelist.append(treeMaker6(dic[i]))
    for i in range(0,len(words)):
        for m in range(0,5):
        
            if len(words[i])<5-m:
                continue
            
            sum2 = 0
            for j in range(0,5-m):
                sum2 = sum2 + ord(words[i][j])
            if BTSearch(treelist[4-m],sum2)==True:
                if dic[4-m].count([words[i][:5-m],sum2])!=0:
                    words[i] = "[" + words[i][:5-m] + "]" + words[i][5-m:]
                    break
            flag = False
            for j in range(1,len(words[i])-4+m):
                sum2 = sum2 - ord(words[i][j-1]) + ord(words[i][j+4-m])
                flag = False
                if BTSearch(treelist[4-m],sum2)==True:
                    if dic[4-m].count([words[i][j:j+5-m],sum2])!=0:
                        words[i] = words[i][:j] + "[" + words[i][j:j+5-m] + "]" + words[i][j+5-m:]
                        flag = True
                        break
            if flag == True:
                break
    return words
            
def treeApend(t,num):
    tmp = t
    while(True):
        if tmp.value > num:
            if tmp.left == None:
                tmp.left = Tree(num)
                break
            else:
                tmp = tmp.left
                continue
        elif tmp.value < num:
            if tmp.right == None:
                tmp.right = Tree(num)
                break
            else:
                tmp = tmp.right
                continue
        else:
            break
    return t

def BTSearch(t,key):
    tmp1 = t
    while(tmp1!=None):
        if tmp1.value > key:
            tmp1 = tmp1.left
        elif tmp1.value < key:
            tmp1 = tmp1.right
        else:
            return True
    return False

def treeMaker5(stringinwords,control):
    if len(stringinwords) <control:
        return None
    sum1 = 0
    for i in range(0,control):
        sum1 = sum1 + ord(stringinwords[i])
    loot = Tree(sum1)
    for i in range(1,len(stringinwords)-control+1):
        sum1 = sum1 - ord(stringinwords[i-1]) + ord(stringinwords[i+control-1])
        treeApend(loot,sum1)
    return loot
    
def treeMaker6(listofstrings):
    if len(listofstrings)== 0:
        return None
    loot = Tree(listofstrings[0][1])
    for i in range(1,len(listofstrings)):
        treeApend(loot,listofstrings[i][1])
    return loot
