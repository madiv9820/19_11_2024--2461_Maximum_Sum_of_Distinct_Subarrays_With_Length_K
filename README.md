- ## Approach 1:- Brute Force (Time Limit Exceed)

    - ### Intuition:
        The problem asks us to find the maximum sum of any subarray of length `k` that contains only distinct elements. The key challenge is ensuring that the subarray has exactly `k` elements and no duplicates while calculating the sum.

    - ### Approach:
        1. **Outer Loop (Starting Index)**: We iterate over each possible starting index `index` in the array `nums`. For each starting index, we try to form a subarray of length `k`.
        2. **Inner Loop (Subarray Construction)**: For each starting index, we attempt to build subarrays by iterating from `index` to the end of the array. We maintain a hash map (`unordered_map`) to store elements and check for duplicates.
        3. **Subarray Validation**: If a subarray reaches the required length `k`, we check if it is valid (all distinct elements). If so, we update the maximum sum.
        4. **Breaking on Duplicates**: If a duplicate element is found within the current subarray, we break out of the loop early since the subarray is no longer valid.

        The overall idea is to use a sliding window-like approach where we expand the window by adding elements but ensure that the window contains only distinct elements using the hash map.

    - ### Code Implementation:
        - **Python Solution**

            ```python3 []
            from collections import defaultdict
            from typing import List

            class Solution:
                def maximumSubarraySum(self, nums: List[int], k: int) -> int:
                    # Initialize variable to store the maximum sum of valid subarrays
                    max_Subarray_Sum = 0
                    # Get the length of the input array nums
                    n = len(nums)

                    # Iterate over each starting index of the subarray
                    for index in range(n):
                        # Variable to keep track of the current subarray sum
                        current_Subarray_Sum = 0
                        # Use a defaultdict to store elements of the subarray and check for duplicates
                        subArray = defaultdict(bool)
                        
                        # Start the current subarray at 'index'
                        currentIndex = index

                        # Iterate over the subarray starting at 'index' and check all possible subarrays
                        while currentIndex < n:
                            # If the length of the subarray reaches 'k', check the sum and update the result
                            if currentIndex - index == k:
                                max_Subarray_Sum = max(max_Subarray_Sum, current_Subarray_Sum)
                                break
                            
                            # If the current element is already in the subarray (duplicate), break the loop
                            if nums[currentIndex] in subArray:
                                break
                            
                            # Add the current element to the subarray sum and mark it as seen in the subarray
                            current_Subarray_Sum += nums[currentIndex]
                            subArray[nums[currentIndex]] = True
                            
                            # Move to the next element in the subarray
                            currentIndex += 1

                        # If the subarray length reached 'k', update the maximum sum
                        if currentIndex - index == k:
                            max_Subarray_Sum = max(max_Subarray_Sum, current_Subarray_Sum)

                    # Return the maximum sum found for valid subarrays of length 'k'
                    return max_Subarray_Sum
            ```
        
        - **C++ Solution**

            ```cpp []
            class Solution {
            public:
                long long maximumSubarraySum(vector<int>& nums, int k) {
                    // Initialize the variable to store the maximum subarray sum
                    long long max_Subarray_Sum = 0;
                    
                    // Get the size of the input vector 'nums'
                    int n = nums.size();

                    // Outer loop iterates over each possible starting index of the subarray
                    for (int index = 0; index < n; ++index) {
                        // Variable to accumulate the sum of the curr- ent subarray
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
            ```

    - ### Time Complexity:
        - **Outer Loop**: Iterates over each starting index of the array, which takes `O(n)` where `n` is the length of the array.
        - **Inner Loop**: For each starting index, in the worst case, it iterates through the rest of the array. However, the loop can exit early if a duplicate is encountered or if the subarray reaches the length `k`. In the worst case, the inner loop also takes `O(n)`.
        - **Overall Time Complexity**: Since we have two nested loops that may iterate up to `n` times each, the time complexity is **O(n<sup>2</sup>)**.

    - ### Space Complexity:
        - **Hash Map**: For each subarray, we maintain a hash map to store the elements. In the worst case, the hash map can store up to `k` distinct elements, which takes **O(k)** space.
        - **Other Variables**: We use a constant amount of additional space for variables like `current_Subarray_Sum`, `index`, and `currentIndex`.
        - **Overall Space Complexity**: The space complexity is **O(k)** due to the hash map storing at most `k` distinct elements.