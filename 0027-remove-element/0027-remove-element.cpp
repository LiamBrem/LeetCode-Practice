class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0;

        while (i < nums.size()){
            while (i < nums.size() && nums[i] == val){
                int last_element = nums.back();
                nums.pop_back();
                nums[i] = last_element;

            }
            i++;
        }

        return nums.size();
    }
};