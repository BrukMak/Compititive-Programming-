class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        st_ptr , en_ptr = 0, len(numbers)-1
        while st_ptr < en_ptr:
            cur = numbers[st_ptr] + numbers[en_ptr]
            if cur < target:
                st_ptr += 1
            elif cur > target:
                en_ptr -= 1
            else:
                return [st_ptr+1, en_ptr + 1]
            