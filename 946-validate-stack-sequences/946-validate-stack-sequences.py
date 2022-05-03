class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        check_stack = []
        ptr = 0
        n = len(popped)
        for val in pushed:
            check_stack.append(val)
            while ptr < n and check_stack and check_stack[-1] == popped[ptr]:
                check_stack.pop()
                ptr += 1
        return not check_stack
            