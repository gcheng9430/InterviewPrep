# thoughts: use dictionary to count frequency of each number, and for each time we add number to res, 
# make number=number/2

# time complexity: O(n) iterating array and entries in dict costs O(n)
# space complexity: O(n) created n entries in dict at most


import collections
from math import ceil
class Solution(object):
    
    def find(self,execution):
        valToFreq = collections.defaultdict(int)
        # initialize dict
        for num in execution:
            valToFreq[num]+=1
        time = 0
        # make value half when adding value to result, add freq times in total
        for val,freq in valToFreq.items():
            for i in range(freq):
                time  += val
                val = int(ceil(val/2.0))
        return time



# #runtime O(n^2)
# #space O(n^2)

# def solution(execution):
#     #val->list of idx Hashmap
#     valToIdxList = collections.defaultdict(list)
#     for idx,value in enumerate(execution):
#         valToIdxList[value].append(idx)

#     #idx-> list of idx 
#     idxToOtherIdxs = collections.defaultdict(list)
#     for value in valToIdxList:
#         idxList = valToIdxList[value]
#         for idx in idxList:
#             idxToOtherIdxs[idx] = idxList
#             idxToOtherIdxs[idx].remove(idx)
            
#     #iterate through array and count time spent
#     time  = 0
#     for i in range(len(execution)):
#         curr = execution[i]
#         time += curr
#         #divide later elements that originally equal to this element by half
#         for idx in idxToOtherIdxs[i]:
#             if idx>i:
#                 execution[idx] = int(round(execution[idx]/2.0))

#     return time



def main():
    solution = Solution()
    
    test3 = [5,5,3,6,5,3]
    test4 = [4,3,3,3]
    test5 = [5,8,4,4,8,2]
    test6 = [2]
  
    print("Expected: 21 , Actual: ",solution.find(test3))
    print("Expected: 10 , Actual: ",solution.find(test4))
    print("Expected: 25 , Actual: ",solution.find(test5))
    print("Expected: 2 , Actual: ",solution.find(test6))
    
if __name__ == "__main__":
    main()

