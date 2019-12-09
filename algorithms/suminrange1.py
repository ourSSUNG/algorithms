def sumInRange(nums, queries):
    checker = [0] * len(nums)
    for i in range(0,len(queries)):
        new2 = map(lambda a:a+ 1,checker[queries[i][0]:queries[i][1]+1])
        checker = checker[:queries[i][0]] + list(new2) + checker[queries[i][1]+1:]
    
    ans = 0
    for i in range(0,len(nums)):
        ans = ans + nums[i]*checker[i]
    return ans%(10**9+7)
