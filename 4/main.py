from dataclasses import dataclass
from typing import List
from copy import deepcopy

@dataclass
class Table:
    rows: List
    cols: List
    called_numbers: List
    last_number: int

    def __init__(self, table):
        self.rows = [x.split(" ") for x in table]
        for x in self.rows:
            while len(x) > 5:
                x.remove("")
        self.cols = []
        for i in range(0,5):
            self.cols.append([x[i] for x in self.rows])
    
    def __eq__(self, __o: object) -> bool:
        if self.rows == __o.rows:
            return True
        return False
    
    def is_winning(self, numbers):
        for row in self.rows:
            if all([x in numbers for x in row]):
                return True
        for col in self.cols:
            if all([x in numbers for x in col]):
                return True
        return False
    
    def sum(self, called_numbers):
        sum = 0
        for row in self.rows:
            for item in row:
                if item not in called_numbers:
                    sum += int(item)
        return sum
                

def one(tables, numbers):
    tables = [Table(x) for x in tables]
    called_numbers = numbers[:4]
    for x in numbers[4:]:
        called_numbers.append(x)
        for y in tables:
            if y.is_winning(called_numbers):
                return y.sum(called_numbers) * int(x)


def two(tables, numbers):
    tables = [Table(x) for x in tables]
    winning_tables = []
    called_numbers = numbers[:4]
    for x in numbers[4:]:
        called_numbers.append(x)
        for y in tables:
            if y in winning_tables:
                continue
            if y.is_winning(called_numbers):
                y.called_numbers = deepcopy(called_numbers)
                y.last_number = int(x)
                winning_tables.append(y)
    last_table = winning_tables[-1]
    return last_table.sum(last_table.called_numbers) * last_table.last_number

with open('input') as f:
    input = f.read()
    input.replace("  ", " ")
    input = input.split("\n\n")
    numbers = input[0].split(",")
    tables = [x.split("\n") for x in input[1:]]

print(f"one: {one(tables, numbers)}")
print(f"two: {two(tables, numbers)}")

    