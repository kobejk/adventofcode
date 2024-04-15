# Handle conents possibly being unbound
contents = ""

# Open file
try:
    with open("./input_02.txt", "r") as file:
        contents = file.read()
except FileNotFoundError:
    print("File not found.")

# Define mappings for strategy guide
strategy_guide = {
    "A": "Y",  # rock (A) vs paper (Y)
    "B": "X",  # paper (B) vs rock (x)
    "C": "Z",  # scissors (C) vs scissors (Z)
}

# Define scores for choice of rock, paper or scissors
choice_score = {
    "X": 1,  # rock
    "Y": 2,  # paper
    "Z": 3,  # scissors
}

# Define scores for win, lose or draw
outcome_score = {"win": 6, "draw": 3, "lose": 0}


# Play a round
def determine_outcome(oppenent, response):
    win_conditions = {("A", "Y"), ("B", "Z"), ("C", "X")}
    draw_conditions = {("A", "X"), ("B", "Y"), ("C", "Z")}
    if (oppenent, response) in win_conditions:
        return "win"
    elif (oppenent, response) in draw_conditions:
        return "draw"
    else:
        return "lose"


total_score = 0
try:
    # Split the contens of the file into different rounds by line
    rounds = contents.strip().split("\n")
    for round in rounds:
        moves = round.split()
        opponent_move = moves[0]
        your_move = moves[1]

        outcome = determine_outcome(opponent_move, your_move)
        round_score = choice_score[your_move] + outcome_score[outcome]
        total_score += round_score
except Exception as e:
    print(f"An error occured: {e}")

print("Total score:", total_score)
