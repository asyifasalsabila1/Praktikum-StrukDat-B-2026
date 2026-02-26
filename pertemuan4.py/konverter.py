# konverter.py

from kurs import kurs  #untuk mengambil dictionary kurs dari file kurs.py.

def idr_ke_mata_uang(jumlah, kode):   #untuk mengubah mata uang IDR ke mata uang asing
    if kode in kurs:   #mengecek apakah kode mata uang yang dimasukkan user tersedia di dalam dictionary kurs.
        return jumlah / kurs[kode]
    return None  #Jika kode tidak ditemukan fungsi mengembalikan nilai kosong sebagai tanda bahwa kode tidak valid.
 
def mata_uang_ke_idr(jumlah, kode):  #digunakan untuk mengubah mata uang asing ke Rupiah (IDR).
    if kode in kurs:   #Mengecek apakah kode mata uang tersedia.
        return jumlah * kurs[kode]
    return None  #jika kode tidak valid 