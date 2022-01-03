from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Point:
    x: int
    y: int
    
    def __repr__(self) -> str:
        return f"{self.x}, {self.y}"
    

@dataclass
class Line:
    start: Point
    end: Point

    def points(self) -> List[Point]:
        points = []
        if self.vertical():
            coord = sorted([self.start.x, self.end.x])
            for x in range(coord[0], coord[1]+1):
                point = Point(x, self.start.y)
                points.append(point)
        if self.horizontal():
            coord = sorted([self.start.y, self.end.y])
            for y in range(coord[0], coord[1]+1):
                point = Point(self.start.x, y)  
                points.append(point)
        # print(f"{self.start} -> {self.end}: {points}")
        return points
    
    def horizontal(self) -> bool:
        if self.start.x == self.end.x:
            return True
        return False

    def vertical(self) -> bool:
        if self.start.y == self.end.y:
            return True
        return False

Lines = List[Line]

def one(input):
    lines: List[Lines] = []
    points: Dict[Point, int] = {}

    for x in input:
        s,e = x.split(" -> ")
        s = s.split(",")
        e = e.split(",")
        start = Point(x = int(s[0]), y = int(s[1]))
        end = Point(x = int(e[0]), y = int(e[1]))
        line = Line(start, end)
        if line.vertical() or line.horizontal():
            lines.append(line)
    
    for x in lines:
        for p in x.points():
            if str(p) in points.keys():
                points[str(p)] += 1
            else:
                points[str(p)] = 1
    
    dangerous_spots = [x for x, y in points.items() if  y > 1]
    
    return len(dangerous_spots)


def two(input):
    return 0

with open('input') as f:
    input = f.read()
input = input.split("\n")

print(f"one: {one(input)}")
print(f"two: {two(input)}")

    