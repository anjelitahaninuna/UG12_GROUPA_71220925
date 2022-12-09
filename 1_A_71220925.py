a = int(input("Masukkan awal deret :"))
b = int(input("Masukkan akhir deret :"))

for i in range(a,b):
    if i%2==1   and i%3!=0 and i%6!=0:
        print (i,end=" ")
