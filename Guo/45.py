class Solution:
     
     #intuition: Calculate a number's difference to the number before it. If that number is negative
     #           we know that we must add that value to make the array non decreasing 
     #runtime: O(N)
     #space: O(1)
    def makePowerNonDecreasing(self,nums):
        if len(nums)<=1:
            return 0

        res = 0
        for i in range(1,len(nums)):
            # diff.append(nums[i]-nums[i-1]) 
            # if diff[-1]<0:
            #     res += abs(diff[-1]) 实际不用差分数组
            diff = nums[i]-nums[i-1]
            if diff<0:
                res += abs(diff)

        return res


def main():
    sol = Solution()
    nums = [3,4,1,6,2]
    result =  sol.makePowerNonDecreasing(nums)
    print('Expected: 7, Result: ',result)
 
if __name__=="__main__":
    main()
