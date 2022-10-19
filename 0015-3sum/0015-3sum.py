class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        itemsBefore = set()
        itemsBefore.add(nums[0])
        answer = set()
        for index2 in range(1, N):
            second = nums[index2]
            for index3 in range(index2+1, N):
                third = nums[index3]
                first = 0 - (second + third)
                if first in itemsBefore:
                    answer.add(tuple(sorted([first, second, third])))
            itemsBefore.add(second)
        return answer
            
            
        