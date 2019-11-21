def nearestGreater(a):
    n = len(a)
    b = []
    for i in range(0,n):
        tmp = a[i]
        j = i-1
        k = i+1
        check = i
        while(j>=0 or k<n):
            if j>=0:
                if a[j] > tmp:
                    check = j
                    break
                j = j - 1
            if k<n:
                if a[k] > tmp:
                    check = k
                    break
                k = k + 1
        if check == i:
            b.append(-1)
        else:
            b.append(check)
    return b
