class Node :
    def __init__(self,data) :
        self.data = data
        self.left = None 
        self.right = None

class BinarysearchTree:
    def __init__(self):
        self.root = None 

    def insert(self, data) :
        new = Node(data)

        #langkah 1
        if self.root == None:
            self.root = new
            return
    

    #langkah 2
        P = self.root
        Q = self.root

    #langkah 4
        while  Q != None and new.data != P.data:

    #langkah 5
            P = Q 

    #langkah 6 
            if new.data < P.data:
                Q = P.left
            else:
                Q = P.right   

    #langkah 7 
    # #jika iya
        if new.data == P.data:
            print('data duplkat!')
            return

   #jika tidak, lanjut
   # #langkah 8
        if new.data < P.data:
           #jika iya
           P.left = new
        else:
           P.right = new

bst = BinarysearchTree() 

bst.insert(12)
bst.insert(72)
bst.insert(99) 
bst.insert(67) 
bst.insert(35) 
        
        
def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end= " ")
        in_order(node.right)

in_order(bst.root)






                   
