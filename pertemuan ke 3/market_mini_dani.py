# 1. Mengambil Input dari Pengguna
nama_barang = input("Masukkan nama barang: ")
harga_barang = int(input("Masukkan harga barang (Rp): "))
jumlah_barang = int(input("Masukkan jumlah barang: "))

# 2. Expression & Operator Aritmatika (Hitung Total)
total_harga = harga_barang * jumlah_barang

# 3. Menampilkan Total yang Harus Dibayar
print("\nTotal yang harus dibayar: Rp", total_harga)

# 4. Input Uang Pembayaran
uang_bayar = int(input("Masukkan uang pembayaran (Rp): "))

# 5. Expression & Operator Aritmatika (Hitung Kembalian)
uang_kembalian = uang_bayar - total_harga

# 6. Menampilkan Hasil Akhir
print("\n--- STRUK KASIR ---")
print("Barang      :", nama_barang)
print("Total Bayar : Rp", total_harga)
print("Uang Dibayar: Rp", uang_bayar)
print("Kembalian   : Rp", uang_kembalian)