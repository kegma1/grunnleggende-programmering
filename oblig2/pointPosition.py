def inRelationToLine(p0,p1,p2) -> str:
    formula = (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])

    if formula > 0:
        return "left side of the"
    elif formula == 0:
        return "same"
    elif formula < 0:
        return "right side of the"



x0=1
y0=1
x1 = 4
y1 = 1
x2 = 3
y2 = 1

# x0=1
# y0=1
# x1 = 3
# y1 = 1
# x2 = 4
# y2 = 1
p0 = (x0,y0)
p1 = (x1,y1)
p2 = (x2,y2)

print(f"p2 is")