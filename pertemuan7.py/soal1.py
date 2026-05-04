# 1. Case: Sistem Riwayat Pencarian (Search History)
# Skenario: Anda sedang membuat fitur "Riwayat Pencarian" untuk sebuah browser. Setiap kali
# pengguna mencari sesuatu, kata kunci tersebut akan ditambahkan ke daftar riwayat. Pengguna bisa
# melihat riwayat dari yang paling baru hingga yang paling lama.
# Data Awal: ["google.com", "python.org"]

# Tugas 1: Implementasi Menggunakan List (Array) Python
# Gunakan tipe data list bawaan Python.
# 1. Buatlah sebuah list bernama history_array.
# 2. Buat fungsi tambah_pencarian_array(keyword) yang menambahkan kata kunci baru ke
# posisi paling depan (indeks 0).
# o Catatan: Di dalam Array, saat memasukkan data di depan, semua elemen di
# belakangnya harus bergeser.
# 3. Cetak isi history_array.

# Tugas 2: Implementasi Menggunakan Singly LinkedList
# Buatlah struktur manual menggunakan Class.
# 1. Buat class Node dan class HistoryLinkedList.
# 2. Buat metode tambah_pencarian_linked(keyword) yang menambahkan node baru di posisi
# Head.
# o Catatan: Di LinkedList, Anda hanya perlu mengubah pointer next node baru ke head
# lama.
# 3. Buat metode tampilkan_history() untuk mencetak riwayat.

#TUGAS 1
history_array = ["google.com", "python.org"]

def tambah_pencarian_array(keyword):
    history_array.insert(0, keyword)
    return history_array

print(tambah_pencarian_array("shoppe"))



#TUGAS 2

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class HistoryLinkedList:
    def __init__(self):
        self.head = None

def traverseAndPrint(head):
    currentPosition = head
    while currentPosition:
        print(currentPosition.data, end=" -> ")
        currentPosition = currentPosition.next
    print("null")

node1 = Node("shopee")
node2 = Node("google.com")
node3 = Node("python.org")

node1.next = node2
node2.next = node3

traverseAndPrint(node1)

def tambah_pencarian_linked(self, keyword):
    nodeBaru = Node(keyword)
    nodeBaru.next = self.head
    self.head = nodeBaru

def tampilkan_history(self):
    currentPosition = self.head
    while currentPosition:
        print(currentPosition.data)
        currentPosition = currentPosition.next