int removeDuplicates(vector<int>& nums) {
	int n = nums.size();
	if (n == 0)return 0;
	int i = 0, j = 1;

	while (j < n) {
		if (nums[i] != nums[j]) {
			nums[++i] = nums[j++];
		}
		else {
			j++;
		}
	}
	return i + 1;
}
