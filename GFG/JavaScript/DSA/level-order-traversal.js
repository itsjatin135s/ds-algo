// https://www.geeksforgeeks.org/problems/level-order-traversal/1

class Solution {
  //Function to return the level order traversal of a tree.
  levelOrder(root) {
    //your code here
    let res = [];
    let queue = [root];

    while (queue.length) {
      let node = queue.shift();
      res.push(node.data);

      if (node.left) {
        queue.push(node.left);
      }
      if (node.right) {
        queue.push(node.right);
      }
    }
    return res;
  }
}
