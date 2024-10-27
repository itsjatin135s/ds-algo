class Solution {
  // Function to find sum of divisors
  sumOfDivisors(n) {
    // your code here
    let ans = 0;
    for (let i = 1; i <= n; i++) {
      for (let j = 1; j * j <= i; j++) {
        if (i % j === 0) {
          ans += j;
          // this will check that if this number is 2x of i and if not below we will add the complimentary number of that as well
          if (j !== i / j) {
            ans += i / j;
          }
        }
      }
    }
    return ans;
  }
}

/*
Explanation of above code

let day we are finding for 6
for divisor will be like

1, 2, 3, 6
so when we are at at 1 we see 1/6 != 6 so there must be a complimentary for that number as well which will be 6 and we don't have to go there
*/
