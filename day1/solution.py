# Day 1: Calorie Counting #
import io

with io.open("day1/input.txt", "r", encoding="utf-8") as input_file:
    input_string = input_file.read()
    input_list = input_string.split("\n\n")

calories_per_elf_combined_array = []

for current_elf_calories in input_list:
    current_elf_calories_array = current_elf_calories.split("\n")
    current_elf_calories_combined = 0

    for calories in current_elf_calories_array:
        if calories:  # check if the string is not empty
            current_elf_calories_combined += int(calories)

    calories_per_elf_combined_array.append(current_elf_calories_combined)

calories_per_elf_combined_array.sort(reverse=True)

# Answer for part 1 - Calories amount for elf with most calories

print(calories_per_elf_combined_array[0])

# Answer for part 2 - Top 3 Elves calories

print(calories_per_elf_combined_array[0] + calories_per_elf_combined_array[1] + calories_per_elf_combined_array[2])
