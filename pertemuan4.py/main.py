# main.py

from kurs import kurs    #mengambil variabel kurs (dictionary nilai tukar mata uang) dari file kurs.py.
from konverter import idr_ke_mata_uang, mata_uang_ke_idr  #Baris ini mengimpor dua fungsi dari file konverter.py, yaitu 
from tabulate import tabulate  #Mengimpor library eksternal tabulate yang digunakan untuk menampilkan data dalam bentuk tabel yang rapi.

print("=== KONVERTER MATA UANG ===")  #menampilkan judul bahwa ini program konverter mata uang 

# Menampilkan tabel kurs
print(tabulate(kurs.items(), headers=["Kode", "Kurs"], tablefmt="grid"))

# Input user
dari = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()  #upper() digunakan agar input otomatis menjadi huruf besar sehingga cocok dengan key di dictionary.
ke = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()   #Meminta memasukkan mata uang tujuan konversi.
jumlah = float(input("Jumlah: "))    #Meminta pengguna memasukkan jumlah uang yang ingin dikonversi.float() digunakan agar angka bisa berupa desimal dan dapat dihitung.

# Proses konversi
if dari == "IDR":   #ngin mengubah Rupiah ke mata uang asing, maka program menjalankan(hsdil=idr ke mata uang)
    hasil = idr_ke_mata_uang(jumlah, ke)  #Fungsi ini membagi jumlah Rupiah dengan nilai kurs mata uang tujuan.
    print(f"Rp {jumlah:,.0f} = {hasil:.2f} {ke}")  #{jumlah:,.0f} → menampilkan angka dengan pemisah ribuan tanpa desimal.{hasil:.2f} → menampilkan hasil dengan 2 angka di belakang koma.

elif ke == "IDR":  #Jika  ingin mengubah mata uang asing ke Rupiah, maka program menjalankan:
    hasil = mata_uang_ke_idr(jumlah, dari)  #fungsi ini mengalikan jumlah mata uang asing dengan nilai kurs.
    print(f"{dari} {jumlah:.2f} = Rp {hasil:,.0f}")  #dan menampilkan ini 

else:
    print("Konversi hanya mendukung IDR ke mata uang lain atau sebaliknya.")  #jika bukan keduanya akan mencoba mengonversi misalnya USD ke EUR secara langsung, maka program menampilkan pesan bahwa konversi hanya didukung antara IDR dan mata uang lain.