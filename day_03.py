# Day 3 Gamma Epsilon Rates

def gamma_epsilon(diagnostics):
    """Returns the Gamma and Epsilon Rate.
    diagnostics (list) of binomial integers
    """
    zeroes = [0,0,0,0,0]
    ones = [0,0,0,0,0]
    gamma = ''
    epsilon = ''

    # Tallies up the number of zeroes and ones and stores it to the respective lists indices
    for line in diagnostics:
        for digit in range(0, len(line)):
            if int(line[digit]) == 0:
                zeroes[digit] += 1
            else:
                ones[digit] += 1
    print(f"Zeroes: {zeroes}")
    print(f"Ones: {ones}")
    # Compares the list of zeroes to list of ones, and determines which one is greater.
    # Gamma Rate = most common bit in the corresponding position of all numbers
    # Epsilon Rate = least common bit in the corresponding position of all numbers
    for i in range(len(zeroes)):
        if zeroes[i] > ones[i]:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    print(f"Gamma rate is: {gamma}")
    print(f"Epsilon rate is: {epsilon}")

def main():
    with open("diagnostics.txt") as file:
        lines = file.read().split('\n')
    gamma_epsilon(lines)

if __name__ == "__main__":
    main()
