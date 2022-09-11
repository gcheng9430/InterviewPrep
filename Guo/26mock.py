# input:arr   int k
# : [1, 3, 5, 7, 10] k = 7;
# miss nums: 2, 4, 6, 8, 9
# k - List.size( ) numbers who are smallest of missing numbers
# return : sum of these smallest missing numbers

# 2
# missing=[2,4]
# 6

# runtime: O(nlogn for sorting +n for loop=O(nlogn)
# space:O(logn for sort)
def minimalKSum(nums,k):
    #intuition: the result should be 1+2+..maxVal - sum of nums(note that we minus existing number during  the loop)
    # for every element, we minus itself from res, we find out the difference of the next element  with itself
    # decrease remaining k accordingly
    nums.sort()
    n = len(nums)
    sumNum = 0
    maxVal = 0
    k = k-len(nums)
    res = 0
    for i in range(n-1):
        res -= nums[i]
        diff = nums[i+1]-nums[i]
        if diff>1:
            temp = diff-1
            if temp<k:
                k-= temp
            else: #temp>=k,we won't reach next number, stop at k
                maxVal = nums[i]+k
                k= 0
                break
    #process the last element if needed: if we still have k reamaining
    if k>0:
        res -= nums[-1] 
        maxVal = nums[-1]+k
    return res+(1+maxVal)*maxVal//2

nums = [1, 3, 5, 7, 10] 
k = 7
print("Expted:6, Actual:",minimalKSum(nums,k))


# 用上面那个
# intuition: starting from 1, continue to increase until curr is not in arr, add it to missing array
#             end  when missing arr reaches required len
# runtime:O(n+k=max(n,k))->depends on k, could go up to n^2
# space:O(1)
def minimalKSum2(nums,k):
    mySet = set(nums)
    curr = 1
    n = k-len(nums)
    missing = []
    while len(missing)<n:
        while  curr in mySet:
            curr +=1
        missing.append(curr)
        curr+=1
    return sum(missing)


print("Expted:6, Actual:",minimalKSum2(nums,k))