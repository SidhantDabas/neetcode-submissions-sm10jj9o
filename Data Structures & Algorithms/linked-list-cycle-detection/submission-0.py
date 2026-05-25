# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # create a hash table of next pointers
        # if the next pointer already exists then there is a loop
        # just iterate through with while loop till there is loop or end
        # o(n), o(n)
        nxt = set()
        curr = head
        while curr:
            if curr in nxt:
                return True
            else:    
                nxt.add(curr)
            curr = curr.next
        return False

