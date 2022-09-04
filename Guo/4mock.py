# array execution 
# n tasks
# ith task: execution[n] time 

# 5 5 3 6 5 3
# after time 5:

#   3 3 6 3 3
# after time 3:
#     3 6 2 3

# after time 3:
#       6 2 2

# after time 6:
#         2 2

# after 2:
#            2

# after 2:
# []

# return: total time elapse 




# 4 2 4 2
# 0 1 2 3

# valToIdxList = 
# 4->0,2
# 2->1,3

# idxToOtherIdxs
# 0->[2]
# 2->[0]
# 1->[3]
# 3->[1]

# time =4
# [4,2,2,2]
# i=1,curr=2

import collections

#possible better： 
def solution2(execution):
    #intituion: 记录每个value出现了几次（因为别的value无论怎样变化不会影响这个value 所以可以直接遍历次数 每次加value/2
    valToFreq = collections.defaultdict(int)
    for num in execution:
        valToFreq[num]+=1
    
    time = 0
    for val,freq in valToFreq.items():
        for i in range(freq):
            time  += val
            val = int(round(val/2.0))
    return time





#runtime O(n^2)
#space O(n^2)

def solution(execution):
    #val->list of idx Hashmap
    valToIdxList = collections.defaultdict(list)
    for idx,value in enumerate(execution):
        valToIdxList[value].append(idx)

    #idx-> list of idx 
    idxToOtherIdxs = collections.defaultdict(list)
    for value in valToIdxList:
        idxList = valToIdxList[value]
        for idx in idxList:
            idxToOtherIdxs[idx] = idxList
            idxToOtherIdxs[idx].remove(idx)
            
    #iterate through array and count time spent
    time  = 0
    for i in range(len(execution)):
        curr = execution[i]
        time += curr
        #divide later elements that originally equal to this element by half
        for idx in idxToOtherIdxs[i]:
            if idx>i:
                execution[idx] = int(round(execution[idx]/2.0))

    return time





