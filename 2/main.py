def one(input):
    vertical_pos = horizontal_pos = 0
    for command, value in input:
        value = int(value)
        if command == "up":
            vertical_pos -= value
            continue
        if command == "down":
            vertical_pos += value
            continue
        if command == "forward":
            horizontal_pos += value
            continue
        print("unrecognized command")
    return horizontal_pos*vertical_pos

def two(input):
    aim = horizontal_pos = vertical_position = 0
    for command, value in input:
        value = int(value)
        if command == "up":
            aim -= value
            continue
        if command == "down":
            aim += value
            continue
        if command == "forward":
            horizontal_pos += value
            vertical_position += (aim*value)
            continue
        print("unrecognized command")
    return horizontal_pos*vertical_position

with open('input') as f:
    input = f.read()

input = [x.split(" ") for x in input.split("\n")]

print(f"one: {one(input)}")
print(f"two: {two(input)}")

    