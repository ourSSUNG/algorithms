def graphDistances(g, s):
    ans = []
    rem = []
    for i in range(0,len(g)):
        if g[s][i]!= -1:
            ans.append(g[s][i])
        else:
            ans.append(31)
        rem.append(i)
    ans[s] = 0
    rem.remove(s)
    ssg(g,0,rem,s,ans)
    return ans
    
def ssg(g,sumation,remain,now,ans):
    if ans[now] > sumation:
        ans[now] = sumation
    if len(remain)==0:
        return 0
    for i in range(0,len(remain)):
        if g[now][remain[i]] != -1:
            ssg(g,sumation+g[now][remain[i]],remain[:i]+remain[i+1:],remain[i],ans)
    return 0
