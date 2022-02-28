# G7
# Dinda Sherly Maharani, 202410103056 
# Khodijah Annabilah, 202410103084

import json 
import datetime 
import os

NamaFile = 'DataPendaftar.json'
NamaFile2 = 'DataPerwakilan.json'

def Pembuka():
    print('''
    Aplikasi ini digunakan untuk mempermudah pendaftaran UMROH. Data yang anda masukkan hanya bersifat  
    garis besar, setelah data telah disimpan, pihak kami akan menghubungi anda untuk membicarakan 
    pendaftaran lebih lanjut beserta persyaratan yang dibutuhkan  
    ''')
    lanjut = input("Silahkan tekan enter untuk menuju ke menu utama")
    os.system("cls")
    return lanjut

def MenuUtama():
    print('''\t =============== MENU UTAMA ===============
    \t\t Aplikasi Pendaftaran UMROH
    \t Silakhkan pilih menu yang ingin anda gunakan
    
    1. Lihat paket umroh 
    2. Daftar Umroh
    3. Lihat data pendaftaran saya
    4. Hapus data pendaftaran saya
    5. Simpan Permanen data pendaftaran
    0. Selesai
    ''')
    menu = input("Pilih menu yang ingin anda gunakan : ")
    os.system("cls")
    return menu

def PaketUmroh():
    print(''' 
    Paket A : 
        Berangkat = Februari 2021
        Harga = Rp 30.000.000,00
    Paket B :
        Berangkat = April 2021
        Harga = Rp 35.000.000,00
    Paket C :
        Berangkat = Juni 2021
        Harga = Rp 35.000.000,00
    ''') 

DaftarList = []
def DaftarUmroh():
    DataBaru = {}
    DataBaru['Tanggal'] = str(datetime.date.today())
    DataBaru['Nama'] = input("Nama Lengkap : ") 
    DataBaru['Email'] = input("Alamat Email : ") 
    NoHP = int(input("Nomor Handphone (contoh : 082229992329) : "))
    DataBaru['No Handphone']  = ("0"+str(NoHP))
    DataBaru['Paket'] = Paket = input("Pilih Paket Umroh yang anda minati : ")
    if (Paket == 'A' or Paket == 'B' or Paket == 'C') and (9<=len(str(NoHP))<=12):
        DaftarList.append(DataBaru)
        with open(NamaFile, "w") as file: 
            json.dump(DaftarList, file, indent=4) 
        print("\nData berhasil ditambahkan\n")
        DaftarLagi = input("Apakah anda ingin mendaftarkan data lagi? [ya/tidak] : ")
        while DaftarLagi != 'ya' and DaftarLagi != 'tidak':
            print("Inputkan jawaban ya/tidak!")
            DaftarLagi = input("Apakah anda ingin mendaftarkan data lagi? [ya/tidak] : ")
        if DaftarLagi == 'ya':
            DaftarUmroh()
    else:
        print("Mohon maaf, pastikan data yang anda masukkan valid. Silahkan masukkan data kembali") 
        DaftarUmroh()

def BacaData():
    with open(NamaFile, 'r') as file:
        Data = json.load(file)
        print(f"{'Tanggal':<12} {'Nama':<26} {'Email':<30} {'No HP':<18} {'Paket'}")
        for i in Data:
            print(f"{i['Tanggal']:<12} {i['Nama']:<26} {i['Email']:<30} {i['No Handphone']:<18} {i['Paket']}")                                               

def HapusData(): 
    with open(NamaFile) as file:
        DaftarList = json.load(file)
        NamaDihapus = input("Nama yang ingin dihapus : ")
        for data in range(len(DaftarList)):
            if DaftarList[data]['Nama'] == NamaDihapus:
                del DaftarList[data]
                with open(NamaFile, "w") as file: 
                    json.dump(DaftarList, file, indent=4)
                print("\nData Berhasil dihapus")
                break
        else:
            print("Nama tidak terdapat pada daftar, silahkan inputkan nama kembali")
            HapusData()

DataPerwakilan = []
def Simpan():
    Simpan = input("Apakah anda yakin ingin simpan permanen? [ya/tidak] : ")
    while Simpan != 'ya' and Simpan != 'tidak':
        print("Inputkan jawaban ya/tidak!")
        Simpan = input("Apakah anda yakin ingin simpan permanen? [ya/tidak] : ")
    if Simpan == 'ya':
        print("\nTerimakasih telah mendafatar. Berikut data yang telah anda simpan\n")
        BacaData()    
        print("\nUntuk pemberitahuan lebih lanjut, silahkan isi Nomor Handphone dan Alamat email yang dapat dihubungi.")
        Perwakilan = {}
        NoHP = int(input("Nomor Handphone yang dapat dihubungi (contoh : 082229992329) : "))
        Perwakilan['Nomor HP'] = ("0"+str(NoHP))
        Perwakilan['Email'] = input("Alamat Email yang dapat dihubungi : ") 
        print('''\nDalam kurun waktu kurang dari 24 jam, pihak kami akan menghubungi anda untuk pendaftaran lebih lanjut. Jika tak kunjung mendapat pesan, hubungi custumer service kami di nomor : 0331-2831''')
        if 9<=len(str(NoHP))<=12:
            DataPerwakilan.append(Perwakilan)
            with open(NamaFile2, "w") as file: 
                json.dump(DataPerwakilan, file, indent=4)

def Selesai():
    Selesai = input("Apakah anda yakin ingin selesai? [ya/tidak]: ")
    while Selesai != 'ya' and Selesai != 'tidak':
        print("Inputkan jawaban ya/tidak!")
        Selesai = input("Apakah anda yakin ingin selesai? [ya/tidak]: ")
    if Selesai == 'ya':
        with open(NamaFile) as file:
            DaftarList = json.load(file)
            del DaftarList
            DaftarList = []
            with open(NamaFile, "w") as file: 
                json.dump(DaftarList, file) 
        exit()

Lanjut = Pembuka()
while Lanjut != "":
    Pembuka()
    Lanjut = Pembuka()
if Lanjut == "" :
    Menu = MenuUtama()
    while True :
        if Menu == '1':
            PaketUmroh()
        elif Menu == '2':
            DaftarUmroh()
        elif Menu == '3':
            BacaData()
        elif Menu == '4':
            HapusData()
        elif Menu == '5':
            Simpan()
        elif Menu == '0':
            Selesai()
        else :
            print("Menu yang anda masukkan tidak tersedia. Silahkan pilih menu kembali")
        Kembali = input("\nSilahkan tekan enter untuk kembali ke menu utama")
        print()
        os.system("cls")
        while Kembali != "" :
            Kembali = input("\nSilahkan tekan enter untuk kembali ke menu utama")
            print()
        if Kembali == "" :
            Menu = MenuUtama()