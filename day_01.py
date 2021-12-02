# Advent of Code 2021
# --- Day 1: Sonar Sweep ---

# For Part 1

sonars = []
with open('Advent/day_01_input.txt') as sonar_file:
    sonars = sonar_file.readlines()

def sonar_increaser(waves):
    depth_increase_counter = 0
    for index in range(0, len(waves)):
        if int(waves[index - 1]) < int(waves[index]):
            depth_increase_counter += 1
            # print(f"{waves[index - 1]} < {waves[index]}", end="")
    print(f"Final answer is: {depth_increase_counter}")

sonar_increaser(sonars)


# For Part 2
def triple_measurements(waves):
    triple_waves = []
    # depth_increase_counter = 1
    # index = 1
    counter = -1
    for index in range(0, len(waves) - 2):
        # letter = waves[index] + waves[index + 1] + waves[index + 2]
        letter = int(waves[index]) + int(waves[index + 1]) + int(waves[index + 2])
        triple_waves.append(letter)
        counter += 1
    print(f"Triple wave counter: {counter}")
    return triple_waves

reading = triple_measurements(sonars)
sonar_increaser(reading)
        

