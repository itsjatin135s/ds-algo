class Solution {
  // Function to reverse a linked list.
  reverseList(head) {
    // your code here
    let node = head;
    let prev = null;

    while (node) {
      const temp = node.next;
      node.next = prev;
      prev = node;
      node = temp;
    }
    return prev;
  }
}
