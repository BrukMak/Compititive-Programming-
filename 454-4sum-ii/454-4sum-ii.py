class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        g1, g2 = [], defaultdict(int)
        res = 0
        for i in range(n):
            for j in range(n):
                g1.append(nums1[i] + nums2[j])
                g2[nums3[i] + nums4[j]] += 1
        for v in g1:
            if (0-v) in g2:
                res += g2[0-v]
        return res