#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        // Initialize the variable to store the maximum subarray sum
        long long max_Subarray_Sum = 0;
        
        // Get the size of the input vector 'nums'
        int n = nums.size();

        // Outer loop iterates over each possible starting index of the subarray
        for (int index = 0; index < n; ++index) {
            // Variable to accumulate the sum of the current subarray
            long long current_Subarray_Sum = 0;
            
            // HashMap to keep track of the elements in the current subarray
            unordered_map<int, bool> subArray;
            
            // Variable to track the current position in the subarray
            int currentIndex = index;

            // Inner loop checks all subarrays starting at 'index'
            for (; currentIndex < n; ++currentIndex) {
                
                // If the length of the current subarray reaches 'k', check the sum
                if (currentIndex - index == k) {
                    // Update the maximum sum if the current subarray sum is greater
                    max_Subarray_Sum = max(max_Subarray_Sum, current_Subarray_Sum);
                    break;
                }
                
                // If the current element is a duplicate, break the loop (no longer distinct)
                if (subArray.find(nums[currentIndex]) != subArray.end())
                    break;

                // Add the current element to the subarray sum
                current_Subarray_Sum += nums[currentIndex];

                // Mark the element as seen in the subarray
                subArray[nums[currentIndex]] = true;
            }

            // If the subarray length reaches 'k', update the maximum sum
            if(currentIndex - index == k) {
                max_Subarray_Sum = max(max_Subarray_Sum, current_Subarray_Sum);
            }
        }
        
        // Return the maximum sum found for valid subarrays
        return max_Subarray_Sum;
    }
};

int main() {
    vector<int> nums = {1,5,4,2,9,9,9}; int k = 3;
    Solution sol;
    cout << sol.maximumSubarraySum(nums, k) << endl;
}