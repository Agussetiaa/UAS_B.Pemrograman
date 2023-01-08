def input_data():
    # function untuk meminta input data dari pengguna
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM: ")
    tugas = int(input("Masukkan nilai tugas: "))
    uts = int(input("Masukkan nilai UTS: "))
    uas = int(input("Masukkan nilai UAS: "))

    # hitung nilai akhir
    akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas

    data = (nama, nim, tugas, uts, uas, akhir)
    return data