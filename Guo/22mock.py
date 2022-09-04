# input: ratings arr 
# 4:39

# return: int :valid group of ratings: 
# 4 3 5 4 3
# 9

# 9 consecutive decreasing subarray
# 5 single
# 43 54 43 3s
# 543 1s


# right-left+1 = n
# n + (n-1)+ (n-2)+ 1 = (1+n)*n/2

# 4 3 5 4 3 
# left = 2
# right = 5
# prev = 3
# count = 3+ (1+3)*3//2=3+6=9

#intution: two pointers, coontinue to find consec dec array, when 
# an element violate the rule, reset subarray, and process the previous one
#with 首项加末项的和乘项数除以二 （算1个ele 2个ele 到最后一整条）
#runtime O(n) space O(1)

def solution(ratings):
    if not ratings:
        return 0

    n = len(ratings)
    left = 0
    right = 0
    prev = ratings[0]+1
    count = 0
    while right<n:
        curr = ratings[right]
        if curr!=prev-1:
            #process the previous one
            leng = right-left
            count += (1+leng)*leng//2
            #reset subarray  
            left = right
        prev = curr
        right+=1
    #process the last subarray we found
    leng = right-left
    count += (1+leng)*leng//2
    return count 

ratings = [4,3,5,4,3]
print("Expected:9, Actual: ",solution(ratings))