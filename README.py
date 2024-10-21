stok_barang = {
    "Kitkat": 999,
    "TimTam": 999,
    "Oreo": 999,
    "Tango": 999
}

def lihat_stok():
    for barang, stok in stok_barang.items():
        print(f"{barang}: {stok}")

def jual_barang(nama, jumlah):
    if nama in stok_barang:
        if stok_barang[nama] >= jumlah:
            stok_barang[nama] -= jumlah
            print(f"{jumlah} {nama} berhasil dijual.")
        else:
            print(f"Stok {nama} tidak mencukupi.")
    else:
        print(f"Barang {nama} tidak ditemukan.")

print("\nMenu:")
print("1. Lihat Menu")
print("2. Jual Snack")
print("3. Keluar")
pilihan = input("Pilih menu (1/2/3): ")
if pilihan == '1':
        lihat_stok()
elif pilihan == '2':
        nama = input("Masukkan nama snack yang ingin dijual: ")
        jumlah = int(input("Masukkan jumlah yang ingin dijual: "))
        jual_barang(nama, jumlah)
elif pilihan == '3':
        print("Terima kasih telah menggunakan program ini!")
else:
        print("Pilihan tidak valid, silakan coba lagi.")
