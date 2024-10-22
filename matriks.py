baris_a = int(input("Masukkan baris a: "))
kolom_a = int(input("Masukkan kolom a: "))

baris_b = int(input("Masukkan baris b: "))
kolom_b = int(input("Masukkan kolom b: "))

if (kolom_a != baris_b):
    print("Matriks a dan b tidak dapat dikallikan!")
else:
    print("Matriks a dan b dapat di kalikan")
    a = []
    for i in range(baris_a):
        baris = []
        for j in range(kolom_a):
            value = int(input("Masukkan elemen matriks a: "))
            baris.append(value)
        a.append(baris)

    b = []
    for i in range(baris_b):
        baris = []
        for j in range(kolom_b):
            value = int(input("Masukkan elemen matriks b: "))
            baris.append(value)
        b.append(baris)
    print("Matriks a: ", a)
    print("Matriks b: ", b)
