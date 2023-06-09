# Definition for singly-linked list.
from LinkedList import ListNode, BaseSolution
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

class Solution(BaseSolution):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 初始化个位节点，先不做进位
        newPoint = ListNode(l1.val + l2.val)

        # tp用来遍历节点
        tp = newPoint

        # l1,l2只要后面还有节点，就继续往后遍历；或者新链表还需要继续往后进位
        while (l1 and l1.next) or (l2 and l2.next) or (tp.val > 9):
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
            # 计算下个节点的和，先不考虑这个节点是否进位
            tmpsum = (l1.val if l1 else 0) + (l2.val if l2 else 0)
            # 计算新链表下个节点的值（当前节点的进位+当前l1 l2的值之和），先不做进位，//表示整除，抛弃余数，用于进位
            tp.next = ListNode(tp.val // 10 + tmpsum)
            # 新链表当前节点的值取个位
            tp.val %= 10
            # 新链表往后遍历一个节点
            tp = tp.next

        return newPoint


if __name__ == '__main__':
    sol = Solution()
    l1 = sol.create_linklist_tail([2, 4, 3])
    l2 = sol.create_linklist_tail([5, 6, 4])

    res = sol.addTwoNumbers(l1, l2)
    sol.print_LinkedList(res)
