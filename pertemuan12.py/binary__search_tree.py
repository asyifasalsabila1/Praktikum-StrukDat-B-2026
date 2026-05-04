class Node:
    def __init__(self, id_buku, judul):
        self.id = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, id_buku, judul):
        '''Fungsi untuk menambahkan judul buku baru beserta ID-nya'''
        def _insert(node, id_buku, judul):
            if node is None:
                print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
                return Node(id_buku, judul)
            
            if id_buku < node.id:
                node.left = _insert(node.left, id_buku, judul)
            elif id_buku > node.id:
                node.right = _insert(node.right, id_buku, judul)
            return node
        
        self.root = _insert(self.root, id_buku, judul)

    def search(self, id_buku):
        '''Fungsi untuk mencari judul buku yang sudah ditambahkan berdasarkan ID'''
        def _search(node, id_buku):
            if node is None:
                return None
            if id_buku == node.id:
                return node
            elif id_buku < node.id:
                return _search(node.left, id_buku)
            else:
                return _search(node.right, id_buku)
            
        return _search(self.root, id_buku)

    def traversal_inorder(self):
        '''Fungsi untuk mengurutkan buku berdasarkan ID, terkecil hingga terbesar'''
        self.no = 1

        def _inorder(node):
            if node is not None:
                _inorder(node.left)
                print(f"{self.no}. {node.id} - {node.judul}")
                self.no += 1
                _inorder(node.right)

        _inorder(self.root)

    def get_min(self):
        '''Fungsi untuk menemukan ID buku terkecil'''
        node = self.root
        while node and node.left is not None:
            node = node.left
        return node
    
    def get_max(self):
        '''Fungsi untuk menemukan ID buku terbesar'''
        node = self.root
        while node and node.right is not None:
            node = node.right
        return node

    def height(self):
        '''Fungsi untuk menghitung total ketinggian dari tree yang sudah dibentuk'''
        def _height(node):
            if node is None:
                return -1
            return 1 + max(_height(node.left), _height(node.right))
        
        return _height(self.root)
    
BST = BinarySearchTree()

print('SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"')
print("============================================")

BST.insert(50, "Dasar Pemrograman")
BST.insert(30, "Struktur Data")
BST.insert(70, "Kecerdasan Buatan")
BST.insert(20, "Matematika Diskrit")
BST.insert(40, "Basis Data")
BST.insert(60, "Jaringan Komputer")
BST.insert(80, "Sistem Operasi")
print("...")

print("\n[INFO] Koleksi Buku (In-0rder Traversal): ")
BST.traversal_inorder()
print("...")

cari = 60
hasil = BST.search(cari)
print(f"[SEARCH] Mencari ID {cari}... Ditemukan! Judul: {hasil.judul}")

cari2 = 100
hasil2 = BST.search(cari2)
if hasil2:
    print(f"[SEARCH] Mencari ID {cari2}... Ditemukan! Judul: {hasil2.judul}")
else:
    print(f"[SEARCH] Mencari ID {cari2}... Data Tidak Ditemukan.")

mins = BST.get_min()
maks = BST.get_max()
print(f"\n[STATISTIK] ID Terkecil: {mins.id}")
print(f"[STATISTIK] ID Terbesar: {maks.id}")
print("[INFO] Tinggi (Height) Tree: ", BST.height())

print("============================================")
print("Simulasi Selesai!")