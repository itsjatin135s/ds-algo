// https://www.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1

/* My approach 
   So I am trying to look  through all the array elements and if the numbers are same doing the splice to remove the duplicate
   which is good but a bit time consuming for big array because inside a for loop I am doing a splice which again take O(index) time so total time become 
   O(n* variableIndex)
*/

let arr = [32, 40, 43, 60, 72, 78, 82, 82, 82, 99];

function remove_duplicate(arr) {
  // Code Here
  let index = 0;
  console.log(arr.length);
  for (let i = 1; i <= arr.length; ) {
    if (arr[index] === arr[i]) {
      let removed = arr.splice(i, 1);
      console.log("removed : ", removed);
    } else {
      index++;
      i++;
    }
  }
  return arr.length;
}

console.log(remove_duplicate(arr));

/* Better Approach
    We keep a uniqueIndex that points to the position where the next unique element should go.
    We iterate through the array starting from the second element.
    When we find a non-duplicate element, we place it at the uniqueIndex and increment the uniqueIndex.
    Finally, we trim the array to the length of uniqueIndex.

    This approach ensures that the array is modified in place without using additional space for a new array.
*/

let arr2 = [32, 40, 43, 60, 72, 78, 82, 82, 82, 99, 99];
// console.log(arr.splice(2))
function remove_duplicate2(arr) {
  // Code Here
  let uniqueIndex = 1;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] !== arr[i - 1]) {
      arr[uniqueIndex] = arr[i];
      uniqueIndex++;
    }
  }
  arr.splice(uniqueIndex); // if need to return the arr of unique elements otherwise not necessary.
  return uniqueIndex;
}
console.log(remove_duplicate2(arr));
