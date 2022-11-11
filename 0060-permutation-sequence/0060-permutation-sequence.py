class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Finding all permutation and find the kth => TLE
        
        # The permutation start rom 1 ... n for each has (n! / n) part
        # So find out which part k is
        # do all permutation for (n-1) elements
        # add the group representative to the front on each
        # find the k - (leader - 1)*group_size
        answer = []
        nums = [i for i in range(1 , n + 1)]
        flag = [False for _ in range(n - 1)]
        group_size = factorial(n - 1)
        group_leader = ceil(k / group_size)
        nums.remove(group_leader)
        new_k = k - ((group_leader - 1) * group_size)
        
        
        self.allPermutations(nums, flag, [], answer)
        output = str(group_leader) + answer[new_k - 1]
        return output
    def allPermutations(self, arr, flag, cur, answer):
        if len(cur) == len(arr):
            answer.append("".join(cur))
            return
        for i in range(len(arr)):
            if not flag[i]:
                flag[i] = True
                cur.append(str(arr[i]))
                self.allPermutations(arr, flag, cur, answer)
                cur.pop()
                flag[i] = False
            
            
            
        