class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1, 10)]
        answer = []
        def backtracking(index, cur_arr, target, k, answer):
            if index == 10:
                if k == 0 and target == 0:
                    answer.append(cur_arr[:])
                return 
            if target >= index:
                backtracking(index + 1, cur_arr + [index], target - index, k - 1, answer)
            backtracking(index + 1, cur_arr, target, k, answer)
            
        backtracking(1, [], n, k, answer)
        return answer