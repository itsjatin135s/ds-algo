// https://www.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1

// Much Efficient approach require only O(n/2) traversal
class Solution {
  /* Should return data of middle node. If linked list is empty, then  -1*/
  getMiddle(node) {
    // your code here
    let slow = node;
    let fast = node;

    while (fast && fast.next) {
      slow = slow.next;
      fast = fast.next.next;
    }
    return slow.data;
  }
}

// Though is O(n) but a require 2 traversal

class Solution {
  /* Should return data of middle node. If linked list is empty, then  -1*/
  getMiddle(node) {
    // your code here
    const middleIndex = Math.floor(this.getListLength(node) / 2);

    let currIndex = 0;
    while (currIndex < middleIndex) {
      node = node.next;
      currIndex++;
    }
    return node.data;
  }
  getListLength(node) {
    let length = 0;
    let currNode = node;
    while (currNode) {
      currNode = currNode.next;
      length++;
    }
    return length;
  }
}
