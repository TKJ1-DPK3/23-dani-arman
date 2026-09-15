harga = int(input("harga barang: "))
diskon = int(input("diskon barang: "))
jumlah = int(input("jumlah barang: "))

total = harga * jumlah
total = (harga * jumlah) / diskon 

print("total pembayaran:", total)