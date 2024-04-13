# open input file for reading, using text mode
try:
    file = open("input_01.txt", "rt")

    # create some empty arrays
    file_list = []
    current_sublist = []

    # add each line of the file to the list
    for line in file:
        # first strip lines of any possible white space
        line = line.strip()
        # if the line is not empty, add it to the current sublist
        if line != "":
            current_sublist.append(int(line))
        # if the line is empty, add sublist to file_list and return empty sublist
        else:
            file_list.append(current_sublist)
            current_sublist = []

    file.close()

    most_calories = 0
    elf = 0

    # loop through each array and count calories
    for sublist in file_list:
        # check if current list is more calories than the largest amount so far
        if sum(sublist) > most_calories:
            most_calories = sum(sublist)
            elf = file_list.index(sublist)

    # as .index() returns the index where the first element is 0, make it
    # easier to read by giving the actual elf, not the index of the elf
    elf += 1

    print("The elf carrying the most calories is elf:", elf)
    print("The most calories being carried by elf", elf, "is:", most_calories)

except Exception:
    print("Error opening file")
