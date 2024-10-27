// https://www.geeksforgeeks.org/problems/find-first-and-last-occurrence-of-x0849/1

function indexes(v, x) {
  let res = [-1, -1];
  let left_index = 0;
  let right_index = v.length - 1;
  let res_index;
  let middle_index;
  while (left_index <= right_index) {
    middle_index = Math.floor((left_index + right_index) / 2);
    if (x == v[middle_index]) {
      res_index = middle_index;
      break;
    } else if (x > v[middle_index]) {
      left_index = middle_index + 1;
    } else {
      right_index = middle_index - 1;
    }
  }
  console.log(res_index);
  if (res_index >= 0) {
    res = [res_index, res_index];
    console.log(res);
    while (v[res_index] == v[res_index - 1]) {
      res[0] = res_index - 1;
      res[1] = res_index - 1;
      res_index = res_index - 1;
    }
    while (v[res_index] == v[res_index + 1]) {
      res[1] = res_index + 1;
      res_index = res_index + 1;
    }
  }
  return res;
}

console.log(indexes([1, 2, 3, 5, 5, 5], 1));
