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
            current_sublist.append(int(line))
        # if the line is empty, add sublist to file_list and return empty sublist
        else:
            file_list.append(current_sublist)
            current_sublist = []

    most_calories = 0
    current_calories = 0

    # loop through each array and count calories
    for sublist in file_list:
        for calorie_count in sublist:
            current_calories += calorie_count

        # check if current list is more calories than the largest amount so far
        if current_calories > most_calories:
            most_calories = current_calories

        current_calories = 0

    print("The most calories being carried by an elf is:", most_calories)

    file.close()
except Exception:
    print("Error opening file")
