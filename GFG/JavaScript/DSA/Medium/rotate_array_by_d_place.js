// Brute Force
function rotateArrToRightByDPlace(arr, d) {
  let n = arr.length;
  d = d % n;

  if (d < 1) {
    return arr;
  }
  n = n - 1;
  let temp = [];
  for (let i = n - d + 1; i <= n; i++) {
    temp.push(arr[i]);
  }
  console.log("temp -> ", temp);

  let j = n;
  for (let i = n - d; i >= 0; i--) {
    arr[j] = arr[i];
    j--;
  }

  console.log("arr -> ", arr);
  //   j = 0;
  for (let i = 0; i < d; i++) {
    arr[i] = temp[i];
    // j++;
  }
  return arr;
}

// Optimized for space complexity
function rotateArrToRightByDPlaceOptimized(arr, d) {
  if (d < 1) {
    return arr;
  }
  const n = arr.length - 1;
  d = d % (n + 1);
  reverse(arr, 0, n - d);
  reverse(arr, n - d + 1, n);
  reverse(arr, 0, n);
  return arr;
}

function reverse(arr, start, end) {
  while (start < end) {
    temp = arr[start];
    arr[start] = arr[end];
    arr[end] = temp;
    start++;
    end--;
  }
  return arr;
}

test1 = [-1, -100, 3, 99]; // d = 2
test2 = [1, 2, 3, 4, 5, 6, 7]; //d = 3
test3 = [1, 2]; //d = 0
test4 = [1, 2, 3, 4, 5, 6]; //d = 1

console.log(rotateArrToRightByDPlaceOptimized(test4, 1));
