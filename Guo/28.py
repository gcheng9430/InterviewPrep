
def maxSumOfStock(stockPrice,k):
    #intuition: using a sliding window with two pointers, for each 
    #element we add to the window, shrink the window until all elmenet
    #are distinct
    #update maximum price sum if length of the window is k
    #runtime: O(N)
    #space: O(N)
    if not stockPrice or k<=0:
        return -1
    left = 0
    right = 0
    windowSum=0
    globalMax = 0
    window = set()
    while right<len(stockPrice):
        #extend window by one
        curr = stockPrice[right]
        windowSum += curr
        #shrink window when there are duplicates or window too long to meet requirement
        while curr in window or (right-left+1)>k:
            leftCurr = stockPrice[left]
            left+=1
            window.remove(leftCurr)
            windowSum-=leftCurr
        #update max when window length is k
        if right-left+1==k:
            globalMax=max(globalMax,windowSum)
        window.add(curr) 
        right+=1
    return globalMax if globalMax!=0 else -1

stockPrice = [1,2,7,7,4,3,6]
k=3
print("Expted:14, Actual:",maxSumOfStock(stockPrice,k))