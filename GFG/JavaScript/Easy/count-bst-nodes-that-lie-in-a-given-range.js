// https://www.geeksforgeeks.org/problems/count-bst-nodes-that-lie-in-a-given-range/1

class Solution {
  //Function to count number of nodes in BST that lie in the given range.
  getCount(root, low, high) {
    //your code here
    let queue = [root];
    let res = 0;
    while (queue.length > 0) {
      root = queue.shift();
      if (root.data >= low && root.data <= high) res++;
      if (root.left) {
        queue.push(root.left);
      }
      if (root.right) {
        queue.push(root.right);
      }
    }
    return res;
  }
}

// Very Easy Not included in python folder...😅
