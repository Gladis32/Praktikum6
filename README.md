# Praktikum Dictionary
>Tugas praktikum 6 Bahasa Pemrograman | Universitas Pelita Bangsa
## PROFIL
| Variable | Isi |
| -------- | --- |
| **Nama** | Gladis Toti Anggraini |
| **NIM** | 312310566 |
| **Kelas** | TI.23.A.5 |
| **Mata Kuliah** | Bahasa Pemrograman |

## Tugas Latihan 
* Buat Dictionary daftar kontak. Nama sebagai key, dan nomor sebagai value 
* Tampilkan kontaknya Arii
* Tambah kontak baru dengan nama Riko, nomor 087654544
* ubah kontak Dina dengan nomor baru 088999776
* Tampilkan semua Nama 
* Tampilkan semua Nomor 
* Tampilkan daftar Nama dan Nomornya 
* Hapus kontak Dina 

![Alt text](image-5.png)
```
list = {
    "Arii" : "081267888", "Dina" : "087677776"
}
```
**'list'** nama variabel yang digunakan untuk menyimpan daftar kontak dalam bentuk dictionary. Dictionary ini memiliki pasangan key-value yang merepresentasikan nama kontak dan nomor teleponnya.

``````
for x in list.keys():
``````

**'for x in list.keys():'** fungsi dari *'loop for'* yang digunakan untuk mengiterasi melalui semua kunci (keys) dalam kamus list. Variabel x akan mewakili kunci (nama dalam konteks ini) pada setiap iterasi.

``````
for x in list.values():
``````
**'for x in list.values():'** fungsi *'loop for'* yang digunakan untuk mengiterasi melalui semua nilai (values) dalam kamus list. Variabel x akan mewakili nilai nomor telepon pada setiap iterasi.

``````
for x, y in list.items():
``````
**'for x, y in list.items():'** fungsi dari *'loop for'* yang digunakan untuk mengiterasi melalui setiap item dalam kamus. x akan menjadi kunci (nama), dan y akan menjadi nilai (nomor telepon).

![Alt text](image-1.png)


## Tugas Praktikum
Buat program sederhana yang akan menampilkan daftar nilai
mahasiswa, dengan ketentuan :

- Program dibuat dengan menggunakan Dictionary
- Tampilkan menu pilihan: (Tambah Data, Ubah Data, Hapus Data, Tampilkan Data, Cari Data)
- Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, uas: 35%)
- Buat flowchart dan penjelasan programnya pada README.md. • Commit dan push repository ke github.



### Membuat dictionary dan Menambahkan data input
![Alt text](image-4.png)
```Python
list = {}

while True:
    c = input("\n(T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar: ")

    # Menambahkan data inputan 
    if c.lower() == 't':
        print("Tambah data :\n")
        nama    = input("Nama           : ")
        nim     = int(input("NIM            : "))
        uts     = int(input("Nilai UTS      : "))
        uas     = int(input("Nilai UAS      : "))
        tugas   = int(input("Nilai Tugas    : "))
        akhir = (tugas * 30/100) + (uts * 35/100) + (uas * 35/100)
        list[nama] = [nim, tugas, uts, uas, akhir]
```
`if c.lower` Berfungsi seperti `or` input bisa berjalan jika memasukan T/t<br>

### Mengubah data inputan
``` Python
    # Mengubah data inputan
    elif c.lower() == 'u':
        print("Ubah Data :")
        nama = input("\nMasukkan Nama  : ")
        if nama in list.keys():
            nim     = int(input("NIM            : "))
            uts     = int(input("Nilai UTS      : "))
            uas     = int(input("Nilai UAS      : "))
            tugas   = int(input("Nilai Tugas    : "))
            akhir = (tugas * 30/100) + (uts * 35/100) + (uas * 35/100)
            list[nama] = [nim, tugas, uts, uas, akhir]
        else:
            print("NAMA {0} TIDAK ADA!".format(nama))
```
>`print("NAMA {0} TIDAK ADA!".format(nama))` memanggil variable nama <br>
Apabila kita menginput 'u' maka akan ada keterangan untuk mengubah data dan kita akan diminta untuk menginputkan nama yang mau diubah datanya, apabila nama tidak ada maka outputnya "Nama {} tidak ditemukan". Dimana {} adalah nama/data yang mau kita ubah.
### Menghapus Data yg sudah di input
``` Python
    # Menghapus inputan Nama
    elif c.lower() == 'h':
        print("Hapus berdasarkan nama inputan :")
        nama = input("\nMasukkan Nama  : ")
        if nama in list.keys():
            del list[nama]
            print("\nData {0} berhasil di hapus".format(nama))
        else:
            print("NAMA {0} TIDAK ADA!".format(nama))
```
>Apabila kita menginput 'h' maka kita akan diminta menginput nama yang akan dihapus. Jika nama ada di dalam dictionary, maka system akan menghapus keys/nama tersebut beserta valuesnya pada statement del x[nama].
### Mencari data yang telah di input
``` Python
    # Mencari data yg sudah di input
    elif c.lower() == 'c':
        print("Cari data berdasarkan nama inputan :")
        nama = input("\nMasukkan Nama : ")
        if nama in list.keys():
            print("\nNama        : {0}".format(nama))
            print("NIM         : {0}".format(nim))
            print("Nilai UTS   : {0}".format(uts))
            print("Nilai UAS   : {0}".format(uas))
            print("Nilai Tugas : {0}".format(tugas))                  
            print("Nilai Akhir : {0}".format(akhir)) 
        else:
            print("NAMA {0} TIDAK ADA!".format(nama))
```
>Apabila kita menginputkan 'c' maka kita akan diminta untuk memasukkan nama yang akan dicari. Apabila nama yang dicari ada di dalam dictionary maka outputnya akan menampilkan data dari nama tersebut.
### Menampilkan seluruh data 
``` Python
    # Menampilkan seluruh data 
    elif c.lower() == 'l':
        if list.items():
            print("-"*78)
            print("|                               Daftar Mahasiswa                             |")
            print("-"*78)
            print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*78)
            i = 0
            for z in list.items():
                i += 1
                print("| {no:2d} | {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                      .format(z[0][:13], z[1][0], z[1][1], z[1][2], z[1][3], z[1][4], no=i))
            print("-"*78)
        else:
            print("-"*78)
            print("|                               Daftar Mahasiswa                             |")
            print("-"*78)
            print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("-"*78)
            print("|                       TIDAK ADA DATA! Silakan tambah data                  |")
            print("-"*78)
```

``` Python 
for z in list.items():
                i += 1
                print("| {no:2d} | {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                      .format(z[0][:13], z[1][0], z[1][1], z[1][2], z[1][3], z[1][4], no=i))
```
>`list.items():` memanggil isi dari variable list, `.format`  Digunakan untuk mengatur format string yang nantinya akan dicetak atau ditampilkan ke layar.<br>
>Apabila kita menginput 'l/L' maka sistem akan menampilkan data - data yang sudah kita masukkan. Jika kita belum memasukkan data maka outputnya menjadi "TIDAK ADA DATA".
<img src="praktikum 5/ss 1.png">


### Keluar program
```Python
    # Keluar program
    elif c. lower() == 'k':
        break

    else:
        print("\n INPUT {} TIDAK ADA!, Silakan pilih [T/U/H/C/L] untuk menjalankan program!".format(c))
```
><b>Program untuk menghentikan perulangan</b><br>Jika menginput"k/K" program akan berhenti melakukan perulangan dan otomatis keluar dari program
![Alt text](image-2.png)



>Hasil hanya sebagian dari fungsi program

### Flowchart
![Alt text](image-6.png)

*********************************************************

### Catatan

- Program berjalan dalam loop tak terbatas (`while True`) sehingga pengguna dapat terus melakukan operasi hingga memilih untuk keluar.
- Program menggunakan kamus (`list`) untuk menyimpan data mahasiswa, dengan nama sebagai kunci dan nilai-nilai terkait sebagai nilai.

### Cara Penggunaan

1. Pilih opsi sesuai dengan tindakan yang ingin dilakukan: (T)Tambah, (U)Ubah, (H)Hapus, (C)Cari, (L)Lihat, atau (K)Keluar.
2. Ikuti petunjuk yang muncul untuk setiap opsi, dan program akan merespons sesuai.
3. Program akan terus berjalan hingga pengguna memilih untuk keluar.

### Perhatian

- Pastikan untuk memasukkan input sesuai dengan petunjuk untuk hasil yang diinginkan.
- Program memberikan pesan informasi jika terjadi kesalahan input atau jika data yang dicari/tindakan yang diinginkan tidak ditemukan.