def cetak_daftar_nilai(daftar):
    # function untuk mencetak daftar nilai
    print("Daftar Nilai Mahasiswa:")
    print("="*70)
    print("| No |     Nama     |    NIM    | Tugas |  UTS  | UAS  | Akhir |")
    print("="*70)
    for i in range(len(daftar)):
        print("| {no:2d} | {nama:14s} | {nim:9s} | {tugas:5d} | {uts:5d} | {uas:5d} | {akhir:6.2f} |"
              .format(no=i+1, nama=daftar[i][0], nim=daftar[i][1], tugas=daftar[i][2], uts=daftar[i][3], uas=daftar[i][4], akhir=daftar[i][5]))
    print("="*70)

def cetak_hasil_pencarian(data):
    # function untuk mencetak hasil pencarian data
    if data == "Data tidak ditemukan.":
        print(data)
    else:
        print("Data ditemukan:")
        print("="*70)
        print("|     Nama     |    NIM    | Tugas |  UTS  | UAS  | Akhir |")
        print("="*70)
        print("| {nama:14s} | {nim:9s} | {tugas:5d} | {uts:5d} | {uas:5d} | {akhir:6.2f} |"
              .format(nama=data[0], nim=data[1], tugas=data[2], uts=data[3], uas=data[4], akhir=data[5]))
        print("="*70)