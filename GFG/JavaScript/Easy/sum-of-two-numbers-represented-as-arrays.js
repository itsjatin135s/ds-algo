// https://www.geeksforgeeks.org/problems/sum-of-two-numbers-represented-as-arrays3110/1

class Solution {
  findSum(arr1, arr2) {
    // code here
    let carry = 0;
    let res = [];

    arr1 = arr1.reverse();
    arr2 = arr2.reverse();

    const n = Math.max(arr1.length, arr2.length);

    for (let i = 0; i < n; i++) {
      const num1 = arr1[i] ? arr1[i] : 0;
      const num2 = arr2[i] ? arr2[i] : 0;
      const sum = num1 + num2 + carry;
      if (sum >= 10) {
        carry = 1;
        res.push(sum - 10);
        continue;
      }
      res.push(sum);
      carry = 0;
    }
    if (carry) res.push(carry);

    return res.reverse();
  }
}
