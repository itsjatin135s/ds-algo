// https://www.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1

class Solution {
  longestCommonPrefix(arr) {
    // code here
    let commonString = arr[0].length;

    for (let i = 0; i < arr.length - 1; i++) {
      let tempString = 0;
      for (let j = 0; j < Math.min(arr[i].length, arr[i + 1].length); j++) {
        if (arr[i][j] != arr[i + 1][j]) {
          commonString = Math.min(commonString, tempString);
        } else {
          tempString++;
        }
      }
    }
    return commonString > 0 ? arr[0].slice(0, commonString) : -1;
  }
}
