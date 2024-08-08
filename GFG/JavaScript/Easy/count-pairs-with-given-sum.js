// https://www.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1

class Solution {
  getPairsCount(arr, k) {
    // code here
    let freq = {};
    let result = 0;

    for (const i of arr) {
      if (k - i in freq) {
        result += freq[k - i];
      }

      if (i in freq) {
        freq[i] += 1;
      } else {
        freq[i] = 1;
      }
    }
    return result;
  }
}
