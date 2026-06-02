# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #define a hash set which will contain all the node's address
        #use a loop to loop through all the nodes
        #if a node repeats then there is a cycle else not
        nodes = set()
        while head:
            if head.next in nodes:
                return True
            else:
                nodes.add(head.next)
            head = head.next
        return False
