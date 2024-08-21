// https://www.geeksforgeeks.org/problems/first-repeating-element4018/1

class Solution {
  // Function to return the position of the first repeating element.
  firstRepeated(arr) {
    // your code here
    let map = {};
    const n = arr.length;
    let res = n;
    for (let i = 0; i < n; i++) {
      if (arr[i] in map) {
        if (res > map[arr[i]]) res = map[arr[i]];
      } else {
        map[arr[i]] = i;
      }
    }
    return res === n ? -1 : res + 1;
  }
}
