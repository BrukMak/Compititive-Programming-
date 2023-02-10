class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        img1_ones = []
        img2_ones = []
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    img1_ones.append((i, j))

                if img2[i][j] == 1:
                    img2_ones.append((i, j))

        
        difference = defaultdict(int)
        for r1, c1 in img1_ones:
            for r2, c2 in img2_ones:
                k = (r1-r2, c1-c2)
                difference[k] += 1
                

        return max(difference.values() or [0])