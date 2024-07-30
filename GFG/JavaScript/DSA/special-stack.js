// https://www.geeksforgeeks.org/problems/special-stack/1

class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class SpecialStack {
  constructor(n) {
    this.stackLength = n;
    this.currLength = 0;
    this.head = null;
    this.tail = null;
  }
  /**
   * @param {number} x
   * @return {void}
   */
  push(x) {
    if (this.isFull()) {
      return false;
    }
    if (this.isEmpty()) {
      this.head = new Node(x);
      this.tail = this.head;
    } else {
      let node = new Node(x);
      this.tail.next = node;
      this.tail = node;
      // console.log(this.tail.data)
    }
    this.currLength++;
    return true;
  }
  /**
   * @return {number}
   */
  pop() {
    if (this.isEmpty()) {
      return false;
    } else {
      let node = this.head;
      this.head = this.head.next;
      this.currLength--;
    }
    return node.data;
  }

  /**
   * @return {boolean}
   */

  isFull() {
    return this.currLength == this.stackLength;
  }
  /**
   * @return {boolean}
   */
  isEmpty() {
    return this.head === null;
  }
  /**
   * @return {number}
   */
  getMin() {
    if (this.isEmpty()) {
      return false;
    }
    let minNum = this.head.data;
    let node = this.head;
    while (node) {
      minNum = Math.min(minNum, node.data);
      node = node.next;
    }
    return minNum;
  }
}
