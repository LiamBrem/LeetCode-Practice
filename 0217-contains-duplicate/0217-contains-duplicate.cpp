class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_set<int> hashSet;

        for (int i = 0; i < nums.size(); i++){
            if (hashSet.count(nums[i]) == 1){
                return 1; 
            }

            hashSet.insert(nums[i]);
        }

        return 0; 
        
    }
};