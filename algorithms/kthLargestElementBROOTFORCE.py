def kthLargestElement(nums, k):
    nums.reverse()
    heap = [nums[0]]
    i = 1
    while(i<k and i<len(nums)):
        
        tmp = nums[i]
        for j in range(0,len(heap)):
            if heap[j] >= tmp:
                heap = heap[:j] + [tmp] + heap[j:]
                break
            if j == len(heap)-1:
                heap.append(tmp)
        i = i + 1
    for j in range(i,len(nums)):
        
        tmp = nums[j]
        if tmp <= heap[0]:
            continue
        if tmp >= heap[k-1]:
            heap.append(tmp)
            heap.pop(0)
            continue
        for m in range(0,k):
            if heap[m] >= tmp:
                heap = heap[:m] + [tmp] + heap[m:]
                heap.pop(0)
                break
            
        
    return heap[len(heap)-k]
