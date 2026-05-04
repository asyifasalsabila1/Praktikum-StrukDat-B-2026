"""
Sistem antrian kasir toko "Literasi"
Kasir toko menggunakan Circular Linked List untuk antrian pelanggan. Antrian
awal: Andi → Budi → Citra → Dina → (kembali ke Andi).
1. Buat class Node dengan atribut nama dan next. Buat fungsi insert_tail() dan
tambahkan 4 pelanggan.
2. Buat fungsi print_antrian() untuk menampilkan satu putaran antrian.
3. Tambahkan pelanggan baru Edo di akhir antrian menggunakan insert_tail(), lalu
tampilkan antrian.
4. Buat fungsi delete_head(), hapus Andi (sudah dilayani), lalu tampilkan antrian.
"""

# 1. Class Node
class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

# Class Circular Linked List
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # insert_tail()
    def insert_tail(self, nama):
        new_node = Node(nama)

        # jika list kosong
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        
        temp.next = new_node
        new_node.next = self.head

    # 2. print_antrian()
    def print_antrian(self):
        if self.head is None:
            return
        
        temp = self.head
        while True:
            print(temp.nama, end=", ")
            temp = temp.next
            if temp == self.head:
                break
        print("(kembali ke", self.head.nama + ")")

    # 4. delete_head()
    def delete_head(self):
        if self.head is None:
            return
        
        # jika hanya 1 node
        if self.head.next == self.head:
            self.head = None
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        
        # node terakhir menunjuk ke head baru
        temp.next = self.head.next
        self.head = self.head.next


# ======================
# Program Utama
# ======================

cll = CircularLinkedList()

# Tambah 4 pelanggan
cll.insert_tail("Andi")
cll.insert_tail("Budi")
cll.insert_tail("Citra")
cll.insert_tail("Dina")

print("ANTRIAN AWAL:")
cll.print_antrian()

# 3. Tambah Edo
cll.insert_tail("Edo")
print("\nSETELAH TAMBAH EDO:")
cll.print_antrian()

# 4. Hapus Andi
cll.delete_head()
print("\nSETELAH ANDI DILAYANI:")
cll.print_antrian()