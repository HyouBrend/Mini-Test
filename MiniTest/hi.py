for i in range(1, 151):
    output = ""

    if i % 3 == 0:
        output += "Nonton"

    if i % 5 == 0:
        output += "Anime"

    if i % 7 == 0:
        output += "Suka"

    if output == "":
        output = str(i)

    print(output)