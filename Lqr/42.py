

class Solution(object):
    def find(self,data):
        # price->name
        goods=[]
        res=[]
        viewCount=0
        for log in data:
            if log[0]=='INSERT':
                goods.append([log[2],log[1]])
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