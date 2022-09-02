import collections

##intuition: keep a hashmap from value to a list of index of that value,
# then use a sliding window to determine the longest possbile subarray within k deletion
#runtime:O(n) let n be the number of elements int he stock_prices array
#            because we traverse the stock price array once to make the hashmap, 
            #and we traverse all the element once in the hashmap 
#space: O(n) because we store n elements in the hashmap 
class Solution:
    def getKConsistency(self, stock_prices: list, k: int) -> int:
        if not stock_prices:
            return 0

        charToIdxList = collections.defaultdict(list)
        for idx,value in enumerate(stock_prices):
            charToIdxList[value].append(idx)
        
        
        res = 1 
        #for each value to keep
        for char in charToIdxList:
            idxList = charToIdxList[char]
            left = 0
            right = 0
            deleted = 0
            length  = 1
            while right <len(idxList)-1:
                #extend window 注意如果从第二个开始才在这里extend（并且不能改出界）如果从第一个开始就直接开始了
                right+=1
                deleted += idxList[right]-idxList[right-1]-1
                
                while deleted>k:
                    #shrink window
                    left +=1
                    deleted -= idxList[left]-idxList[left-1]-1
                
                #now is of the required array
                length = max(length,right-left+1)
            #update global max
            res = max(res,length)
            
        return res

def main():
    

        # arr=[7,5,7,7,1,1,7,8,7]
        # k=3
        # arr=[1,2,3,4,5,6,6,6,6,6,6]
        # k=1
    solution = Solution()

    test1=[1,1,2,1,2,1]
    test2 = []
    test3 = [1,1,1,2]
    test4 = [3,3,3]
    test5 = [2,2,4,5,1,2]
    print("Expected: 4  , Actual: ",solution.getKConsistency(test1,3))
    print("Expected: 0  , Actual: ",solution.getKConsistency(test2,3))
    print("Expected: 3 , Actual: ",solution.getKConsistency(test3,2))
    print("Expected: 3 , Actual: ",solution.getKConsistency(test4,0))
    print("Expected: 2 , Actual: ",solution.getKConsistency(test5,2))
    
if __name__ == "__main__":
    main()