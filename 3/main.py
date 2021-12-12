from copy import deepcopy

def most_common(input, position):
    freq = [x[position] for x in input]
    freq = ''.join(freq)
    freq_0 = freq.count("0")
    freq_1 = freq.count("1")
    if freq_0 > freq_1:
        return "0"
    elif freq_0 < freq_1:
        return "1"
    return "1"

def least_common(input, position):
    bit = most_common(input, position)
    if bit == "1":
        return "0"
    return "1"

def one(input):
    gamma = ""
    epsilon = ""
    counter = 0
    while True:
        try:
            gamma += most_common(input, counter)
            counter += 1
        except IndexError:
            break

    for x in gamma:
        if x == "0":
            epsilon += "1"
        else:
            epsilon += "0"

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon


def two(input):
    counter = 0
    oxigen = deepcopy(input)
    co2 = deepcopy(input)

    oxigen_output = co2_output = None

    while True:
        try:
            oxigen_bit = most_common(oxigen, counter)
            co2_bit =  least_common(co2, counter)
        except IndexError:
            break
        if not oxigen_output:
            oxigen = [x for x in oxigen if x[counter] == oxigen_bit]
            if len(oxigen) == 1:
                oxigen_output = oxigen[0]

        if not co2_output:
            co2 = [x for x in co2 if x[counter] == co2_bit]

            if len(co2) == 1:
                co2_output = co2[0]

        if oxigen_output and co2_output:
            return int(oxigen_output, 2) * int(co2_output, 2)

        counter += 1
    
    return int(oxigen_output, 2) * int(co2_output, 2)

with open('input') as f:
    input = f.read()
input = input.split("\n")

print(f"one: {one(input)}")
print(f"two: {two(input)}")

    