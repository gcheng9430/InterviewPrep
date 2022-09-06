import collections
from operator import truediv

#可以有重复值

#thoughts: sort list in ascending order first, then iterate, use dictionary to track whether each number is used in a sequence

#time complexity: O(nlogn)
#analysis: sort costs O(nlogn), initializing dict costs O(n), and iterating each number in input list costs O(n)
#space complexity:O(n)
#analysis: initializing dictionary costs O(n) at most


class Solution(object):
    def find(self,arr):
        sorted(arr)
        res=1
        found=False
        map= collections.defaultdict(list)
        # initialize dict, number->whether used in a sequence
        for i in arr:
            map[i]=False
        # iterate each number in list, check if it can form a sequence
        for i in range(len(arr)):
            cur=arr[i]
            # check if exist in dict because it could already be removed when added to a sequence before
            if cur not in map:
                continue
            count=1
            # check whether cur*cur in dict
            while cur*cur in map:
                found=True
                count=count+1
                cur=cur*cur
                map.pop(cur)
            res=max(res,count)
        return res if found else 0

def main():
    solution = Solution()
    
    test3 = [2,8,9,16,4,3,256,5,288,65536]
    test4 = [2,8,9,16,4,3]
    test5 = [2,3,5]
    test6 = [2]
  
    print("Expected: 5 , Actual: ",solution.find(test3))
    print("Expected: 3 , Actual: ",solution.find(test4))
    print("Expected: 0 , Actual: ",solution.find(test5))
    print("Expected: 0 , Actual: ",solution.find(test6))
    
if __name__ == "__main__":
    main()


        


