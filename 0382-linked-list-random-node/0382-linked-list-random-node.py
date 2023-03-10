# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.size = 0
        self.head = head
        cur = head
        self.arr = []
        while cur:
            self.size += 1
            self.arr.append(cur.val)
            cur = cur.next

    def getRandom(self) -> int:
        index = random.randint(0, self.size - 1)
        return self.arr[index]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()