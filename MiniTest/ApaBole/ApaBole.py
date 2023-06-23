for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("ApaBole", end=" ")
    elif i % 3 == 0:
        print("Apa", end=" ")
    elif i % 5 == 0:
        print("Bole", end=" ")
    else:
        print(i, end=" ")
