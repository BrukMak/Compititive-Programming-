class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        p1, p2 = 0, 0
        nums1.sort()
        nums2.sort()
        intersection = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                intersection.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                p1 += 1
        return intersection