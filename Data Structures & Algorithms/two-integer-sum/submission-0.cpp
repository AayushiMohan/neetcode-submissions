class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i = 0;
        int j = 0;
        int t = target;
        for(i = 0; i<nums.size();i++){
            for(int j = i+1; j<nums.size();j++){
            if(nums[i]+nums[j]==t){
                return {i,j};
            }
        }
        }
        return {};
    }
};
