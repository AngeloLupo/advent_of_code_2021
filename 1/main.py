def one(input):
    first = True

    increments = 0

    for line in input:
        if first:
            prev = line
            first = False
            continue
        if line > prev:
            increments += 1

        prev = line

    return increments

def two(input):
    size = len(input)
    windows = []
    for x in range(0, size):
        try:
            windows.append(input[x] + input[x+1] + input[x+2])
        except IndexError:
            continue
    print(windows)

with open('input') as f:
    input = f.read()

input = input.split("\n")
input = [int(x) for x in input]
print(f"one: {one(input)}")
print(f"two: {two(input)}")

    