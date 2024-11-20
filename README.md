- ## Approach 2:- Sliding Window

    - ### Intuition:
        The problem requires finding the maximum sum of a subarray of length `k` where all elements in the subarray are distinct. The idea is to maintain a sliding window of size `k` and ensure that all elements within the window are distinct. If a duplicate is encountered, we adjust the window by removing elements from the start of the subarray (using the `exclude` pointer) until the duplicate is removed. This allows us to efficiently compute the sum of valid subarrays and track the maximum sum.

    - ### Approach:
        1. **Sliding Window Technique**: 
            - We maintain a sliding window with two pointers (`include` and `exclude`) that track the bounds of the current subarray.
            - The `include` pointer adds elements to the subarray, while the `exclude` pointer removes elements from the subarray when duplicates are encountered.
        
        2. **Tracking Distinct Elements**: 
            - A dictionary (`subarray_With_Distinct_Elements`) is used to store the elements in the current window to check for duplicates efficiently.
        
        3. **Window Expansion and Contraction**: 
            - As we move the `include` pointer, we add elements to the subarray and update the sum. 
            - If a duplicate is found, we move the `exclude` pointer to the right and remove elements until the duplicate is excluded, ensuring all elements in the window are distinct.
        
        4. **Sum Calculation**: 
            - Whenever the window length reaches `k`, we check the sum of the current subarray. If it is larger than the previous maximum, we update the maximum sum.
        
        5. **Final Calculation**: 
            - After the loop ends, we perform one last check to ensure that the last valid subarray of length `k` is considered for the maximum sum.

    - ### Code Implementation:
        - **Python Solution**

            ```python3 []
            class Solution:
                def maximumSubarraySum(self, nums: List[int], k: int) -> int:
                    # Initialize variables:
                    # 'include' is the index to include new elements in the subarray
                    # 'exclude' is the index to exclude elements from the subarray
                    # 'n' is the length of the input array 'nums'
                    include, exclude, n = 0, 0, len(nums)

                    # 'max_Subarray_Sum' will hold the maximum sum found for subarrays of length 'k'
                    # 'current_Subarray_Sum' tracks the sum of the current valid subarray
                    max_Subarray_Sum, current_Subarray_Sum = 0, 0
                    
                    # 'subarray_With_Distinct_Elements' is a dictionary to track distinct elements in the current subarray
                    subarray_With_Distinct_Elements = {}

                    # Iterate while 'include' pointer is within the array
                    while include < n:
                        # If the subarray length is equal to 'k', check if it's the maximum sum
                        if include - exclude == k:
                            max_Subarray_Sum = max(max_Subarray_Sum, current_Subarray_Sum)
                            
                            # Remove the element at the 'exclude' index from the subarray
                            current_Subarray_Sum -= nums[exclude]
                            subarray_With_Distinct_Elements.pop(nums[exclude])
                            
                            # Move the 'exclude' pointer to the right, effectively excluding the element
                            exclude += 1

                        # If the current element at 'include' is not a duplicate, add it to the subarray
                        if nums[include] not in subarray_With_Distinct_Elements:
                            subarray_With_Distinct_Elements[nums[include]] = True
                            current_Subarray_Sum += nums[include]
                            include += 1
                        else:
                            # If the current element is a duplicate, exclude elements until the duplicate is removed
                            while exclude < n and nums[exclude] != nums[include]:
                                current_Subarray_Sum -= nums[exclude]
                                subarray_With_Distinct_Elements.pop(nums[exclude])
                                exclude += 1

                            # Remove the duplicate element (i.e., the one at 'exclude')
                            current_Subarray_Sum -= nums[exclude]
                            subarray_With_Distinct_Elements.pop(nums[exclude])
                            
                            # Move the 'exclude' pointer to the right to skip the duplicate element
                            exclude += 1
                    
                    # After the loop ends, check one last time if we have found a valid subarray of length 'k'
                    if include - exclude == k:
                        max_Subarray_Sum = max(max_Subarray_Sum, current_Subarray_Sum)

                    # Return the maximum sum of valid subarrays of length 'k'
                    return max_Subarray_Sum
            ```
        
        - **C++ Solution**

            ```cpp []
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
            ```

    - ### Time Complexity:
        - **Outer Loop**: The `include` pointer iterates through each element in the array exactly once, so the outer loop runs in **O(n)**, where `n` is the length of the `nums` array.
        - **Inner Loop (Exclude Pointer Adjustment)**: The `exclude` pointer may move to the right for each duplicate encountered, but each element is excluded at most once. Therefore, the total number of operations performed by the `exclude` pointer is also **O(n)**.
        - **Overall Time Complexity**: Since each pointer (`include` and `exclude`) moves across the array only once, the total time complexity is **O(n)**.

    - ### Space Complexity:
        - **HashMap**: The dictionary `subarray_With_Distinct_Elements` stores elements from the current subarray. In the worst case, it stores `k` distinct elements (if all elements in the subarray are distinct). Therefore, the space complexity due to the hash map is **O(k)**.
        - **Other Variables**: The other variables (`include`, `exclude`, `current_Subarray_Sum`, `max_Subarray_Sum`, etc.) take constant space, i.e., **O(1)**.
        - **Overall Space Complexity**: The overall space complexity is **O(k)** due to the space required by the hash map.