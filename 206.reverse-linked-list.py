# @before-stub-for-debug-begin
from python3problem206 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1 → 2 → 3 → Ø


class Solution:
    def reverseList(self, head):
        currentNode = head
        prev = None
        while currentNode:
            nxt = currentNode.next
            # severing the link and using this to chain
            # 1-> None
            # 2 -> 1 → None etc
            currentNode.next = prev
            # updating the value to our current node
            prev = currentNode
            # updating to the saved value
            currentNode = nxt
        return prev


# @lc code=end
