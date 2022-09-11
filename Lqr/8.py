from turtle import onclick

# thoughts: use two pointers, left pointer always start from index 0, right pointer will go through string

# time complexity: average O(n) worst O(n^2)
# analysis: right pointer go through string once, each move left pointer could possible go O(1)~O(n);
# in worst case if all letters are equal, O(n^2)
# space complexity: O(1)
# analysis: only created a result list, not counted as extra space



class Solution(object):
    def find(self,s):
        res=[None]*len(s)
        res[0] = len(s)
        for i in range(1,len(s)):
            left,right,count=0,i,0
            # move forward pointers and update result if letter of prefix and suffix matches
            while right<len(s) and s[right]==s[left]:
                left=left+1
                right=right+1
                count=count+1
            res[i]=count
        return res


def main():
    solution = Solution()
    
    test3 = 'abcabcd'
    test4 = 'a'
    test5 = 'abc'
    test6 = 'aaaaaa'
  
    print("Expected: 7003000 , Actual: ",solution.find(test3))
    print("Expected: 1 , Actual: ",solution.find(test4))
    print("Expected: 300 , Actual: ",solution.find(test5))
    print("Expected: 654321 , Actual: ",solution.find(test6))
    
if __name__ == "__main__":
    main()