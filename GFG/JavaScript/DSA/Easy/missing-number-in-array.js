// https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1

class Solution {
  missingNumber(n, arr) {
    const sum = (n * (n + 1)) / 2;
    const arrSum = arr.reduce((a, b) => a + b, 0);
    return sum - arrSum;
  }
}
