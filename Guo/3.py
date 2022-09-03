

# 1 3 5 11 12

# sumArray = [1,3,4,  5 , 6  ]
#            1  3 1,3  4


# (6,2)    1 5
# (8,2)   3 5
# (11,3)   11
# (16,3)    11 4


#intuition: sum all the positive values to be the largest combo
            #turn all the negative value into positive(because plus negative number
            # equals minus positive number)
            #sort the array, starting form the first index, find the k-1 lowest combo sums
            #use the max popularity to minus these lowest sums to get required result
#runtime: O(nlogn+klogk)=O(nlogn)
#space: O(logN for sorting +2k for heap) = O(logN)
import heapq
class Solution:
    def largestCombo(self,popularity,k):
        maxCombo = 0
        for i in range(len(popularity)):
            if popularity[i] > 0:
                maxCombo+=popularity[i]
            else:
                popularity[i] = -popularity[i]
        
        popularity.sort()

        q = [(popularity[0],0)] #contains the min sum of subarray, the last index of the subarray
        minSums = []
        while q and len(minSums)<k-1:
            sum, idx = heapq.heappop(q)
            minSums.append(sum)
            #extend the subarray
            if idx<len(popularity)-1:
                heapq.heappush(q,(sum+popularity[idx+1],idx+1)) #include current one
                heapq.heappush(q,(sum-popularity[idx]+popularity[idx+1],idx+1)) #don't include current one
        
        res = [maxCombo]
        for sum in minSums:
            res.append(maxCombo-sum)
        return res

def main():

    popularity1 = [3,5,-2]
    k1 = 3
    popularity2 = [2,-3]
    k2 = 2
    sol = Solution()
    print("Expted:[8,6,5], Actual:",sol.largestCombo(popularity1,k1))
    print("Expted:[2,0], Actual:",sol.largestCombo(popularity2,k2))

if __name__ == "__main__":
    main()



                

