for angka in range(1, 101):
    if angka % 3 == 0 and angka % 5 == 0:
        print("ApaBole", end=", ")
    elif angka % 3 == 0:
        print("Apa", end=", ")
    elif angka % 5 == 0:
        print("Bole", end=", ")
    else:
        print(angka, end=", ")
