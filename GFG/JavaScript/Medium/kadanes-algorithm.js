class Solution {
  // Function to find the sum of contiguous subarray with maximum sum.
  maxSubarraySum(arr) {
    // code here
    let max = -Infinity;
    let currMax = 0;

    for (let i = 0; i < arr.length; i++) {
      if (currMax < 0) {
        currMax = 0;
      }
      currMax += arr[i];
      if (max < currMax) {
        max = currMax;
      }
    }
    return max;
  }
}
