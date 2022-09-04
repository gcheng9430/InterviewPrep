# input: string
# define: 1 occurance ->redundant free
# return:min # of redundance free subarray i can divide into

# a abcde a->3
# al ab am a->4
# a a a a a a->6

#intuition:using two pointers, sliding window with hashSet
#runtime:O(n)
#space:O(n)
def findMinSegments(password):
    if not password:
        return 0
    right = 0
    n = len(password)
    window = set()
    res = 1 #注意这里是1！！！！ 
    while right<n:
        #if we found a repeating char, start with a new redundant free subarray
        if password[right] in window:
            res +=1
            window  = set()
        #add to window and update sum
        window.add(password[right])
        right+=1
    return res

password1 = "aabcdea"
password2 = "alabama"
password3 = "aaaaaa"
print("Expted:3, Actual:",findMinSegments(password1))
print("Expted:4, Actual:",findMinSegments(password2))
print("Expted:6, Actual:",findMinSegments(password3))



# al ab am a->4
# dp[0, 1, 1, 2,2 ,3 ,3 , 4]
# window:()
#intuition: dp[i] is the minimum number of redundance free subarrays until ith element(including)
#dp[i] = min(dp[i-1],dp[i-2],dp[i-k])+1 where k is leftmost idx where k-i doesn't have repeating element
#basically we extend the last subarray containing ith as much  as we can and choose one that gives minimum count
#runtime:O(n^2)
#space:O(n)
def solution(data):
    n = len(data)
    dp = [float('inf')]*(n+1)
    dp[0] = 0

    #iterate through the array
    for idx, value in enumerate(data):
        j=idx
        window = set()
        #j starting from idx going backward
        while j>=0:
            #if we encounter reapeating element, we break because data[j:idx+1] cannot  be redundant free
            if data[j] in window:
                break
            else: #record if we get a better  result  with dp[j-1](min count until j-1) with the last  reundent free as data[j:idx+1]
                window.add(data[j])
                dp[idx+1] = min(dp[idx+1],1+dp[j])
            j-=1

    return dp[-1]

print("Expted:3, Actual:",solution(password1))
print("Expted:4, Actual:",solution(password2))
print("Expted:6, Actual:",solution(password3))
