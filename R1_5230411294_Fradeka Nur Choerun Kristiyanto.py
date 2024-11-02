class Pegawai:
    def __init__(self, no_pegawai, nama, alamat):
        self.no_pegawai = no_pegawai
        self.nama = nama
        self.alamat = alamat
        self.pegawai_list = []

    def tambah_pegawai(self):
        no_pegawai = input("Masukkan nomor pegawai: ")
        nama = input("Masukkan nama pegawai: ")
        alamat = input("Masukkan alamat pegawai: ")

        if not no_pegawai or not nama or not alamat:
            print("Data pegawai tidak lengkap.")
            return

        pegawai_baru = Pegawai(no_pegawai, nama, alamat)
        self.pegawai_list.append(pegawai_baru)
        print("Pegawai baru berhasil ditambahkan.")

    def display(self):
        print(f"Pegawai(No: {self.no_pegawai}, Nama: {self.nama}, Alamat: {self.alamat}")

class Produk:
    def __init__(self, kode_produk, nama_produk, jenis_produk):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk

    def get_info(self):
        return f"{self.jenis_produk}: {self.nama_produk} (Kode: {self.kode_produk})"


class Snack(Produk):
    def __init__(self, kode_produk, nama_snack, harga):
        super().__init__(kode_produk, nama_snack, "Snack")
        self.harga = harga

    def get_info(self):
        return f"Snack: {self.nama_produk}, Harga: {self.harga}"


class Makanan(Produk):
    def __init__(self, kode_produk, nama_makanan, harga):
        super().__init__(kode_produk, nama_makanan, "Makanan")
        self.harga = harga

    def get_info(self):
        return f"Makanan: {self.nama_produk}, Harga: {self.harga}"


class Minuman(Produk):
    def __init__(self, kode_produk, nama_minuman, harga):
        super().__init__(kode_produk, nama_minuman, "Minuman")
        self.harga = harga

    def get_info(self):
        return f"Minuman: {self.nama_produk}, Harga: {self.harga}"


class Transaksi:
    def __init__(self, no_transaksi, pegawai):
        self.no_transaksi = no_transaksi
        self.pegawai = pegawai
        self.produk_list = []

    def tambah_produk(self, produk, jumlah):
        self.produk_list.append((produk, jumlah))

    def get_total_harga(self):
        total = sum(produk.harga * jumlah for produk, jumlah in self.produk_list)
        return total

    def __str__(self):
        return f"Transaksi No: {self.no_transaksi}, Pegawai: {self.pegawai.nama}, Total Harga: {self.get_total_harga()}"

class Struk:
    def __init__(self, transaksi):
        self.transaksi = transaksi

    def cetak_struk(self):
        print(f"Struk Transaksi No: {self.transaksi.no_transaksi}")
        print(f"Nama Pegawai: {self.transaksi.pegawai.nama}")
        print("Daftar Produk:")
        for produk, jumlah in self.transaksi.produk_list:
            print(f"- {produk.get_info()} x{jumlah}")
        print(f"Total Harga: {self.transaksi.get_total_harga()}")


def main():
    pegawai1 = Pegawai("001", "Ali", "Jl. Kebon Jeruk")

    snack1 = Snack("S01", "Keripik", 10000)
    makanan1 = Makanan("M01", "Nasi Goreng", 20000)
    minuman1 = Minuman("D01", "Teh Manis", 5000)

    while True:
        print("\n============ Toko Grosir anti ngacir ============")
        print("1. Pegawai")
        print("2. Produk")
        print("3. Transaksi")
        print("0. Keluar")

        menu = int(input("Masukkan pilihan anda: "))
        
        if menu == 1:
            while True:
                print("1. Lihat Pegawai")
                print("2. Tambah pegawai")
                print("0. Keluar")
                men = int(input("Masukkan pilihan anda: "))
                
                if men == 1:
                    pegawai1.display()
                elif men == 2:
                    pegawai1.tambah_pegawai()
                elif men == 0:
                    break
                else:
                    print("Pilihan tidak ada")
        
        elif menu == 2:
            while True:
                print("1. Lihat Produk")
                print("2. Tambah Produk")
                print("0. Keluar")
                men = int(input("Masukkan pilihan anda: "))
                
                if men == 1:
                    while True:
                        print("1. Lihat Makanan")
                        print("2. Lihat Minuman")
                        print("3. Lihat Snack")
                        print("0. Keluar")
                        me = int(input("Masukkan pilihan anda: "))
                        
                        if me == 1:
                            print(makanan1.get_info())
                        elif me == 2:
                            print(minuman1.get_info())
                        elif me == 3:
                            print(snack1.get_info())
                        elif me == 0:
                            break
                        else:
                            print("Pilihan tidak ada")
                
                elif men == 2:
                    while True:
                        print("1. Tambah Makanan")
                        print("2. Tambah Minuman")
                        print("3. Tambah Snack")
                        print("0. Keluar")
                        me = int(input("Masukkan pilihan anda: "))
                        
                        if me == 1:
                            kode = input("Masukkan kode makanan : ")
                            nama = input("Masukkan nama makanan : ")
                            harga = int(input("Masukkan harga : "))
                            makanan_baru = Makanan(kode, nama, harga)
                            # Here you may want to store makanan_baru in a list
                            # For now we will just use it for demonstration
                            makanan1 = makanan_baru
                        elif me == 2:
                            kode = input("Masukkan kode minuman : ")
                            nama = input("Masukkan nama minuman : ")
                            harga = int(input("Masukkan harga : "))
                            minuman_baru = Minuman(kode, nama, harga)
                            minuman1 = minuman_baru
                        elif me == 3:
                            kode = input("Masukkan kode snack : ")
                            nama = input("Masukkan nama snack : ")
                            harga = int(input("Masukkan harga : "))
                            snack_baru = Snack(kode, nama, harga)
                            snack1 = snack_baru
                        elif me == 0:
                            break
                        else:
                            print("Pilihan tidak ada")

        elif menu == 3:
            while True:
                print("1. Tambah Transaksi")
                print("2. Lihat Transaksi")
                print("0. Keluar")
                me = int(input("Masukkan pilihan anda: "))
                
                if me == 1:
                    transaksi1 = Transaksi(input('Masukkan nomor transaksi: '), pegawai1)
                    transaksi1.tambah_produk(snack1, 2)
                    transaksi1.tambah_produk(makanan1, 1)
                    transaksi1.tambah_produk(minuman1, 3)
                    
                    struk1 = Struk(transaksi1)  # Create a receipt for the transaction
                    
                elif me == 2 and 'struk1' in locals():
                    struk1.cetak_struk()
                elif me == 0:
                    break
                else:
                    if 'struk1' not in locals():
                        print('Belum ada transaksi yang ditambahkan.')
                    else:
                        print('Pilihan tidak ada')
        
        elif menu == 0:
            break
        else:
            print("Pilihan tidak ada")

if __name__ == "__main__":
    main()