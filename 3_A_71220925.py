a = int(input("Masukkan Pembatas:"))
b = int(input("Masukkan Angka yang dlarang:"))

for i in range (a):
     if i==b :
         continue
     print(i, end=' ')
