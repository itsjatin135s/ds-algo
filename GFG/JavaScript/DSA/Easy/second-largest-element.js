class Solution {
  // Function returns the second largest element
  getSecondLargest(arr) {
    // Code Here
    let max1 = arr[0];
    let max2 = -1;

    for (let i = 1; i < arr.length; i++) {
      if (arr[i] > max1) {
        max2 = max1;
        max1 = arr[i];
      } else if (arr[i] > max2 && arr[i] != max1) {
        max2 = arr[i];
      }
    }
    return max2;
  }
}
