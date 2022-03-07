class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> vis(nums.begin(), nums.end());
        int maxlen = 0;
        for(int& num:nums){
            int count = 0;
            if(!vis.count(num - 1)){
                while(vis.count(num)){
                    count++;
                    num++;
                }
            }
            
            maxlen = max(maxlen, count);
        }
        
        return maxlen;
    }
};