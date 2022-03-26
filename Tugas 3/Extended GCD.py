a = 26513
b = 32321

if a < b:
    a, b = b, a  

a1, a2 = a, b
b1, b2 = 1, 0
c1, c2 = 0, 1

while a2 > 0:
    n, x = divmod(a1, a2)  
    a1, a2 = a2, x
    
    b1, b2 = b2, b1 - n * b2
    c1, c2 = c2, c1 - n * c2

print(f"Hasil :{b1}")