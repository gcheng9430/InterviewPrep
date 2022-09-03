from operator import index


# time complexity: O(n) n=len(stock_prices)
# analysis: go through list once to initialize dictionary, which is O(n), and sliding window while loop costs O(n)
# space complexity: O(n)
# analysis: used a dictionary as extra space, and there are n elements in list
import collections

class Solution(object):



    def getKConsistency(self,stock_prices,k):
        res=0
        map = collections.defaultdict(list) #map 需要initialize
        #initialize a dict, stock_price->[index1,index2,index3,...]
        for i in range(len(stock_prices)): #range里面是放一个数所以用len包括一下
            map[stock_prices[i]].append(i)
        #go through each unique price in stock_prices
        for num in map:
            #get its index list
            indexes=map[num]
            #left and right sliding window pointer, count of deletion used, max length of consistent prices
            left,right,used,length=0,0,0,1
            while right<len(indexes)-1:
                #expand window
                right+=1
                used+=indexes[right]-indexes[right-1]-1
                #if not exceed k,update max length
                if used<=k:
                    length=max(length,right-left+1)

                #shrink window
                while used>k:
                    left+=1
                    used-=indexes[left]-indexes[left-1]-1
            #record max length for each unique price
            res=max(res,length)
        return res

def main():
    arr=[1,1,2,1,2,1]
    k=3
        # arr=[7,5,7,7,1,1,7,8,7]
        # k=3
        # arr=[1,2,3,4,5,6,6,6,6,6,6]
        # k=1
    solution = Solution()
    ans=solution.getKConsistency(arr,k)
    print(ans)

    test2 = []
    test3 = [1,1,1,2]
    test4 = [3,3,3]
    test5 = [2,2,4,5,1,2]
    test6 = [2]
    print("Expected:0  , Actual: ",solution.getKConsistency(test2,3))
    print("Expected: 3 , Actual: ",solution.getKConsistency(test3,2))
    print("Expected: 3 , Actual: ",solution.getKConsistency(test4,0))
    print("Expected: 2 , Actual: ",solution.getKConsistency(test5,2))
    print("Expected: 1 , Actual: ",solution.getKConsistency(test6,2))
    
if __name__ == "__main__":
    main()
    
