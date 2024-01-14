class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end="")

        node = node.next

        if node:
            print(sep, end="")


def mergeLists(head1, head2):
    dummy = SinglyLinkedListNode(None)
    cur = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            cur.next, head1 = head1, head1.next
        else:
            cur.next, head2 = head2, head2.next

        cur = cur.next

    cur.next = head1 or head2

    return dummy.next


if __name__ == '__main__':
    tests = int(input("Enter the number of test cases: "))

    for _ in range(tests):
        llist1_count = int(input("Enter the length of the first linked list: "))

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input("Enter the length of the second linked list: "))

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        # Print the merged linked list
        print_singly_linked_list(llist3, ' ')

        # Print a newline after each test case
        print()
