# -*- coding:utf-8 -*-
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next




'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result_list = ListNode(None)
        l3 = result_list.next
        flag = 0 
        while l1 and l2:
            if flag:
                if l1.val + l2.val + 1 < 10:
                    l3.val = l1.val + l2.val + 1
                    flag = 0
                else:
                    l3.val = l1.val + l2.val - 9 
                    flag = 1
            else:
                if l1.val + l2.val < 10:
                    l3.val = l1.val + l2.val
                    flag = 0
                else:
                    l3.val = l1.val + l2.val - 10
                    flag = 1
            l3.next = ListNode()
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next
        if l2:
            while l2:
                l3.val = l2.val + flag
                if l3.val >= 10:
                    flag = 1
                    l3.val -= 10
                else:
                    flag = 0
                l3.next = ListNode()
                l3 = l3.next
                l2 = l2.next
        if l1:
            while l1:
                l3.val = l1.val + flag
                if l3.val >= 10:
                    flag = 1
                    l3.val -= 10
                else:
                    flag = 0
                l3.next = ListNode()
                l3 = l3.next
                l1 = l1.next
'''
            
            