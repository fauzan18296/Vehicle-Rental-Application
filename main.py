import os
from data import KENDARAAN as vehicle
from ui import tampilkan_header, tampilkan_kendaraan, tampilkan_menu, tampilkan_rental, cetak_struk
from functions import cari_kendaraan, validasi_angka, generate_no_transaksi
from transaction import buat_rental

os.system("cls" if os.name == "nt" else "clear")

rental_aktif = []
riwayat = []
no_transaksi = 1

tampilkan_header()

running = True
while running:
    tampilkan_menu()
    pilih = input("Pilih menu (1-6): ")

    if pilih == "1":
        tampilkan_kendaraan(vehicle)
    elif pilih == "2":
        tampilkan_kendaraan(vehicle)
        id_kendaraan = input("ID kendaraan: ")

        if not validasi_angka(id_kendaraan):
            print("❌ ID tidak valid\n") if validasi_angka(id_kendaraan) != 0 else print("❌ Pembatalan rental\n")
            continue

        k = cari_kendaraan(vehicle, int(id_kendaraan))
        if not k or k["stok"] <= 0:
            print("❌ Kendaraan tidak tersedia\n")
            continue

        hari = input("Lama sewa (hari): ")
        if not validasi_angka(hari):
            print("❌ Lama sewa tidak valid\n") if validasi_angka(hari) != 0 else print("❌ Pembatalan rental\n")
            continue

        rental = buat_rental(k, int(hari))
        rental_aktif.append(rental)
        k["stok"] -= 1

        cetak_struk(generate_no_transaksi(no_transaksi), rental)
        no_transaksi += 1

    elif pilih == "3":
        tampilkan_rental(rental_aktif)

    elif pilih == "4":
        if not rental_aktif:
            print("❌ Tidak ada rental aktif\n")
            continue

        r = rental_aktif.pop(0)
        riwayat.append(r)
        print(f"✅ {r['nama']} berhasil dikembalikan\n")

    elif pilih == "5":
        tampilkan_rental(riwayat)

    elif pilih == "6":
        print("\n👋 Terima kasih telah menggunakan jasa rental!\n")
        running = False

    else:
        print("❌ Pilihan tidak valid\n")
