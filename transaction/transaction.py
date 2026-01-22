def buat_rental(kendaraan, hari, penyewa = "Pelanggan"):
    TOTAL = kendaraan["harga"] * hari
    return {
        "id": kendaraan["id"],
        "penyewa": penyewa,
        "nama": kendaraan["nama"],
        "hari": hari,
        "total": TOTAL
    }
