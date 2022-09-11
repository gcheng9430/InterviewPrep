# thoughts: we just need sorting for first k elements, thus we can use quick sorting instead of 
# sorting the entire list which costs O(Nlog(N))

# time complexity: O(N) in average case and O(N^2)in the worst case, where N is the length of points 
# space complexity: O(N)

import collections
import random


class Solution(object):
    def find(self, points, K):
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        # sort in ascending order in range[i:j+1]
        def sort(i, j, K):
            
            if i >= j: return
            # choose random element as pivot
            k = random.randint(i, j)
            points[i], points[k] = points[k], points[i]

            mid = partition(i, j)
            if K < mid - i + 1:
                sort(i, mid - 1, K)
            elif K > mid - i + 1:
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(i, j):
            oi = i
            pivot = dist(i)
            i += 1

            while True:
                # [oi,i)<pivot (j,oj]>=pivot
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]
            # put pivot at right place
            points[oi], points[j] = points[j], points[oi]
            return j

        sort(0, len(points) - 1, K)
        return points[:K]
    


def main():
    solution = Solution()
    
    test3 = [[1,2],[3,4],[1,-1]]
    test4 = [[3,3],[5,-1],[-2,4]]
    test5 = [[1,0],[9,0],[3,0],[10,0],[5,0]]
    # test6 = [2]
  
    print("Expected: [[1,-1],[1,2]] , Actual: ",solution.find(test3,2))
    print("Expected: [[3,3],[-2,4]] , Actual: ",solution.find(test4,2))
    print("Expected: [[1,0],[5,0],[3,0]], Actual: ",solution.find(test5,3))
    # print("Expected: 0 , Actual: ",solution.find(test6))
    
if __name__ == "__main__":
    main()