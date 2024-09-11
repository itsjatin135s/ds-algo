// https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1

// Un-OPtimized Solution

class Solution {
  // Function to return the minimum cost of connecting the ropes.
  minCost(arr) {
    let res = [];
    while (arr.length > 1) {
      let min1 = arr.indexOf(Math.min(...arr));
      min1 = arr.splice(min1, 1)[0];

      let min2 = arr.indexOf(Math.min(...arr));
      min2 = arr.splice(min2, 1)[0];
      // console.log(min1, min2)
      arr.push(min1 + min2);
      res.push(min1 + min2);
    }
    return res.length > 0 ? res.reduce((acc, val) => acc + val, 0) : 0;
  }
}
