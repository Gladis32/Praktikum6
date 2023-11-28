list = {
    "Arii" : "081267888", "Dina" : "087677776"  
}
print("\nTampilkan kontak Arii dan Dina :", )
print(29*"=")
print(" {0:^2} |".format("Nama"), "Nomor Telepon")      
print("=============================")
print(" {0:^2} |".format("Arii") ,list["Arii"],"\n")
print(" {0:^2} |".format("Dina") ,list["Dina"],"\n")

# Tampilkan kontak Ari
list = {
    "Arii" : "081267888", "Dina" : "087677776"  
}
print("\nTampilkan kontak Arii :")
print(29*"=")
print(" {0:^2} |".format("Nama"), "Nomor Telepon")      
print("=============================")
print(" {0:^2} |".format("Arii") ,list["Arii"],"\n")

# Tambah Kontak baru dengan nama Riko
list["Riko"] = "087654544"
# Ubah kontak dina dengan nomor baru 088999776
list["Dina"] = "088999776"

# Tampilkan semua Nama 
print("Tampilan semua Nama :")
print("=============================")
# Setelah di ubah
print(" {0:^2} |".format("Nama"), "Nomor Telepon")
print("=============================")
for x in list.keys():
    print(" {0:^2} |".format(x))
print("\n")

# Tampilkan Semua Nomor 
print("Tampilan semua Nomor :")
print("=============================")
# Setelah di ubah
print(" {0:^2} |".format("Nama"), "Nomor Telepon")
print("=============================")
for x in list.values():
    print(" {0:^2} |".format(x))
print("\n")

# Tampilkan daftar Nama & Nomor
print("Tampilan daftar Nama & Nomor :")
print("=============================")
# Setelah di ubah
print(" {0:^2} |".format("Nama"), "Nomor Telepon")
print("=============================")
for x, y in list.items():
    print(" {0:^2} |".format(x), (y))
print("\n")

# Menghapus Kontak Dina
print("Menghapus Kontak Dina :")
print(29*"=")
del list["Dina"]
print(" {0:^2} |".format("Nama"), "Nomor Telepon")
print("=============================")
for x, y in list.items():
    print(" {0:^2} |".format(x), (y))
print("\n")