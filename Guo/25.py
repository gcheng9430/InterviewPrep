class Solution:
    #intution: using recursion to calculate the next level
    #runtime:O(n^2)
    #space:O(n)
    def getEncryptedNumber(self,nums):
        if len(nums)==2:
            return str(nums[0])+str(nums[1])
        for i in range(len(nums)-1):
            nums[i]= (nums[i]+nums[i+1])%10
        nums.pop()
        return self.getEncryptedNumber(nums)

def main():
    sol = Solution()
    nums = [4,5,6,7]
    result =  sol.getEncryptedNumber(nums)
    print('Expected: 04, Result: ',result)
 
if __name__=="__main__":
    main()