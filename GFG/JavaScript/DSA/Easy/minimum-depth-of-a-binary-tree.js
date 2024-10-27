// https://www.geeksforgeeks.org/problems/minimum-depth-of-a-binary-tree/1

class Solution {
  minDepth(root) {
    if (!root) {
      return 0;
    }
    let depth = 0;
    let queue = [root];
    while (queue.length > 0) {
      depth++;
      let levelNodes = queue.length;
      for (let i = 0; i < levelNodes; i++) {
        let node = queue.shift();

        if (node.left == null && node.right == null) {
          return depth;
        }
        if (node.left != null) {
          queue.push(node.left);
        }
        if (node.right != null) {
          queue.push(node.right);
        }
      }
    }
    return depth;
  }
}
