from heapq import heappush, heappop
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        generator_arr = [2, 3, 5]
        ugly_heap = [1]
        check_dup_set = set()
        count = 0
        
        while count < n - 1:
            poped = heappop(ugly_heap)
            for i in range(len(generator_arr)):
                generated_num = poped * generator_arr[i]
                
                if generated_num not in check_dup_set:
                    check_dup_set.add(generated_num)
                    heappush(ugly_heap, generated_num)
            count += 1
        return heappop(ugly_heap)
