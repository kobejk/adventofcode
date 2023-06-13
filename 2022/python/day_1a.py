# open input file for reading, using text mode
try:
    file = open("day_1a_input.txt", "rt")

    # first create an empty list
    file_list = []

    # add each line of the file to the list
    for x in file:
        file_list.append(x)

    print(file_list[0])

    file.close()
except Exception:
    print("Error opening file")
