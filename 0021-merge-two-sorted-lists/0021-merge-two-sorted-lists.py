# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def mergeTwoList(list1, list2):
            if not list1:
                return list2
            elif not list2:
                return list1
            elif list1.val <= list2.val:
                list1.next = mergeTwoList(list1.next, list2)
                return list1
            else:
                list2.next = mergeTwoList(list1, list2.next)
                return list2

        return mergeTwoList(list1,list2)

        