# Handle conents possibly being unbound
contents = ""

# Open file
try:
    with open("./input_02.txt", "r") as file:
        contents = file.read()
except FileNotFoundError:
    print("File not found.")

# Define strategy of winning/losing/drawing round
desired_outcome = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}

# Define scores for win, lose or draw
outcome_score = {"win": 6, "draw": 3, "lose": 0}

response_map = {
    "A": {"win": "Y", "lose": "Z", "draw": "A"},  # Opponent plays Rock (A)
    "B": {"win": "Z", "lose": "X", "draw": "B"},  # Opponent plays Paper (B)
    "C": {"win": "X", "lose": "Y", "draw": "C"},  # Opponent plays Scissors (C)
}


# Determine what move to make for the desired outcome
def which_move(opponent, outcome):
    return response_map[opponent][desired_outcome[outcome]]
