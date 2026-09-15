# Nama File: server_status_namapanggilanmu.py

print("====================================")
print("        SERVER STATUS CHECKER        ")
print("====================================")

# Meminta input nama server dan suhu CPU dari pengguna
nama_server = input("Nama Server : ")
suhu_cpu = int(input("Suhu CPU    : "))

# Menentukan status suhu CPU menggunakan percabangan
if suhu_cpu < 40:
    status = "Suhu terlalu rendah"
elif 40 <= suhu_cpu <= 59:
    status = "Suhu normal"
elif 60 <= suhu_cpu <= 79:
    status = "Suhu cukup tinggi"
else:
    status = "WARNING! Suhu terlalu tinggi"

# Menampilkan hasil
print("====================================")
print(f"Status      : {status}")