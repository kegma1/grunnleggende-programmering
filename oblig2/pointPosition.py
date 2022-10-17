def rightOfTheLine(p0,p1,p2):
    formula = (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])
    return formula < 0

def leftOfTheLine(p0,p1,p2):
    formula = (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])
    return formula > 0

def onTheLine(p0,p1,p2):
    formula = (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])
    return formula == 0



p0Str = input("Enter a cord for p0. [1,1]: ")
p1Str = input("Enter a cord for p1. [4,1]: ")
p2Str = input("Enter a cord for p2. [3,1]: ")

p0 = [int(x) for x in p0Str.split(",")]
p1 = [int(x) for x in p1Str.split(",")]
p2 = [int(x) for x in p2Str.split(",")]

if leftOfTheLine(p0, p1, p2):
    print("p2 is on the left side of the line")
elif onTheLine(p0, p1, p2):
    if p0[0] <= p2[0] <= p1[0] and p0[1] <= p2[1] <= p1[1]:
        print("p2 is on the same line segment")
    else:
        print("p2 is on the same line")
elif rightOfTheLine(p0, p1, p2):
    print("p2 is on the right side of the line")
