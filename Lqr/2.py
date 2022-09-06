import collections
from operator import truediv

#假设可以有重复值

class Solution(object):
    def find(self,arr):
        sorted(arr)
        res=1
        found=False
        map= collections.defaultdict(list)
        for i in arr:
            map[i]=False
        for i in range(len(arr)):
            if map[arr[i]]:
                continue
            if i>0&arr[i]==arr[i-1]:
                continue
            count=1
            cur=arr[i]
            while cur*cur in map:
                found=True
                count=count+1
                cur=cur*cur
                map[cur]=True
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


        


