import os
from data import MOBIL, MOTOR
from ui import tampilkan_header, tampilkan_kendaraan, tampilkan_menu, tampilkan_rental, cetak_struk, tampilkan_sub_menu, tampilan_pengembalian
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
        tampilkan_sub_menu()
        p = input("Pilih jenis: ")
        if p == "1":
            tampilkan_kendaraan(MOBIL)
        elif p == "2":
            tampilkan_kendaraan(MOTOR)
        elif p == "3":
            tampilkan_kendaraan(MOBIL + MOTOR)

    elif pilih == "2":
        tampilkan_sub_menu()
        p = input("Pilih jenis: ")
        if p == "1":
            tampilkan_kendaraan(MOBIL)
        elif p == "2":
            tampilkan_kendaraan(MOTOR)
        elif p == "3":
            tampilkan_kendaraan(MOBIL + MOTOR)
        else:
            continue

        id_k = input("ID kendaraan: ")
        if not validasi_angka(id_k):
            print("❌ ID tidak valid\n")
            continue

        kendaraan = cari_kendaraan(MOBIL + MOTOR, int(id_k))
        if not kendaraan or kendaraan["stok"] <= 0:
            print("❌ Kendaraan tidak tersedia\n")
            continue

        nama_penyewa = input("Nama penyewa: ")
        if not nama_penyewa.strip():
            print("❌ Nama tidak boleh kosong\n")
            continue

        hari = input("Lama sewa (hari): ")
        if not validasi_angka(hari):
            print("❌ Lama sewa tidak valid\n")
            continue

        rental = buat_rental(kendaraan, int(hari), nama_penyewa)
        rental_aktif.append(rental)
        kendaraan["stok"] -= 1

        cetak_struk(generate_no_transaksi(no_transaksi), rental)
        no_transaksi += 1

    elif pilih == "3":
        tampilkan_rental(rental_aktif)

    elif pilih == "4":
        print("❌ Tidak ada kendaraan yang sedang aktif") if len(rental_aktif) == 0 else tampilan_pengembalian(rental_aktif)
        if len(rental_aktif) != 0:
            id_k = input("Nomer antrian yang dikembalikan ( ketik 0 untuk membatalkan ): ")
        elif not validasi_angka(id_k):
            print("❌ Nomer antrian tidak valid\n") if validasi_angka(id_k) != 0 else print("❌ Pengembalian dibatalkan\n")
            continue
        else:
            continue
        r = rental_aktif.pop()
        riwayat.append(r)
        print(f"✅ {r['nama']} milik {r['penyewa']} berhasil dikembalikan\n")

    elif pilih == "5":
        tampilkan_rental(riwayat)

    elif pilih == "6":
        print("👋 Terima kasih!")
        running = False

    else:
        print("❌ Pilihan tidak valid\n")