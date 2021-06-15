class LinkedList:
    def __init__(self):
        self.head = None


    def create_ll(self, array):
        if self.head is None:
            self.head = Node(array[0])
        if len(array) > 0:
            curr = self.head
            for i in array[1:]:
                curr.next = Node(i)
                curr = curr.next


    def print_ll(self):
        curr = self.head
        print(f'The head is {self.head.data}\n\n')
        while curr:
            if curr.next is None:
                print(curr.data)
            else:
                print(curr.data, end=' --> ')
            curr = curr.next

    def fill_ll(self, start):
        count = 0
        


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



if __name__ == '__main__':
    arr = '. R . . . .'.split()
    ll = LinkedList()
    ll.create_ll(arr)
    ll.print_ll()
    # t = int(input())
    # for _ in range(t):
    #     n, m = list(map(int, input().split()))
    #     arr = []
    #     for i in range(n):
    #         x = input()
    #         for ch in range(len(x)):
    #             if x[ch] == 'R' or x[ch] == 'W':
    #                 print(ch, i + 1, sep=" - ", end=" ** ")
    #         arr.append(x)
    #
    #     print('\n\n')
