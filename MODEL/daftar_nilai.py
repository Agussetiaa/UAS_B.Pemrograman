def tambah_data(daftar, data):
    # function untuk menambahkan data ke daftar
    daftar.append(data)
    return daftar

def ubah_data(daftar, data_baru, data_lama):
    # function untuk mengubah data yang ada di daftar
    for i in range(len(daftar)):
        if daftar[i][0] == data_lama[0]:
            daftar[i] = data_baru
            break
    return daftar

def hapus_data(daftar, data):
    # function untuk menghapus data dari daftar
    daftar.remove(data)
    return daftar

def cari_data(daftar, data):
    # function untuk mencari data di daftar
    for i in range(len(daftar)):
        if daftar[i][0] == data[0]:
            return daftar[i]
    return "Data tidak ditemukan."