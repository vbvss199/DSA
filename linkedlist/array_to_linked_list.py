class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def array_to_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node
    return head


def print_list(head_node):
    current = head_node
    while current is not None:
        print(current.data, end="->")
        current = current.next
    print("None")


if __name__ == "__main__":
    arr = [5, 6, 7, 8, 9, 10]
    head_node = array_to_linked_list(arr)
    print_list(head_node)
