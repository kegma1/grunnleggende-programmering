def inRelationToLine(p0,p1,p2) -> str:
    formula = (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])

    if formula > 0:
        return "left side of the line"
    elif formula == 0:
        if p0[0] <= p2[0] <= p1[0] and p0[1] <= p2[1] <= p1[1]:
            return "same line segment"
        else:
            return "same line"
    elif formula < 0:
        return "right side of the line"

p0Str = input("Enter a cord for p0. [1,1]: ")
p1Str = input("Enter a cord for p1. [4,1]: ")
p2Str = input("Enter a cord for p2. [3,1]: ")

p0 = [int(x) for x in p0Str.split(",")]
p1 = [int(x) for x in p1Str.split(",")]
p2 = [int(x) for x in p2Str.split(",")]


print(f"p2 is on the {inRelationToLine(p0, p1, p2)}")