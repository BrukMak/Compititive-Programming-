class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def numRollsToTargetHelper(cur_die, cur_sum):
            if cur_die == n:
                return 1 if cur_sum == target else 0

            res = 0
            for i in range(1, k + 1):
                res += numRollsToTargetHelper(cur_die + 1, cur_sum + i)

            return res

        return numRollsToTargetHelper(0, 0) % (10**9 + 7)