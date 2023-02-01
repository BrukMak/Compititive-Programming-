class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        finding k sized window of max black count 
        """
        black_white_count = defaultdict(int)
        left = 0
        max_black_count = 0
        for right in range(len(blocks)):
            black_white_count[blocks[right]] += 1
            if right - left + 1 > k:
                black_white_count[blocks[left]] -= 1
                left += 1
            max_black_count = max(max_black_count, black_white_count['B'])
            
        return k - max_black_count
                