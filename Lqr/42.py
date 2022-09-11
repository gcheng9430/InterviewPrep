
# time complexity: O(ABlog(A)) in worst case, sort once costs Alog(A), and we sorted B times in total;
# A is number of INSERT operations, B is number of VIEW operations
# in left dictionary, thus costs O(n) since the max number of entries in left dict is 26
# space complexity: O(log(A))  because we used sorting method


class Solution(object):
    def find(self,data):
        # price->name
        goods=[]
        res=[]
        viewCount=0
        for log in data:
            # if INSERT, add to the list
            if log[0]=='INSERT':
                goods.append([log[2],log[1]])
            # if VIEW, sort and then update result
            elif log[0]=='VIEW':
                goods.sort()
                res.append(goods[viewCount][1])
                viewCount+=1
        
        return res


def main():
    solution = Solution()
    
    test3 = [['INSERT','MILK','4'],['INSERT','COFFEE','3'],['VIEW','-','-'],['INSERT','PIZZA','5'],['INSERT','GUM','1'],['VIEW','-','-']]
  
    print("Expected: COFFEE,COFFEE , Actual: ",solution.find(test3))
    
if __name__ == "__main__":
    main()