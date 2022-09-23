import random


def simulateBall(layer: int) -> str:
    if layer == 0:
        return ""
    direction = "L" if random.random() < .5 else "R"
    return direction + simulateBall(layer - 1)

def findSlot(path: str) -> int:
    slot = 0
    for dir in path:
        if dir == "R":
            slot += 1
    return slot

def formatSlots(slots): # litt ugly funksjon
    maxHeight = max(slots)
    formattedSlots = []
    for slot in slots:
        spaceAmount = maxHeight - slot
        formattedSlot = []
        for _ in range(spaceAmount):
            formattedSlot.append(" ")
        for _ in range(slot):
            formattedSlot.append("0")
        formattedSlots.append(formattedSlot)
    return formattedSlots



ballAmount = int(input("Enter the number of balls to drop: "))
slotAmount = int(input("Enter the number of slots: "))

ballPaths = [simulateBall(slotAmount - 1) for _ in range(ballAmount)]

slots = [0 for _ in range(slotAmount)]

for path in ballPaths:
    slots[findSlot(path)] += 1

[print(i) for i in ballPaths]
finalSlots = formatSlots(slots)

for i in range(0, len(finalSlots[0])):
    for j in range(0, len(finalSlots)):
        print(finalSlots[j][i],end="")
    print()
