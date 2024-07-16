// https://www.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1

// Correct Solution :
/*
    Initialization:
        minLength is initialized to n + 1, which is larger than any possible subarray length.
        currentSum is initialized to 0 to keep track of the sum of the current window.
        start is initialized to 0 to denote the starting index of the current window.
    Expand Window:
        The end pointer is used to expand the window by adding arr[end] to currentSum.
    Shrink Window:
        When currentSum becomes greater than x, the inner while loop tries to shrink the window from the left side by moving the start pointer to the right.
        During this process, minLength is updated if the current window size is smaller than the previously recorded minLength.
    Result:
        If minLength is still n + 1, it means no valid subarray was found, so it returns 0. Otherwise, it returns minLength.

    This solution ensures that each element is processed at most twice, resulting in O(n)O(n) time complexity.
*/

const smallestSubWithSum = (arr, x) => {
  let n = arr.length;
  let minLength = n + 1;
  let currSum = 0;
  let start = 0;

  for (let end = 0; end < n; end++) {
    currSum += arr[end];

    while (currSum > x) {
      minLength = Math.min(minLength, end - start + 1);
      currSum -= arr[start];
      start++;
    }
  }
  return minLength == n + 1 ? 0 : minLength;
};

//  My Wrong approach
/*
            assign a number and then add the following number to it is the 
            income number is bigger then the outgoing number then remove the 
            outgoing number.
            
            first add the number and check if it's greater then the given number
            then do not perform above operation.
            
            also keep the track of the length of the subarray used
            assign a initial minLengthSubArray = 0;
            
            though you find the subArray there might be some other subarray which is
            smaller then the currSolution
            
            so to solve this loop through whole array and after looping whole array
            return the minLengthSubArray at the end irrespective of the condition
            because if there is no subarray it's already 0
*/

// Problems
/*
    So basically it wont be able to find the smallest subarray if the smallest numbers needs to be included.
    Example -     
    let arr = [2,3,1]
    let x = 6

    Here it will remove 2 after it see 3 is bigger then 2 and its the next element.
*/
