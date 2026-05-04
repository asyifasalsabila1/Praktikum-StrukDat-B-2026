class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        '''Membuat Node terlebih dahulu'''
        rootA = Node('A')
        nodeB = Node('B')
        nodeC = Node('C')
        nodeD = Node('D')
        nodeE = Node('E')
        nodeF = Node('F')

        '''Menyusun tree sesuai instruksi'''
        self.root = rootA
        rootA.left = nodeB
        rootA.right = nodeC
        nodeB.left = nodeD
        nodeB.right = nodeE
        nodeC.right = nodeF

    def traverse_preorder(self, node):
        '''Pre-Order: Root -> Kiri -> Kanan'''
        if node is not None:
            print(node.data, end=" ")
            self.traverse_preorder(node.left)
            self.traverse_preorder(node.right)

    def traverse_inorder(self, node):
        '''In-Order: Kiri -> Root -> Kanan'''
        if node is not None:
            self.traverse_inorder(node.left)
            print(node.data, end=" ")
            self.traverse_inorder(node.right)

    def traverse_postorder(self, node):
        '''Post-Order: Kiri -> Kanan -> Root'''
        if node is not None:
            self.traverse_postorder(node.left)
            self.traverse_postorder(node.right)
            print(node.data, end=" ")

    def get_leaf_nodes(self, node, leaf):
        '''Mendapatkan leaf dari sebuah tree'''
        if node is not None:
            if node.left is None and node.right is None:
                leaf.append(node.data)
            self.get_leaf_nodes(node.left, leaf)
            self.get_leaf_nodes(node.right, leaf)

tree = BinaryTree()
tree.insert_manual()

print('SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI"')
print("==========================================")

print("\n[INFO] Membangun Struktur Gudang...")
print("[INFO] Struktur Berhasil Dibuat.")

print("HASIL AUDIT: ")

print("\n1. Traverse Pre-order: ", end=" ")
tree.traverse_preorder(tree.root)

print("\n2. Traverse In-order: ", end=" ")
tree.traverse_inorder(tree.root)

print("\n3. Traverse Post-order: ", end=" ")
tree.traverse_postorder(tree.root)

leaf = []
tree.get_leaf_nodes(tree.root, leaf)

print("\n[DATA] Gudang Ujung (Leaf Nodes): ", ', '.join(leaf))

print("\n==========================================")
print("Audit Selesai!")