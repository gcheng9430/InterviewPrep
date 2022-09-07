# input: arr[int]  
# constraint: 1 diff<=1
# availble: rearrange
# reduce to any number at least one

# return max value from final element of the array 

# [3,2,4,16,3]
# [1,1,1,1,1,1]

#intution: if the largest number is less than length of  element [1,2,3,...n]
#then return the largest number(cannot reduce to larger) else return length of element (n)
#runtime: O(n)
#space: O(1)
def maxFinal(nums):
    maxNum = max(nums)
    return maxNum if maxNum<len(nums) else len(nums)

#runtime: O(nlogn)
#space: O(logn)
def maxFinal2(nums):
    nums.sort()
    nums[0]=1
    for i in range(1,len(nums)):
        if nums[i]>nums[i-1]+1:
            nums[i] = nums[i-1]+1
    return nums[-1]

nums = [3,2,4,16,3]
nums2 = [1,1,1,1,1,1]
print("Expted:5, Actual:",maxFinal(nums))
print("Expted:1, Actual:",maxFinal(nums2))
print("Expted:5, Actual:",maxFinal2(nums))
print("Expted:1, Actual:",maxFinal2(nums2))
