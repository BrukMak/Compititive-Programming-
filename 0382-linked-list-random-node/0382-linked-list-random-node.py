# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        cur = head
        while cur:
            self.arr.append(cur.val)
            cur = cur.next

    def getRandom(self) -> int:
        index = int(random.random() * len(self.arr))
        return self.arr[index]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()