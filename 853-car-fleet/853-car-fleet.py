class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spd = list(zip(position, speed))
        
        pos_spd.sort()
        
        time = []
        for i in pos_spd:
            time.append([((target - i[0]) / i[1])])
        
        dec_stack = []
        
        for i in time:
            while dec_stack and dec_stack[-1] <= i:
                dec_stack.pop()
            dec_stack.append(i)
            
        return len(dec_stack)
        
