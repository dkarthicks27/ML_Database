class Solution:
    @staticmethod
    def getDecimalValue(head):
        curr = head
        deci = []
        while curr:
            deci.append(curr.val)
            curr = curr.next
        return int(''.join(map(str, deci)), 2)
