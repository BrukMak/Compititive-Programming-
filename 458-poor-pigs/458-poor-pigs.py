class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return ceil(math.log(buckets, ((minutesToTest // minutesToDie)+1)))
        
        #one pig could test minutesToTest // minutesToDie) + 1
        #so (test + 1) ^ res >= buckets
        