
def imbalanceCount(nums):
    #intuition: use monoStack to create left where left[i] is the index of the first
    #number on i's left that is larger than i and right[i] is the idx of the first
    #number that is larger than i
    #maintain value->index array
    #for each element in  nums, assume it is the smaller one in imbalance, calculate the 
    #number of all possible subarrays with it as the smaller one  of imbalance 
    #then the larger one could either be on the left or on the right
    #we can't include the element that is exactly one larger, so consider it on the
    #left or on the right, and for each case calculet larger imbalance on the left+
    #larger imbalance on the right
    n  = len(nums)
    valToIdx = [0]*(n+1)
    #create value to idx array
    for idx, value in enumerate(nums):
        valToIdx[value]=idx

    #create left and right with stack
    left = [-1]*n
    stack  = [] #decreasing stack  so i can find first larger element on the left 
    for idx,value in enumerate(nums):
        while stack and nums[stack[-1]]<value:
            stack.pop()
        if stack:
            left[idx]=stack[-1]
        stack.append(idx)
    #create right
    stack = []
    right = [n]*n
    for idx in range(n-1,-1,-1):
        value = nums[idx]
        while stack and nums[stack[-1]]<value:
            stack.pop()
        if stack:
            right[idx] = stack[-1]
        stack.append(idx)
    

    count = 0
    for idx,value in enumerate(nums):
        #n自己 和n-1都不可能作为imbalance里更小的那个
        if value>=n-1:
            continue
        #find out value+1 to avoid including it
        oneMoreIdx = valToIdx[value+1]
        #if the element one larger is on the right 
        if oneMoreIdx>idx:
            #add all possibilities of (value,largerOnTheRight) as imbalance
            count += (idx+1)*(oneMoreIdx-right[idx]) #possibility to the left of value * to the right of Larger
            #add all possibilities of (largerOnTheLeft,value) as imbalance
            if left[idx]>=0:
                count += (left[idx]+1)*(right[idx]-idx) #不要 延到后面 不然就重复了
        else: #if the element one larger is on the left 
            #add all possibilities of (largerOnTheLeft,value) as imbalance
            count += (left[idx]-oneMoreIdx)*(n-idx)
            #add all possibilities of (value,largerOnTheRight) as imbalance
            if right[idx]<n:
                count += (idx-left[idx])*(n-right[idx])
    return count
            

nums = [4, 1, 3, 2]
print('Expected: 3, Actual: ',imbalanceCount(nums))