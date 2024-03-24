class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        - The most optimal solution for this porblem is using Floyd’s Tortoise and Hare algorithm
        - Basically if a number is repeated in the array, we can consider it as a graph/ linked list and 
        traverse through it and make a cycle out of it at some point
        - Eg. nums = 3, 1, 3, 4, 2: nums[0] -> 3: nums[3] -> 4: nums[4] -> 2: nums[2] -> 3 after this
        point it will start to go in cycles as a result we will use the Torotoise and Hare algorithm           to get the point where the cycle is created which give us the repeated number
        
        """
        
        slow , fast = nums[0], nums[nums[0]] # we don't to make the start point similar as its the condition for the while loop
        
        while fast != slow:
            slow = nums[slow] # one step
            fast = nums[nums[fast]] # double step

        # reset one of the pointers and move in same pace
        slow = 0
        
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        
        return slow # return any
        
        
        
        