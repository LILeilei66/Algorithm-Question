"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

l1=[9,9] + l2=[1] => 100

list1 = [0, 8, 6, 5, 6, 8, 3, 5, 7]
list2 = [6, 7, 8, 0, 8, 5, 8, 9, 7]

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        answer_list = []
        pointer1 = l1
        pointer2 = l2
        carry = 0
        while pointer1 is not None or pointer2 is not None:
            try:
                val1 = pointer1.val
            except AttributeError:
                val1 = 0
            try:
                val2 = pointer2.val
            except AttributeError:
                val2 = 0
            result = val1 + val2 + carry

            answer_list.append(result % 10 )
            try:
                pointer1 = pointer1.next
            except AttributeError:
                pointer1 = None
            try:
                pointer2 = pointer2.next
            except AttributeError:
                pointer2 = None
            carry = result // 10
        if carry != 0:
            answer_list.append(carry)

        return answer_list

if __name__ == '__main__':
    # <editor-fold desc="case 1">
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    solution = Solution()
    solution.addTwoNumbers(l1,l2)
    # </editor-fold>

    # <editor-fold desc="case 2">
    l1 = ListNode(1)
    l1.next = ListNode(8)
    l2 = ListNode(0)
    solution.addTwoNumbers(l1, l2)
    # </editor-fold>

    # <editor-fold desc="case 3">
    l1 = ListNode(9)
    l1.next = ListNode(9)
    l2 = ListNode(1)
    solution.addTwoNumbers(l1, l2)
    # </editor-fold>

