#thoughts: sort list in ascending order first, then iterate, use dictionary to track whether each number is used in a sequence

#time complexity: O(nlogn)
#analysis: sort costs O(nlogn), initializing dict costs O(n), and iterating each number in input list costs O(n)
#space complexity:O(n)
#analysis: initializing dictionary costs O(n) at most


class Solution(object):
    def find(self,centers,destinations):
        centers.sort()
        destinations.sort()
        sum=0
        for i in range(len(centers)):
            sum+=abs(centers[i]-destinations[i])
        return sum



def main():
    solution = Solution()
    
    test3 = [2,8,9,16,4,3,256,5,288,65536]
    test4 = [2,8,9,16,4,3]
    test5 = [2,3,5]
    test6 = [2]
  
    print("Expected: 5 , Actual: ",solution.find(test3))
    print("Expected: 3 , Actual: ",solution.find(test4))
    print("Expected: 0 , Actual: ",solution.find(test5))
    print("Expected: 0 , Actual: ",solution.find(test6))
    
if __name__ == "__main__":
    main()