/*

Given a base-10 integer as a string, parse the integer and return it as an int. This problem can be done iteratively and recursively, and it's worth doing both! 

Example(s)

atoi("123") == 123

atoi("4") == 4

atoi("007") == 7

atoi("-1") == -1

🛠️ IMPLEMENT

def atoi(intAsString: str) -> int:

*/

const numsMap = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
  }
  
  const aToI = (str) => {
    let total = 0;
    const isNeg = str[0] === '-'
    const absValueStr = isNeg ? str.slice(1) : str;
    
    for (let i = 0; i < absValueStr.length; i++) {
      const multiplier = Math.pow(10, i)
      const digitChar = absValueStr[absValueStr.length - i - 1]
      total += multiplier * numsMap[digitChar]
    }
  
    return isNeg ? total * -1 : total;
  }
  
  /*
  
  input: "-123"
  isNeg: true
  absValueStr: "123"
  total: 123
  return -123
  
  helper("123", 0):     subTotal: 120   multiplier: 1   digitChar: "3" => return 120 + (1 * 3) => 123
    helper("123", 1):     subTotal: 100     multiplier: 10      digitChar: "2" => return 100 + (10 * 2) => 120
      helper("123", 2):       subTotal: 0       multiplier: 100   digitChar: "1" => return 0 + (100 * 1) => return 100
        helper("123", 3) => return 0
  
  */
  const aToIRecursive = (input) => {
    const isNeg = input[0] === '-'
    const absValueStr = isNeg ? input.slice(1) : input;
  
    const helper = (str, idx) => {
      if (idx === str.length) {
        return 0;
      }
  
      const subTotal = helper(str, idx + 1);
      const multiplier = Math.pow(10, idx)
      const digitChar = str[str.length - idx - 1]
  
      return subTotal + (multiplier * numsMap[digitChar])
    }
  
    const total = helper(absValueStr, 0)
    return isNeg ? total * -1 : total;
  }
  
  console.log(aToIRecursive("123"))
  console.log(aToIRecursive("4"))
  console.log(aToIRecursive("007"))
  console.log(aToIRecursive("-1"))
  
  /*
  
  Given a non-negative integer represented as a linked list of digits, plus one to the integer.
  
  The digits are stored such that the most significant digit is at the head of the list.
  
  Example 1:
  
  Input: head = [1,2,3]
  Output: [1,2,4]
  Example 2:
  
  Input: head = [0]
  Output: [1]
  
  recurse until we hit the end
  
  */
  // # Definition for singly-linked list.
  // # class ListNode:
  // #     def __init__(self, val=0, next=None):
  // #         self.val = val
  // #         self.next = next
  // class Solution:
  
  /*
  
  0 -> 0 -> null
  
  addOneToLL(5) return 0
  
  */
  
  class LLNode {
    constructor(val, next = null) {
      this.val = val;
      this.next = next;
    }
  }
  
  const testList = new LLNode(9, new LLNode(9, new LLNode(9)))
  
  const addOneToLL => (head) => {
    const helper = (node) => {
      if (!node) {
        return 0;
      }
  
      const carry = addOneToLL(node.next);
      if (node.val === 9) {
        node.val = 0;
        return 1;
      } else {
        node.val = node.val + 1;
        return 0;
      }
    }
  
    const newNodeVal = helper(head);
  
    if (newNodeVal === 1) {
      const newHead = new LLNode(1, head);
      return newHead;
    } else {
      return head;
    }
  }
  
  class BSTNode {
    constructor(val, left = null, right = null) {
      this.val = val;
      this.left = left;
      this.right = right;
    }
  }
  
  /*
  
            1
        12        15
    2     3             7
            5
  
  */
  
  const testTree = new BSTNode(1,
    new BSTNode(12,
      new BSTNode(2),
      new BSTNode(3,
        null,
        new BSTNode(5)
      )
    ),
    new BSTNode(15,
      null,
      new BSTNode(7)
    )
  );