class Node:
    def __init__(self, data):
        self.data = data
        self.next_link = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_mode = Node(data)
        if self.head is None:
            self.head = new_mode
        else:
            old_head = self.head
            self.head = new_mode
            self.head.next_link = old_head
    
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        
        else:
            last_elem = self.head
            while last_elem.next_link is not None:
                last_elem = last_elem.next_link

            last_elem.next_link = new_node

    def display(self):
        current = self.head
        if current is None:
            print("None")
        else:
            while current.next_link is not None:
                print(current.data, end=" -> ")
                current = current.next_link
            print("None")

lst = SingleLinkedList()
lst.display()

lst.append(5)
lst.append(13)
lst.append("boat")

lst.display()

lst.append(2)
lst.display()
print()

lst.push(9)
lst.display()