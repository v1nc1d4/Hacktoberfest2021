int majorityElement(vector<int>& nums) {
    int n = nums.size(), curr = nums[0], fq = 1;
    for (int i = 1; i < n; i++) {
        if (nums[i] == curr)fq++;
        else {
            fq--;
            if (fq == 0) {
                curr = nums[i];
                fq = 1;
            }
        }
    }
    return curr;
}

