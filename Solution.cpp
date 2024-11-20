#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        // 'include' and 'exclude' are pointers for the sliding window
        // 'n' is the size of the input vector 'nums'
        int include = 0, exclude = 0, n = nums.size();

        // 'max_Subarray_Sum' stores the maximum sum found for valid subarrays
        // 'current_Subarray_Sum' stores the sum of the current subarray
        long long max_Subarray_Sum = 0, current_Subarray_Sum = 0;

        // 'subarray_With_Distinct_Elements' is a hash map to track distinct elements in the current subarray
        unordered_map<int, bool> subarray_With_Distinct_Elements;

        // Iterate with the 'include' pointer to expand the window
        while(include < n) {
            // If the length of the subarray is equal to 'k', check and update the maximum sum
            if(include - exclude == k) {
                max_Subarray_Sum = max(max_Subarray_Sum, current_Subarray_Sum);

                // Exclude the element at the 'exclude' pointer from the sum and the hash map
                current_Subarray_Sum -= nums[exclude];
                subarray_With_Distinct_Elements.erase(nums[exclude]);
                ++exclude;  // Move the 'exclude' pointer to the right
            }

            // If the element at 'include' is not a duplicate, include it in the subarray
            if(subarray_With_Distinct_Elements.find(nums[include]) == subarray_With_Distinct_Elements.end()) {
                // Add the element to the current subarray sum and hash map
                current_Subarray_Sum += nums[include];
                subarray_With_Distinct_Elements[nums[include]] = true;
                ++include;  // Move the 'include' pointer to the right
            }
            else {
                // If the element at 'include' is a duplicate, exclude elements until it's removed
                while(exclude < n && nums[exclude] != nums[include]) {
                    // Remove elements from the left side of the subarray
                    current_Subarray_Sum -= nums[exclude];
                    subarray_With_Distinct_Elements.erase(nums[exclude]);
                    ++exclude;  // Move 'exclude' pointer to the right
                }

                // Remove the element at 'exclude' and move the 'exclude' pointer to the right
                current_Subarray_Sum -= nums[exclude];
                subarray_With_Distinct_Elements.erase(nums[exclude]);
                ++exclude;
            }
        }

        // After the loop ends, check if we have a valid subarray of length 'k' and update the max sum
        if(include - exclude == k)
            max_Subarray_Sum = max(max_Subarray_Sum, current_Subarray_Sum);

        // Return the maximum sum of any valid subarray of length 'k'
        return max_Subarray_Sum;
    }
};

int main() {
    vector<int> nums = {1,5,4,2,9,9,9}; int k = 3;
    Solution sol;

    cout << sol.maximumSubarraySum(nums, k) << endl;
}