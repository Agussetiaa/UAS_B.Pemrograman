import MODEL.daftar_nilai as dn
import VIEW.input_nilai as inp
import VIEW.view_nilai as vi

def main():
    # inisialisasi daftar nilai
    daftar_nilai = []

    # menu pilihan
    while True:
        print("Menu:")
        print("1. Tambah data")
        print("2. Ubah data")
        print("3. Hapus data")
        print("4. Cari data")
        print("5. Lihat daftar nilai")
        print("6. Keluar")
        pilihan = input("Masukkan pilihan Anda (1-6): ")

        if pilihan == "1":
            # tambah data
            data = inp.input_data()
            daftar_nilai = dn.tambah_data(daftar_nilai, data)
        elif pilihan == "2":
            # ubah data
            if data[0] in data.keys():
                data_lama = inp.input_data()
                data_baru = inp.input_data()
            daftar_nilai = dn.ubah_data(daftar_nilai, data_baru, data_lama)
        elif pilihan == "3":
            # hapus data
            data = inp.input_data()
            daftar_nilai = dn.hapus_data(daftar_nilai, data)
        elif pilihan == "4":
            # cari data
            data = inp.input_data()
            hasil_pencarian = dn.cari_data(daftar_nilai, data)
            vi.cetak_hasil_pencarian(hasil_pencarian)
        elif pilihan == "5":
            # lihat daftar nilai
            vi.cetak_daftar_nilai(daftar_nilai)
        elif pilihan == "6":
            # keluar
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()