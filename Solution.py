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