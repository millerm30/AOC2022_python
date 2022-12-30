# Day 2: Rock Paper Scissors Part: One #
import io

with io.open("day2/input.txt", "r") as file:
    inputs = file.read().split("\n")

def part_one():
    my_points = 0
    for input in inputs:
        split_input = input.split(" ")
        if len(split_input) < 2:
            # Handle the error by skipping this input
            continue

        opponent_pick = split_input[0]
        my_pick = split_input[1]

        if opponent_pick == "A":
            if my_pick == "Z":
                print("Opponent picks rock and you pick scissors, you lost.")
                my_points = my_points + 3 + 0
            elif my_pick == "X":
                print("Opponent picks rock and you pick rock, it's a draw.")
                my_points = my_points + 1 + 3
            elif my_pick == "Y":
                print("Opponent picks rock and you pick paper, you win.")
                my_points = my_points + 2 + 6
        elif opponent_pick == "B":
            if my_pick == "Z":
                print("Opponent picks paper and you pick scissors, you win.")
                my_points = my_points + 3 + 6
            elif my_pick == "X":
                print("Opponent picks paper and you pick rock, you lose.")
                my_points = my_points + 1 + 0
            elif my_pick == "Y":
                print("Opponent picks paper and you pick paper, its a draw.")
                my_points = my_points + 2 + 3
        elif opponent_pick == "C":
            if my_pick == "Z":
                print(
                    "Opponent picks scissors and you pick scissors, its a draw."
                )
                my_points = my_points + 3 + 3
            elif my_pick == "X":
                print("Opponent picks scissors and you pick rock, you win.")
                my_points = my_points + 1 + 6
            elif my_pick == "Y":
                print("Opponent picks scissors and you pick paper, you lose.")
                my_points = my_points + 2 + 0

    print("Your total points are: " + str(my_points))


part_one()
