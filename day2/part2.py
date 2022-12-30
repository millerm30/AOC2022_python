# Day 2: Rock Paper Scissors: Part Two #
import io

with io.open("day2/input.txt", "r") as file:
    inputs = file.read().split("\n")

def part_two():
    my_points = 0
    for input_str in inputs:
        split_input = input_str.split(" ")
        if len(split_input) < 2:
            # Handle the error by skipping this input
            continue

        opponent_pick = split_input[0]
        my_plan = split_input[1]

        if opponent_pick == "A":
            if my_plan == "X":
                print(
                    "Opponent picks rock and plan is to lose, you pick scissors."
                )
                my_points = my_points + 3 + 0
            elif my_plan == "Y":
                print(
                    "Opponent picks rock and plan is to draw, you pick rock.")
                my_points = my_points + 1 + 3
            elif my_plan == "Z":
                print(
                    "Opponent picks rock and plan is to win, you pick paper.")
                my_points = my_points + 2 + 6
        elif opponent_pick == "B":
            if my_plan == "X":
                print(
                    "Opponent picks paper and plan is to lose, you pick rock.")
                my_points = my_points + 1 + 0
            elif my_plan == "Y":
                print(
                    "Opponent picks paper and plan is to draw, you pick paper."
                )
                my_points = my_points + 2 + 3
            elif my_plan == "Z":
                print(
                    "Opponent picks paper and plan is to win, you pick scissors."
                )
                my_points = my_points + 3 + 6
        elif opponent_pick == "C":
            if my_plan == "X":
                print(
                    "Opponent picks scissors and plan is to lose, you pick paper."
                )
                my_points = my_points + 2 + 0
            elif my_plan == "Y":
                print(
                    "Opponent picks scissors and plan is to draw, you pick scissors."
                )
                my_points = my_points + 3 + 3
            elif my_plan == "Z":
                print(
                    "Opponent picks scissors and plan is to win, you pick rock."
                )
                my_points = my_points + 1 + 6

    print(f"My points: {my_points}")

part_two()