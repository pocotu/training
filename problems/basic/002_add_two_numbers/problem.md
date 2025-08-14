# Add Two Numbers

## Problem Description

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Examples

### Example 1:
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

### Example 2:
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

### Example 3:
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

## Constraints

- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

## Hints

1. Since the digits are stored in reverse order, we can process them from left to right.
2. Keep track of carry when the sum of two digits exceeds 9.
3. Handle cases where one linked list is longer than the other.
4. Don't forget to add the final carry if it exists.

## Related Topics

- Linked List
- Math
- Recursion

## Companies

- Amazon
- Microsoft
- Facebook
- Google
- Apple

## Follow Up

What if the linked list digits are stored in forward order? For example:
```
(3 -> 4 -> 2) + (4 -> 6 -> 5) = (8 -> 0 -> 7)
```
