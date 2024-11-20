from typing import List

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