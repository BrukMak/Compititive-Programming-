class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        n = len(arr)
        target = n
        for _ in range(n):
            index_target = arr.index(target)+1
            arr
            if index_target != target:
                arr = arr[:index_target][::-1] + arr[index_target:]
                arr = arr[:target][::-1] + arr[target:]
                ans.append(index_target)
                ans.append(target)
            target -= 1
        return(ans)