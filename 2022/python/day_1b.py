# open input file for reading, using text mode
try:
    file = open("day_1_input.txt", "rt")

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

    total_calories = 0
    most_calories = 0
    most_calories_index = 0
    elves = []

    try:
        # find the top 3 elves with the most calories
        for x in range(3):
            for index, sublist in enumerate(file_list):
                # check if current list is more calories than the largest amount so far
                if sum(sublist) > most_calories:
                    most_calories = sum(sublist)
                    most_calories_index = index

            # remove sublist with most calories from the file_list
            file_list.pop(most_calories_index)
            elves.append(most_calories_index + 1)
            total_calories += most_calories
            most_calories = 0
    except Exception:
        print("Error looping through lists...")

    print("The top 3 elves carrying the most calories are elves", elves)
    print(
        "The total amount of calories being carried by these elves is:", total_calories
    )

except Exception:
    print("Error opening file")
