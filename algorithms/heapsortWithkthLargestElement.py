def kthLargestElement(nums, k):
    heaptree = []
    for i in range(0,len(nums)):
        heapInput(heaptree,nums[i])
    for i in range(0,k-1):
        heapPop(heaptree)
    return heapPop(heaptree)
        
def heapInput(heap,num):
    inputindex = len(heap)
    heap.append(num)
    while(True):
        if inputindex == 0:
            break
        tmp =(inputindex+1)//2-1
        if num > heap[tmp]:
            tmp2 = num
            heap[inputindex] = heap[tmp]
            heap[tmp] = tmp2
            inputindex = tmp
        else:
            break
    return heap

def heapPop(heap):
    tmp = heap[0]
    n = len(heap)
    heap[0] = heap[n-1]
    heap[n-1] = tmp
    index = 0
    while(True):
        newindex = index*2 +1
        if newindex > len(heap)-2:
            break
        elif newindex == len(heap)-2:
            if heap[index] < heap[newindex]:
                tmp = heap[index]
                heap[index] = heap[newindex]
                heap[newindex] = tmp
                index = newindex
            else:
                break
        else:    
            if heap[newindex] > heap[newindex+1]:
                if heap[index] < heap[newindex]:
                    tmp = heap[index]
                    heap[index] = heap[newindex]
                    heap[newindex] = tmp
                    index = newindex
                else:
                    break
            else:
                if heap[index] < heap[newindex+1]:
                    tmp = heap[index]
                    heap[index] = heap[newindex+1]
                    heap[newindex+1] = tmp
                    index = newindex+1
                else:
                    break
    return heap.pop()
