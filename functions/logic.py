def cari_kendaraan(data, id_kendaraan):
    for k in data:
        if k["id"] == id_kendaraan:
            return k
    return None

def validasi_angka(x):
    return x.isdigit() and int(x) > 0

def generate_no_transaksi(no):
    return f"TRX{str(no).zfill(4)}"
