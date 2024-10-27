// https://www.geeksforgeeks.org/problems/key-pair5616/1

class Solution {
  hasArrayTwoCandidates(arr, x) {
    // code here
    let storage = new Set();

    for (const i of arr) {
      if (storage.has(x - i)) {
        return true;
      } else {
        storage.add(i);
      }
    }
    return false;
  }
}
