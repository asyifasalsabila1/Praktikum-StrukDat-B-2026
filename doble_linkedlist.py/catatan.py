'''
class Node:
   def __init__(self, data):
        # To store the value or data.
        self.data = data

        # Reference to the previous node
        self.prev = None

        # Reference to the next node
        self.next = None
'''

#Sebuah linked list ganda memiliki node dengan alamat ke node sebelumnya dan node berikutnya,
#  seperti pada gambar di bawah, dan oleh karena itu membutuhkan lebih banyak memori. Namun, 
# linked list ganda bagus jika Anda ingin dapat bergerak ke atas dan ke bawah dalam list.


class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None

if __name__ == "__main__":
    # Create the first node (head of the list)
    head = Node(10)

    # Create and link the second node
    head.next = Node(20)
    head.next.prev = head

    # Create and link the third node
    head.next.next = Node(30)
    head.next.next.prev = head.next

    # Create and link the fourth node
    head.next.next.next = Node(40)
    head.next.next.next.prev = head.next.next

    # Traverse the list forward and print elements
    temp = head
    while temp is not None:
        print(temp.data, end="")
        if temp.next is not None:
            print(" <-> ", end="")
        temp = temp.next