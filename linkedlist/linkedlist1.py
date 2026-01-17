class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(2)
second = Node(3)
third = Node(30)

# current state
# head   → [10 | None]
# second → [20 | None]
# third  → [30 | None]

# lets link them
head.next = second
second.next = third
third.next = None


# printing the linked list
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")
