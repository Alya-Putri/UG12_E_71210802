mapel = ["kelas ke-1 Algorima Graf","kelas ke-3 Sistem Osperasi","kelas ke-4 PAK","kelas ke-5 Pratikum INLAN","kelas ke-2 Matematika Teknik","kelas ke-4 Bhs Indonesia", "kelas ke-6 PKN","kelas ke-1 IMK","kelas ke-3 LogMat","kelas ke-4 Praktekkom","kelas ke-2 Sistem Basis Data","kelas ke-4 Pratiku Sistem Basis Data","kelas ke-6 INLAN"]
#print(len(mapel))

hari = input("Hi Tutu, Silahkan Masukkan hari yang ingin Anda telusuri: ")

if hari == "senin":
    print('',mapel[0],'\n',mapel[1],'\n',mapel[2],'\n',mapel[3])
if hari == "selasa":
    print('',mapel[4],'\n',mapel[5],'\n',mapel[6])      
if hari == "rabu":
    print("Hari rabu Anda tidak ada kelas")
if hari == "kamis":
    print('',mapel[7],'\n',mapel[8],'\n',mapel[9])
if hari == "jumat":
    print('',mapel[10],'\n',mapel[11],'\n',mapel[12])
