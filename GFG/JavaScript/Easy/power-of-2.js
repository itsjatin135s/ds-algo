// https://www.geeksforgeeks.org/problems/power-of-2-1587115620/1

class Solution {
  // Function to check if given number n is a power of two.
  isPowerOfTwo(n) {
    // code here
    let num = 0;
    while (Math.pow(2, num) <= n) {
      if (Math.pow(2, num) == n) {
        return true;
      }
      num++;
    }
    return false;
  }
}
