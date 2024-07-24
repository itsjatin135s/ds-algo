// https://www.geeksforgeeks.org/problems/find-all-pairs-whose-sum-is-x5808/1

class Solution {
  allPairs(x, arr1, arr2) {
    // code here
    arr1.sort((a, b) => a - b);

    // Use a set to store elements of arr2 for quick lookup
    const arr2Set = new Set(arr2);

    const result = [];

    // Iterate through sorted arr1
    for (const u of arr1) {
      const v = x - u;
      if (arr2Set.has(v)) {
        result.push([u, v]);
      }
    }

    return result;
  }
}
