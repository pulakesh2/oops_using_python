
from typing import TypeVar, Generic


T = TypeVar('T')


# create a generic node class
class Node(Generic[T]):
    def __init__(self, data: T):
        self.data : T = data
        self.next: Node[T] = None



# create a generic linked list class
class LinkedList(Generic[T]):
    # constructor to initialize the linked list
    def __init__(self):
        self.head: Node[T] = None


    # method to add a new node to the linked list
    def add(self, data: T) -> None:
        new_node: Node[T] = Node(data)

        if self.head is None:
            self.head = new_node
        
        else:
            temp: Node[T] = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node
    
    # method to display the linked list
    def display(self) -> None:

        temp : Node[T] = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

    # method to check if the linked list is empty
    def is_empty(self) -> bool:
        return self.head is None
    

    # method to get the size of the linked list
    def size(self) -> int:
        size: int = 0

        temp: Node[T] = self.head

        while temp is not None:
            size += 1
            temp = temp.next

        return size
    


if __name__ == "__main__":
    # create a linked list of integers
    int_list: LinkedList[int] = LinkedList()
    int_list.add(1)
    int_list.add(2)
    int_list.add(3)

    print("Integer Linked List:")
    int_list.display()
    print(f"Size of Integer Linked List: {int_list.size()}")
    print(f"Is Integer Linked List empty? {int_list.is_empty()}")

    # create a linked list of strings
    str_list: LinkedList[str] = LinkedList()
    str_list.add("Hello")
    str_list.add("World")
    str_list.add("!")

    print("\nString Linked List:")
    str_list.display()
    print(f"Size of String Linked List: {str_list.size()}")
    print(f"Is String Linked List empty? {str_list.is_empty()}")