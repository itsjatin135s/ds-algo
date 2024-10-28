// Time Complexity O(NlogN)

function mergeSort(arr) {
  let n = arr.length;
  if (n <= 1) {
    return arr;
  }
  let middle = Math.floor(n / 2);
  let leftArr = arr.slice(0, middle);
  let rightArr = arr.slice(middle);

  return merge(mergeSort(leftArr), mergeSort(rightArr));
}

function merge(lArr, rArr) {
  let sortedArr = [];
  while (lArr.length && rArr.length) {
    if (lArr[0] > rArr[0]) {
      sortedArr.push(rArr.shift());
    } else {
      sortedArr.push(lArr.shift());
    }
  }
  return [...sortedArr, ...lArr, ...rArr];
}

let a = [5, 4, 3, 2, 1, 90, -90, 100, 40];

console.log(mergeSort(a));

class MergeSort {
  mergeSort(arr, low, high) {
    if (low >= high) {
      return;
    }
    let mid = Math.floor((low + high) / 2);
    mergeSort(arr, low, mid);
    mergeSort(arr, mid + 1, high);

    merge(arr, low, mid, high);
    return arr;
  }

  merge(arr, low, mid, high) {
    let sortedArr = [];
    let left = low;
    let right = mid + 1;
    while (left <= mid && right <= high) {
      if (arr[left] < arr[right]) {
        sortedArr.push(arr[left]);
        left++;
      } else {
        sortedArr.push(arr[right]);
        right++;
      }
    }
    while (left <= mid) {
      sortedArr.push(arr[left]);
      left++;
    }
    while (right <= high) {
      sortedArr.push(arr[right]);
      right++;
    }
    for (let i = 0; i < sortedArr.length; i++) {
      arr[low + i] = sortedArr[i];
    }
    return;
  }
}

// console.log(mergeSort([4, 3, 2, 1, 6], 0, 4));
