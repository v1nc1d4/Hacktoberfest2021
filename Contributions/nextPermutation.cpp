void nextPermutation(vector<int>& nums) {
    int n = nums.size();
    int i = n - 1;
    while (i - 1 >= 0 && nums[i - 1] >= nums[i])i--;
    --i;
    if (i < 0) {
        reverse(nums.begin(), nums.end());
        return;
    }
    int j = n - 1;
    while (j > i && nums[j] <= nums[i])--j;
    swap(nums[i], nums[j]);
    sort(nums.begin() + i + 1, nums.end());
    return;
}
