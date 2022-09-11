
import collections
from turtle import right

# thoughts: use two dictionaries(char->frequency), for each step of iteration, move one char from right
# dict to left dict, and check how many letters exist both in left and right dict's key set

# time complexity: O(n)
# analysis: initializing right dict costs O(n); while loop costs O(n) and in each step iterate all entries
# in left dictionary, thus costs O(n) since the max number of entries in left dict is 26
# space complexity: O(1)
# analysis: two dictionaries will in total store 26 character entries at most


class Solution(object):
    def find(self,s,k):
        rightDict = collections.defaultdict(int)
        leftDict = collections.defaultdict(int)
        res=0
        # initiate right dict
        for i in range(len(s)):
            rightDict[s[i]]+=1
        p=0
        # move letters from right dict to left dict
        while p<len(s):
            count=0
            c=s[p]
            rightDict[c]=rightDict[c]-1
            # remove key if no longer exist in right dict
            if rightDict[c]==0:
                rightDict.pop(c)
            leftDict[c]+=1
            # check each letter in left dict also exist in right dict
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