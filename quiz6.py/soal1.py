def tambah_buku(nama, harga, stok):
    if harga <= 0:
        print("Error: Harga harus lebih besar dari 0.")
    return None
 
    if stok < 0:
        print("Error: Stok tidak boleh negatif.")
    return None
    
    return {
        "nama": nama,
        "harga": harga,
        "stok": stok
    }


#daftar_buku = []
daftar_buku =[]
for i in range(3):
    print(f"\ n input buku ke-{i+1}")
    nama  = input ("nama buku")
    harga = float (input("harga bukU :"))
    stok = int (input("stok :"))
    print("input harga\stok tidak valid!")


    buku = tambah_buku(nama,harga,stok)
    if buku is not None:
      daftar_buku.append(buku)
    
