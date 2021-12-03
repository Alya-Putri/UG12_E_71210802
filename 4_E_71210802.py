x=([ 3,20,100,-35,50 ])
print(x)

hasil=x[0]
for i in range(1,len(x)):
    y=x[i]
    if y > hasil:
        hasil = y
print("Nilai Terbesar: ",hasil)

for i in range(1,len(x)):
    y=x[i]
    if y < hasil:
        hasil = y
print("Nilai Terkecil: ",hasil)
