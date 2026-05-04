#implementasi Binary tree
class Node :
    """Representasi satu node dalam binary tree"""
    def __init__(self,data):
        self.data = data 
        data.left = None
        self.right.right =None 


class BinaryTree :
    """Implementasi Binary Tree"""
    def __init__(self):
        self.root = None


    def insert_root(self,data):
        self.root = Node (data)


    def insert_left(self,parent_node,data):
        """Memasukkan child kiri dari suatu node"""
        if parent_node.left is None :
           parent_node.left = Node (data)
        else:
            new_node= Node(data)
            new_node.left = new_node


    def insert_right(self,parent_node,data):
        """ memasukkan child kanan dwari suatu node"""
        if parent_node.right is None :
            parent_node.right = Node(data)
        else:  
            new_node =Node (data)
            new_node.right =parent_node.right
            parent_node.right = new_node

            tree = BinaryTree()

            #membuat struktur tree:
            #         10
            #       /   \
            #       5    15
            #       /     \
            #       3      7

            tree.insert_root(10)
            tree.insert_left(tree.root, 5)
            tree.insert_right(tree.root, 15)
            tree.insert_left(tree.root.left, 3)
            tree.insert_right(tree.root.left, 7)



  #pre order -in order -post order       
def preorder(node):
        """pre-order : root - kiri - kanan """
        if node is not None :
            print(node.data, end= " ")
        preorder (node.left)
        preorder (node.right)


def inorder(node):
    """in-order : kiri - root - kanan """
    if node is not None:
        inorder(node.left)
        print(node.data, end= " ")
        inorder(node.right)


def postorder(node):
    """ post - order : kiri- kanan- root """
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end= "")       
       