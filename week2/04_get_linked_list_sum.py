class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)


def get_linked_list_sum(linked_list_1, linked_list_2):
    sum1= _get_linked_List_sum(linked_list_1)
    sum2= _get_linked_List_sum(linked_list_2)
    return sum1+sum2

def _get_linked_List_sum(Linked_List):
    sum= 0
    head= Linked_List.head
    while head is not None:
        sum = sum * 10 + head.data

        head=head.next
    return sum

linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)
#  6 > 7 > 8
linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)
# 3 > 5 > 4 
print(get_linked_list_sum(linked_list_1, linked_list_2))