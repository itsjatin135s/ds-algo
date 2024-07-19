// https://www.geeksforgeeks.org/problems/check-if-two-strings-are-k-anagrams-or-not/1

// Inefficient Solution

class Solution {
  areKAnagrams(str1, str2, k) {
    //code here
    let changes = 0;
    if (str1.length !== str2.length) {
      return false;
    }
    let index;
    str2 = str2.split("");
    for (const i of str1) {
      index = str2.indexOf(i);
      if (index > -1) {
        str2.splice(index, 1);
        continue;
      } else {
        changes++;
      }
      if (changes > k) {
        return false;
      }
    }
    return true;
  }
}

/*
The above implementation uses indexOf and splice, which are costly operations within a loop, leading to a higher time complexity.
*/

// Appropriate Solution

class Solution {
  areKAnagrams(str1, str2, k) {
    //code here
    let changes = 0;
    if (str1.length !== str2.length) {
      return false;
    }
    let count1 = new Array(26).fill(0);
    let count2 = new Array(26).fill(0);
    for (let i = 0; i < str1.length; i++) {
      count1[str1.charCodeAt(i) - "a".charCodeAt(0)]++;
      count2[str2.charCodeAt(i) - "a".charCodeAt(0)]++;
    }
    for (let i = 0; i < 26; i++) {
      if (count1[i] > count2[i]) {
        changes += count1[i] - count2[i];
      }
    }
    return changes <= k;
  }
}

// charCodeAt(i) : The charCodeAt() method of String values returns an integer between 0 and 65535 representing the UTF-16 code unit at the given index.
