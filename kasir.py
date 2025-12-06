import time
import os

def clear_screen():
    os.system('cls')

nama_restoran = ("Toko Makan Serba Ada")
alamat_restoran = ("Jl. Gagasan, PIK 2")
pajak = 0.1
daftar_menu = {
    1: "Nasi Goreng",
    2: "Soto Ayam",
    3: "Nasi Rames",
    4: "Soto Sapi/Kambing",
    5: "Bakso",
    6: "Nasi Ayam Goreng",
    7: "Seafood Asem Pedas Manis",
    8: "Nasi"
}

print("=== Daftar Menu ===")
print("(1) Nasi Goreng")
print("(2) Soto Ayam")
print("(3) Nasi Rames")
print("(4) Soto Sapi/Kambing")
print("(5) Bakso")
print("(6) Nasi Ayam Goreng")
print("(7) Seafood Asem Pedas Manis")
print("(8) Nasi")

nama = str(input("Masukan Nama Costumer:"))
antrian = int(input("Masukan No Antrian Costumer: "))
menu = int(input("Masukan Pilihan Menu: "))
porsi = int(input("Masukan Jumlah Porsi: "))
harga = int(input("Masukan Harga Menu: "))

banyak = porsi * harga
ppn = banyak * pajak
total = banyak + ppn

time.sleep(1.5)
clear_screen()

print("Harga Yang harus dibayar:", total)
uang = int(input("Uang yang diterima:"))
kembalian = uang - total

time.sleep(2)
clear_screen()

print("-------------------------------------------------")
print("Struk Belanja")
print("-------------------------------------------------")
print("Nama Costumer:", nama)
print("Menu Yang dipilih:", daftar_menu[menu])
print("Jumlah Porsi:", porsi)
print("Harga Menu:", harga)
print("Quantity:", banyak)
print("Pajak:", ppn)
print("Harga Yang Harus dibayar:", total)
print("Uang yang diterima: ", uang)
print("Kembalian Yang diterima: ", kembalian)
print("-------------------------------------------------")
print(nama_restoran)
print(alamat_restoran)
print("No Antrian:", antrian)
