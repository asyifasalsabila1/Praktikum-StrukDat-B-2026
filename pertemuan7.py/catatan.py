
#PYTHON Lists 
'''
Di Python, list adalah struktur data bawaan yang berfungsi sebagai array dinamis
Daftar (list) bersifat terurut, dapat diubah (mutable), dan dapat berisi elemen dengan tipe yang berbeda.
Daftar
Daftar adalah struktur data bawaan di Python, yang digunakan untuk menyimpan banyak elemen
Daftar digunakan oleh banyak algoritma.
'''
'''
Membuat Daftar
Daftar dibuat menggunakan tanda kurung siku []:
ContohDapatkan server Python Anda sendiri
'''
# Empty list
x = []

# List with initial values
y = [1, 2, 3, 4, 5]

# List with mixed types
z = [1, "hello", 3.14, True]

'''
Metode Daftar
Daftar Python dilengkapi dengan beberapa algoritma bawaan (disebut metode) untuk melakukan operasi umum seperti menambahkan, mengurutkan, dan banyak lagi
Contoh
Tambahkan satu elemen ke dalam daftar, lalu urutkan daftar tersebut secara menaik:
'''

x = [9, 12, 7, 4, 11]

# Add element:
x.append(8)

# Sort list ascending:
x.sort()

'''
Membuat Algoritma
Terkadang kita ingin melakukan tindakan yang tidak tersedia di Python
Kemudian kita dapat membuat algoritma kita sendiri .Sebagai contoh, algoritma dapat digunakan untuk menemukan nilai terendah dalam sebuah daftar, seperti pada contoh di bawah ini:

Contoh
Buatlah algoritma untuk menemukan nilai terendah dalam sebuah daftar:
'''

my_array = [7, 12, 9, 4, 11, 8]
minVal = my_array[0]

for i in my_array:
  if i < minVal:
    minVal = i

print('Lowest value:', minVal)


#Linked Lists 
#sebuah tipe data yang saling terhubung yang ada isi nya , dan ada list selanjutnya 
'''
Jenis-Jenis Linked List
Ada tiga bentuk dasar linked list:

- Daftar berantai tunggal
- Daftar berantai ganda
- Daftar berantai melingkar
- Daftar berantai tunggal adalah jenis daftar berantai yang paling sederhana. 
- Daftar ini membutuhkan lebih sedikit ruang memori karena setiap node hanya memiliki satu alamat ke node berikutnya, seperti pada gambar di bawah
'''


#penelusuran di linked 
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1)

#Mencari nilai terendah dalam linked list tunggal di Python:

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def findLowestValue(head):
  minValue = head.data
  currentNode = head.next
  while currentNode:
    if currentNode.data < minValue:
      minValue = currentNode.data
    currentNode = currentNode.next
  return minValue

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("The lowest value in the linked list is:", findLowestValue(node1))

#Menghapus node tertentu dalam linked list tunggal di Python:

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def deleteSpecificNode(head, nodeToDelete):
  if head == nodeToDelete:
    return head.next

  currentNode = head
  while currentNode.next and currentNode.next != nodeToDelete:
    currentNode = currentNode.next

  if currentNode.next is None:
    return head

  currentNode.next = currentNode.next.next

  return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before deletion:")
traverseAndPrint(node1)

# Delete node4
node1 = deleteSpecificNode(node1, node4)

print("\nAfter deletion:")
traverseAndPrint(node1)

#Menyisipkan node ke dalam linked list tunggal di Python:

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def insertNodeAtPosition(head, newNode, position):
  if position == 1:
    newNode.next = head
    return newNode

  currentNode = head
  for _ in range(position - 2):
    if currentNode is None:
      break
    currentNode = currentNode.next

  newNode.next = currentNode.next
  currentNode.next = newNode
  return head

node1 = Node(7)
node2 = Node(3)
node3 = Node(2)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

print("Original list:")
traverseAndPrint(node1)

# Insert a new node with value 97 at position 2
newNode = Node(97)
node1 = insertNodeAtPosition(node1, newNode, 2)

print("\nAfter insertion:")
traverseAndPrint(node1)




# Class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Class Linked List
class HistoryLinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan pencarian di posisi head
    def tambah_pencarian_linked(self, keyword):
        node_baru = Node(keyword)
        node_baru.next = self.head
        self.head = node_baru

    # Menampilkan riwayat pencarian
    def tampilkan_history(self):
        current = self.head
        print("Riwayat Pencarian (Linked List):")
        while current:
            print(current.data)
            current = current.next


# Membuat objek Linked List
history_linked = HistoryLinkedList()

# Data awal
history_linked.tambah_pencarian_linked("python.org")
history_linked.tambah_pencarian_linked("google.com")

# Menambahkan pencarian baru
history_linked.tambah_pencarian_linked("stackoverflow.com")
history_linked.tambah_pencarian_linked("github.com")

# Menampilkan riwayat
history_linked.tampilkan_history()
