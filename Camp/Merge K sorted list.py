# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for i in range (len(lists)):
            # print(lists[i].next.val)
            node = lists[i]
            while node != None:
                # print(lists[i].val)
                heapq.heappush(h, node.val)
                node = node.next
        
        ans = ListNode() 
        head = ans
         # ans.val = heapq.heappop(h)
        
        while len(h) > 0:
            newNode = ListNode(heapq.heappop(h))
            ans.next = newNode
            ans= ans.next
        
        return head.next
