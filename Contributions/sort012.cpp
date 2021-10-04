    void sortColors(vector<int>& nums) {
      int left = -1, right = nums.size(), curr = 0;
        
        
        while(curr < right){
            if(nums[curr] == 0){
                swap(nums[++left], nums[curr]);
                curr++;
            }
            else if(nums[curr] == 2){
                swap(nums[curr], nums[--right]);
            }
            else
                curr++;
        }
    }
