# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        temp = None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            temp = list1
            temp.next = Solution.mergeTwoLists(self,list1.next, list2)

        else:

            temp = list2
            temp.next = Solution.mergeTwoLists(self,list1, list2.next)

        return temp
