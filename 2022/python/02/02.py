# Open file
try:
    with open("./input_02.txt", "r") as file:
        # Process each line
        for line in file:
            # strip() removes the newline character at the end of the line
            print(line.strip())
except FileNotFoundError:
    print("File not found.")

# Define mappings for strategy guide
strategy_guide = {"A": "Y", "B": "X", "C": "Z"}

# Define scores for choice of rock, paper or scissors
choice_score = {
    "X": 1,  # rock
    "Y": 2,  # paper
    "Z": 3,  # scissors
}

# Define scores for win, lose or draw
outcome_score = {"win": 6, "draw": 3, "lose": 0}
