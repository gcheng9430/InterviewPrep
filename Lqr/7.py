from contextlib import nullcontext
from tkinter.messagebox import NO

# 不知原题的node类 val代表size

# thoughts: use two pointers to go through list, since we need to break the next pointer of
#  the node right before the head of sublist, use another left pointer to track the previous node, 
# which is initialized at dummy; at last break the next pointer of sublist's tail

# time complexity: O(n)
# analysis: right pointer iterate through linkedlist once, costs O(n)
# space complexity: O(1)
# analysis: only used some node pointers, no extra space

class Node(object):
    def __init__(self,v) -> None:
        self.val=v
        self.next=None

class Solution(object):
    def find(self,head):
        dummy=Node(-1)
        dummy.next=head
        # initialize pointers
        leftPrev,left,right=dummy,head,head
        # nodes that record result
        resLeftPrev,resLeft,resRight=leftPrev,left,right
        maxLen,count=1,1
        while right.next!=None:
            # if next size greater than current size, reset left pointer
            if right.next.val>right.val:
                left=right.next
                leftPrev=right
                count=1
            else:
                # if next size <= current size, expand sublist, update result if current length>maxLen
                count=count+1
                if count>maxLen:
                    maxLen=count
                    resLeftPrev=leftPrev
                    resLeft=left
                    resRight=right.next
            right=right.next
        # make next pointer of the node right before result to null, and next pointer of tail to null
        resLeftPrev.next=None
        resRight.next=None
        return resLeft

def main():
    solution = Solution()
    # 2 5 4 4 5
    head,second,third,fourth,fifth=Node(2),Node(5),Node(4),Node(4),Node(5)
    head.next=second
    second.next=third
    third.next=fourth
    fourth.next=fifth

    ans=solution.find(head)
    two=ans.next
    three=two.next

    print("Expected: 5 , Actual: ",ans.val)
    print("Expected: 4 , Actual: ",two.val)
    print("Expected: 4 , Actual: ",three.val)
    
    
if __name__ == "__main__":
    main()