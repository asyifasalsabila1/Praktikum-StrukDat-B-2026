# Node
class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama   #simpan nama pasien 
        self.keluhan = keluhan  #simpan keluhan pasien 
        self.next = None


# Queue
class Queue:
    def __init__(self):
        self.head = None   #pasien paling depan yng akan di panggil
        self.tail = None   #pasien belakang yang baru daftar
        self._size = 0
        self.no_antrian = 0  #jumlah pasien awal 

    def enqueue(self, nama, keluhan):  #masukkan nama,keluhan pasien
        baru = Node(nama, keluhan)

        if self.head is None:   # 
            self.head = self.tail = baru
        else:
            self.tail.next = baru  #memasukkan pasien terakhir ke pasien baru , menggeser posisi tail ke belakang 
            self.tail = baru

        self._size += 1  #jumlah pasien bertambah 
        self.no_antrian += 1

        print(f"[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self.no_antrian})")

    def dequeue(self):
        if self.head is None:  # kalau kosong tidak bisa manggil siapa-siapa
            return

        ambil = self.head
        self.head = self.head.next   #menggeser ke pasien berikutnya

        if self.head is None:  #kalau habis belakang juga koong 
            self.tail = None

        self._size -= 1 #jumlah pasien berkurang
        print(f"[PANGGIL] Dokter memanggil: {ambil.nama.upper()} (keluhan: {ambil.keluhan})")

    def peek(self):
        if self.head is None:   #kalau kosong tidak ada bisa liat
            return
        print(f"[PEEK] Pasien berikutnya: {self.head.nama.upper()} — {self.head.keluhan}")  #menampilkan pasien depan tapi tidak di hapus

    def is_empty(self):   #kalau head kosong antrian juga kosong 
        return self.head is None

    def size(self): #mengambil jumlah dari variabel 
        return self._size

    def clear(self):  #menghapus semua natrian sekaligus
        self.head = None
        self.tail = None
        self._size = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

    def display(self):
        current = self.head  #mulai dari depan 
        no = 1
        print("[ANTRIAN SAAT INI]")
        while current:   #selama masi ada pasien 
            print(f"{no}. {current.nama.upper()} = {current.keluhan}")  #menampilkan lalu pindah kepasien berikutnya
            current = current.next
            no += 1


# ==========================
# SIMULASI SESUAI OUTPUT
# ==========================
print("====================================")
print("SISTEM ANTRIAN POLI UMUM")
print("RS Sehat Bersama")
print("====================================\n")

q = Queue()

print("[CEK] Apakah antrian kosong? = YA, antrian masih kosong.")

q.enqueue("Budi", "demam tinggi")
q.enqueue("Ani", "batuk pilek")
q.enqueue("Citra", "sakit kepala")


print(f"\n[INFO] Jumlah pasien menunggu: {q.size()} orang")

q.peek() #lihat siapa berikutnya

q.enqueue("Dodi", "nyeri perut")  #dodi masuk antrian

q.display()
print()


print(f"[INFO] Jumlah pasien masih menunggu: {q.size()} orang")
print("[CEK] Apakah antrian kosong? = YA, antrian sudah kosong.")

print("\n====================================")
print("Simulasi Selesai!")
print("====================================")