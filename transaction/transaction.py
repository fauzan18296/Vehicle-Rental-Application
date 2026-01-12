def buat_rental(kendaraan, hari):
    return {
        "id": kendaraan["id"],
        "nama": kendaraan["nama"],
        "hari": hari,
        "total": kendaraan["harga"] * hari
    }
