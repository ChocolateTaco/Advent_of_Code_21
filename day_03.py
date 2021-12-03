"""
--- Day 3: Binary Diagnostic ---
The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.
The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.
You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.
Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.
The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.
The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.
So, the gamma rate is the binary number 10110, or 22 in decimal.
The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.
Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)
"""
def binarytodecimal(bin_number):
    return int(bin_number, 2)

def gamma_epsilon(diagnostics):
    """Returns the Power, which is defined by the product of the Gamma and Epsilon Rates.
    diagnostics (list) of binomial integers
    """
    
    def zerolistmaker(n):
        """Creates a list of n zeroes."""
        listofzeros = [0] * n
        return listofzeros

    zeroes = zerolistmaker(len(diagnostics[0]))
    ones = list(zeroes)
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
    print(f"Gamma rate is: {binarytodecimal(gamma)}")
    print(f"Epsilon rate is: {binarytodecimal(epsilon)}")
    # Power Consumption is considered gamma x epsilon rate
    power = binarytodecimal(gamma) * binarytodecimal(epsilon)
    print(f"Power rate is: {power}")
    return power

def main():
    with open("diagnostics.txt") as file:
        lines = file.read().split('\n')
    gamma_epsilon(lines)

if __name__ == "__main__":
    main()
