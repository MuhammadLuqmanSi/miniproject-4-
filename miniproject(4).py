from prettytable import PrettyTable
import math
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def delete_first(self):
        if self.head:
            self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def display_pretty_table(self):
        table = PrettyTable(["Nama Buku", "ID Buku", "Kategori", "Tahun", "Penulis", "Penerbit"])
        current = self.head
        while current:
            data = current.data.split(',')
            table.add_row([data[0], int(data[1]), data[2], int(data[3]), data[4], data[5]])  
            current = current.next
        return table

    def sort_by_nama_buku(self, ascending=True):
        current = self.head
        while current:
            min_node = current
            next_node = current.next
            while next_node:
                if ascending:
                    if next_node.data.split(',')[0] < min_node.data.split(',')[0]:
                        min_node = next_node
                else:
                    if next_node.data.split(',')[0] > min_node.data.split(',')[0]:
                        min_node = next_node
                next_node = next_node.next
            current.data, min_node.data = min_node.data, current.data
            current = current.next

    def sort_by_id_buku(self, ascending=True):
        current = self.head
        while current:
            min_node = current
            next_node = current.next
            while next_node:
                if ascending:
                    if int(next_node.data.split(',')[1]) < int(min_node.data.split(',')[1]):
                        min_node = next_node
                else:
                    if int(next_node.data.split(',')[1]) > int(min_node.data.split(',')[1]):
                        min_node = next_node
                next_node = next_node.next
            current.data, min_node.data = min_node.data, current.data
            current = current.next
            
    def sort_by_tahun_buku(self, ascending=True):
        current = self.head
        while current:
            min_node = current
            next_node = current.next
            while next_node:
                if ascending:
                    if int(next_node.data.split(',')[3]) < int(min_node.data.split(',')[3]):
                        min_node = next_node
                else:
                    if int(next_node.data.split(',')[3]) > int(min_node.data.split(',')[3]):
                        min_node = next_node
                next_node = next_node.next
            current.data, min_node.data = min_node.data, current.data
            current = current.next
            
    def jump_search(self, key, attribute):
        if attribute not in ['id', 'nama buku']:
            print("Pencarian tidak valid.")
            return None

        if attribute == 'id':
            current = self.head
            while current:
                data = current.data.split(',')
                if int(data[1]) == key:
                    return current.data
                elif int(data[1]) > key:
                    return None
                else:
                    current = current.next
            return None

        if attribute == 'nama buku':
            size = 0
            current = self.head
            while current:
                size += 1
                current = current.next
            
            step = int(math.sqrt(size))
            prev = None
            current = self.head
            while current:
                data = current.data.split(',')
                if data[0] == key:
                    return current.data
                elif data[0] < key:
                    prev = current
                    for _ in range(step):
                        if current:
                            current = current.next
                        else:
                            break
                else:
                    break
            while prev:
                data = prev.data.split(',')
                if data[0] == key:
                    return prev.data
                prev = prev.next


    def search_and_display(self, key, attribute):
        result = self.jump_search(key, attribute)
        if result:
            table = PrettyTable(["Nama Buku", "ID Buku", "Kategori", "Tahun", "Penulis", "Penerbit"])
            data = result.split(',')
            table.add_row([data[0], int(data[1]), data[2], int(data[3]), data[4], data[5]])  
            print("Data ditemukan:")
            print(table)
        else:
            print("Data tidak ditemukan.")


class Databuku:
    def __init__(self):
        self.data_buku = LinkedList()
        
        self.data_buku.append("Laskar Pelangi,1001,Fiction,2005,Andrea Hirata,Bentang Pustaka")
        self.data_buku.append("Ayat-ayat Cinta,1002,Romance,2004,Habiburrahman El Shirazy,Republika")
        self.data_buku.append("Bumi Manusia,1003,Historical Fiction,1980,Pramoedya Ananta Toer,Hasta Mitra")
        self.data_buku.append("Cinta di Dalam Gelas,1004,Fiction,1995,Andrea Hirata,Bentang Pustaka")
        self.data_buku.append("Pulang,1005,Fiction,2015,Tere Liye,Gramedia Pustaka Utama")
        self.data_buku.append("Sang Pemimpi,1006,Fiction,2006,Andrea Hirata,Bentang Pustaka")
        self.data_buku.append("Negeri 5 Menara,1007,Fiction,2009,Ahmad Fuadi,Gramedia Pustaka Utama")
        self.data_buku.append("Perahu Kertas,1009,Fiction,2008,Dee Lestari,Bentang Pustaka")
        self.data_buku.append("Raditya Dika Kambing Jantan,1010,Comedy,2005,Raditya Dika,GagasMedia")


    def create(self):
        print("Masukkan data buku yang diinginkan")
        nama_buku = input("Nama Buku: ")
        id_buku = int(input("ID Buku: ")) 
        kategori_buku = input("Kategori Buku: ")
        tahun_buku = int(input("Tahun Buku: ")) 
        penulis_buku = input("Penulis Buku: ")
        penerbit_buku = input("Penerbit Buku: ")
        buku_data = f"{nama_buku},{id_buku},{kategori_buku},{tahun_buku},{penulis_buku},{penerbit_buku}"

        print("\nPilih lokasi penambahan:")
        print("===========================================")
        print("|1. tambah buku di daftar awal            |")
        print("|2. tambah buku di daftar akhir           |")
        print("|3. tambah buku di antara awal atau akhir |")
        print("===========================================")
        choice = input("Masukkan pilihan: ")

        if choice == '1':
            self.data_buku.prepend(buku_data)
        elif choice == '2':
            self.data_buku.append(buku_data)
        elif choice == '3':
            id_node = int(input("Masukkan ID node setelah node baru: "))  
            current = self.data_buku.head
            while current:
                data = current.data.split(',')
                if int(data[1]) == id_node:  
                    self.data_buku.insert_after(current, buku_data)
                    break
                current = current.next
            else:
                print(f"Node dengan ID {id_node} tidak ditemukan.")
        else:
            print("Pilihan tidak valid.")

    def read(self):
        print("=================================================")
        print("|                  STOK BUKU                    |")
        print("=================================================")
        print("|1. Urutkan berdasarkan nama buku (A-Z)         |")
        print("|2. Urutkan berdasarkan nama buku (Z-A)         |")
        print("|3. Urutkan berdasarkan ID buku (kecil-besar)   |")
        print("|4. Urutkan berdasarkan ID buku (besar-kecil)   |")
        print("|5. Urutkan berdasarkan tahun buku (lama-baru)  |")
        print("|6. Urutkan berdasarkan tahun buku (baru-lama ) |")
        print("|7. Cari berdasarkan ID buku                    |")
        print("|8. Cari berdasarkan nama buku                  |")
        print("=================================================")

        choice = input("Masukkan pilihan: ")

        if choice == '1':
            self.data_buku.sort_by_nama_buku(ascending=True)
            table = self.data_buku.display_pretty_table()
            print(table)
        elif choice == '2':
            self.data_buku.sort_by_nama_buku(ascending=False)
            table = self.data_buku.display_pretty_table()
            print(table)
        elif choice == '3':
            self.data_buku.sort_by_id_buku(ascending=True)
            table = self.data_buku.display_pretty_table()
            print(table)
        elif choice == '4':
            self.data_buku.sort_by_id_buku(ascending=False)
            table = self.data_buku.display_pretty_table()
            print(table)
        elif choice == '5':
            self.data_buku.sort_by_tahun_buku(ascending=True)
            table = self.data_buku.display_pretty_table()
            print(table)
        elif choice == '6':
            self.data_buku.sort_by_tahun_buku(ascending=False)
            table = self.data_buku.display_pretty_table()
            print(table)
        elif choice == '7':
            id_cari = int(input("Masukkan ID buku yang ingin dicari: "))
            self.data_buku.search_and_display(id_cari, 'id')
        elif choice == '8':
            nama_cari = input("Masukkan nama buku yang ingin dicari: ")
            self.data_buku.search_and_display(nama_cari, 'nama buku')
        else:
            print("Pilihan tidak valid.")

    def update(self):
        print("Masukkan ID buku yang ingin diperbarui:")
        id_cari = int(input("ID Buku: "))  
        current = self.data_buku.head
        while current:
            data = current.data.split(',')
            if int(data[1]) == id_cari:  
                print(f"Data buku dengan ID {id_cari}:")
                print(f"Nama Buku: {data[0]}")
                print(f"Kategori: {data[2]}")
                print(f"Tahun: {data[3]}")
                print(f"Penulis: {data[4]}")
                print(f"Penerbit: {data[5]}")
                print("Masukkan data baru:")
                nama_buku = input("Nama Buku: ")
                kategori_buku = input("Kategori Buku: ")
                tahun_buku = int(input("Tahun Buku: "))  
                penulis_buku = input("Penulis Buku: ")
                penerbit_buku = input("Penerbit Buku: ")
                new_data = f"{nama_buku},{id_cari},{kategori_buku},{tahun_buku},{penulis_buku},{penerbit_buku}"
                current.data = new_data
                print("Data buku berhasil diperbarui!")
                return
            current = current.next
        print(f"Buku dengan ID {id_cari} tidak ditemukan.")

    def delete(self):
        print("===========================================")
        print("|1. Hapus buku di daftar awal             |")
        print("|2. Hapus buku di daftar akhir            |")
        print("|3. Hapus buku di antara awal atau akhir  |")
        print("===========================================")
        choice = input("Pilih operasi penghapusan: ")
        if choice == '1':
            self.data_buku.delete_first()
            print("Node di awal berhasil dihapus.")
        elif choice == '2':
            self.data_buku.delete_last()
            print("Node di akhir berhasil dihapus.")
        elif choice == '3':
            id_hapus = int(input("Masukkan ID buku yang ingin dihapus: "))  
            self.data_buku.delete_node(id_hapus)
            print(f"Buku dengan ID {id_hapus} berhasil dihapus.")
        else:
            print("Pilihan tidak valid.")

    def main_menu(self):
        while True:
            print("===========================================")
            print("|            PROGRAMING STORE             |")
            print("===========================================")
            print("|1. Menambahkan Buku                      |")
            print("|2. Melihat Stok Buku                     |")
            print("|3. Memperbarui Buku                      |")
            print("|4. Menghapus Buku                        |")
            print("|5. Keluar                                |")
            print("===========================================")

            choice = input("Masukkan pilihan: ")
            if choice == '1':
                self.create()
            elif choice == '2':
                self.read()
            elif choice == '3':
                self.update()
            elif choice == '4':
                self.delete()
            elif choice == '5':
                print("Terima kasih!")
                break
            else:
                print("Pilihan tidak valid.")

toko = Databuku()
toko.main_menu()
