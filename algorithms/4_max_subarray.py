
def find_max(a):
    n = len(a)
    max_value = 0
    start = 0
    end = 0
    tmp_start = 0
    sum1 = 0
    i = 0
    while i != n:
        sum1 = sum1 + a[i]
        if sum1 > max_value:
            start = tmp_start
            end = i
            max_value = sum1
        if sum1 < 0 :
            tmp_start = i+1
            sum1 = 0
        i = i + 1
    return max_value, start, end




