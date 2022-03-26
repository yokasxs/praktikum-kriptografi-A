def gcd(a,b):
    while b != 0:
        t = b
        b = a%b
        a = t
    return a

angka1 = int(input("Masukkan angka 1:"))
angka2 = int(input("Masukkan Angka 2:"))

print("GCD:",gcd(angka1,angka2))
