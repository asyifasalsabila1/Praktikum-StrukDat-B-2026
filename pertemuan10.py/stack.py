'''
Stack adalah struktur data linear yang
mengikuti prinsip LIFO (Last In, First Out).

Artinya: Elemen yang terakhir kali
dimasukkan, akan menjadi elemen yang
pertama kali dikeluarkan.
'''

#membungkus dalam class
class stack:
    def _init_(self):
        self.items = []
    
    def push(self, item):
        self.item.append(item)

    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        raise IndexError("pop dari stack kosong(underflow)")
    
    def peek(self):
        if not self.is_empty():
            return self.item[-1]

    def is_empty(self):
        return len (self.items) == 0     
    
                   