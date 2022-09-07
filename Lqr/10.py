
import collections
from turtle import right

class Solution(object):
    def find(self,s,k):
        rightDict = collections.defaultdict(int)
        leftDict = collections.defaultdict(int)
        res=0
        for i in range(len(s)):
            rightDict[s[i]]+=1
        p=0
        while p<len(s):
            count=0
            c=s[p]
            rightDict[c]=rightDict[c]-1
            if rightDict[c]==0:
                rightDict.pop(c)
            leftDict[c]+=1
            for a in leftDict:
                if a in rightDict:
                    count=count+1
            if count>k:
                res=res+1
            p+=1
        return res
            


def main():
    solution = Solution()
    
    test3 = 'abbcac'
    k3=1
    test4 = 'a'
    k4=0
    test5 = 'adbccdbada'
    k5=2
    test6 = 'aaaaaa'
    k6=0
  
    print("Expected: 2 , Actual: ",solution.find(test3,k3))
    print("Expected: 0 , Actual: ",solution.find(test4,k4))
    print("Expected: 4 , Actual: ",solution.find(test5,k5))
    print("Expected: 5 , Actual: ",solution.find(test6,k6))
    
if __name__ == "__main__":
    main()