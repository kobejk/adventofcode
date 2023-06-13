# open input file for reading, using text mode
try:
    file = open("day_1a_input.txt", "rt")

    # create some empty arrays
    file_list = []
    current_sublist = []

    # add each line of the file to the list
    for line in file:
        # first strip lines of any possible white space
        line = line.strip()
        # if the line is not empty, add it to the current sublist
        if line != "":
            current_sublist.append(line)
        # if the line is empty, add sublist to file_list and return empty sublist
        else:
            file_list.append(current_sublist)
            current_sublist = []

    # print first two sublists to test
    print("First file list", file_list[0])
    print("Second file list", file_list[1])
    print("Great success!!!")

    file.close()
except Exception:
    print("Error opening file")
