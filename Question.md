# [2461. Maximum Sum of Distinct Subarrays With Length K](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k)

__Type:__ Medium <br>
__Topics:__ Array, Hash Table, Sliding Window <br>
__Companies:__ IBM, Nvidia, Meta, Amazon, Google, Microsoft, Walmart Labs
<hr>

You are given an integer array `nums` and an integer `k`. Find the maximum subarray sum of all the subarrays of `nums` that meet the following conditions:

- The length of the subarray is `k`, and
- All the elements of the subarray are __distinct__.

Return _the maximum subarray sum of all the subarrays that meet the conditions_. If no subarray meets the conditions, return `0`.

_A __subarray__ is a contiguous non-empty sequence of elements within an array_.
<hr>

### Examples:

- **Example 1:** <br>
**Input**: nums = [1,5,4,2,9,9,9], k = 3 <br>
**Output:** 15 <br>
**Explanation:** The subarrays of nums with length 3 are: <br> - [1,5,4] which meets the requirements and has a sum of 10. <br> - [5,4,2] which meets the requirements and has a sum of 11. <br> - [4,2,9] which meets the requirements and has a sum of 15. <br> - [2,9,9] which does not meet the requirements because the element 9 is repeated. <br> - [9,9,9] which does not meet the requirements because the element 9 is repeated. <br> We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

- **Example 2:** <br>
**Input:** nums = [4,4,4], k = 3 <br>
**Output:** 0 <br>
**Explanation:** The subarrays of nums with length 3 are: <br> - [4,4,4] which does not meet the requirements because the element 4 is repeated. <br> We return 0 because no subarrays meet the conditions.
<hr>

### Constraints:
- <code>1 <= k <= nums.length <= 10<sup>5</sup></code>
- <code>1 <= nums[i] <= 10<sup>5</sup></code>
<hr>

### Hints:
- Which elements change when moving from the subarray of size k that ends at index i to the subarray of size k that ends at index i + 1?
- Only two elements change, the element at i + 1 is added into the subarray, and the element at i - k + 1 gets removed from the subarray.
- Iterate through each subarray of size k and keep track of the sum of the subarray and the frequency of each element.