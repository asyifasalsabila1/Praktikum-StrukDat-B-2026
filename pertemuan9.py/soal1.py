"""
Sistem daftar buku toko "Literasi"
Toko buku "Literasi" ingin mencatat daftar buku (judul & pengarang)
menggunakan Double Linked List agar bisa ditelusuri dari depan maupun belakang.
1. Buat class Node dengan atribut judul, pengarang, prev, dan next.
2. Buat fungsi insert_tail(), lalu tambahkan buku: Laskar Pelangi, Bumi Manusia,dan Sang Pemimpi.
3. Buat fungsi print_forward() dan print_backward(), lalu jalankan keduanya.
4. Buat fungsi delete_by_judul(), hapus buku "Bumi Manusia", lalu tampilkan list
kembali.

"""

# 1. Class Node
class Node:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.prev = None
        self.next = None

# 2. Class Double Linked List
class DoubleLinkedList:
    def __init__(self):
        self.head = None

    # insert_tail()
    def insert_tail(self, judul, pengarang):
        new_node = Node(judul, pengarang)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
        new_node.prev = temp

    # print_forward()
    def print_forward(self):
        temp = self.head
        while temp:
            print(f"{temp.judul} - {temp.pengarang}")
            temp = temp.next

    # print_backward()
    def print_backward(self):
        temp = self.head
        if temp is None:
            return
        
        while temp.next:
            temp = temp.next
        
        while temp:
            print(f"{temp.judul} - {temp.pengarang}")
            temp = temp.prev

    # delete_by_judul()
    def delete_by_judul(self, judul):
        temp = self.head
        
        while temp:
            if temp.judul == judul:
                if temp.prev is None:
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None
                else:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prev = temp.prev
                return
            temp = temp.next

# ======================
# Program Utama
# ======================

dll = DoubleLinkedList()

# Tambah data buku
dll.insert_tail("Laskar Pelangi", "Andrea Hirata")
dll.insert_tail("Bumi Manusia", "Pramoedya Ananta Toer")
dll.insert_tail("Sang Pemimpi", "Andrea Hirata")

print("LIST NAMA BUKU DAN PENGARANG SEBELUM DIHAPUS")
print("URUTAN MAJU")
dll.print_forward()

print("\nURUTAN MUNDUR")
dll.print_backward()

# Hapus buku
dll.delete_by_judul("Bumi Manusia")

print("\nLIST NAMA BUKU DAN PENGARANG SETELAH DIHAPUS")
print("URUTAN MAJU")
dll.print_forward()

print("\nURUTAN MUNDUR")
dll.print_backward()