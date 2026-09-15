nama = input("masukkan nama: ")
jurusan = input("masukkan jurusan: ")
nilai = int(input("masukkan nilai: "))
if nilai >= 70:
  print("selamat", nama,"jurusan", jurusan, "kamu lulus")
else:
  print("maaf", nama,"jurusan", jurusan, "kamu belum lulus")