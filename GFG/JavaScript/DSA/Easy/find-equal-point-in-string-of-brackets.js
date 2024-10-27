// https://www.geeksforgeeks.org/problems/find-equal-point-in-string-of-brackets2542/1

class Solution {
  //Your code goes here
  findIndex(str) {
    let n = str.length;

    // Step 1: Calculate total number of closing brackets
    let totalClosing = 0;
    for (let i = 0; i < n; i++) {
      if (str[i] === ")") totalClosing++;
    }

    // Initialize counters
    let openingCount = 0;
    let closingCount = totalClosing;

    // Step 2: Iterate through the string
    for (let i = 0; i < n; i++) {
      if (str[i] === "(") {
        openingCount++;
      } else if (str[i] === ")") {
        closingCount--;
      }

      // Step 3: Check for the equal point
      if (openingCount === closingCount) {
        return i + 1; // Return 1-based index
      }
    }

    return 0; // No equal point found
  }
}
