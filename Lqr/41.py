import collections

# time complexity: O(n)
# analysis: 
# space complexity: O(1)
# analysis: 

class Solution(object):
    def find(self,rideDuration,songDuration):
        # waiting number -> cur index
        dict=collections.defaultdict(int)
        song1,song2=-1,-1
        for i in range(len(songDuration)):
            length=songDuration[i]
            waitingLength=rideDuration-30-songDuration[i]
            # check if match with another song
            if length in dict:
                if max(length,songDuration[dict[length]]>max(songDuration[song1],songDuration[song2])):
                    song1,song2=i,dict[length] 
            # add to dict
            dict[waitingLength]=i
        return [song2,song1]
            


def main():
    solution = Solution()
    
    test3 = [1,10,25,35,60]
    k3=90
    test4 = [1,2,3,4,5]
    k4=90
    test5 =  [1,10,25,35,10,50,60]
    k5=90
    test6 = 'aaaaaa'
    k6=0
  
    print("Expected: 2,3 , Actual: ",solution.find(k3,test3))
    print("Expected: -1,-1 , Actual: ",solution.find(k4,test4))
    print("Expected: 4,5 , Actual: ",solution.find(k5,test5))
    # print("Expected: 5 , Actual: ",solution.find(test6,k6))
    
if __name__ == "__main__":
    main()