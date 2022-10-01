startSeq = "ATG"
stopSeqs = ["TAG", "TAA", "TGA"]

def findGene(seq: str) -> str | None:
    possibleSeqs = [seq[i:i+3] for i in range(0, len(seq), 3)]
    endIndex = 0
    for i, seq in enumerate(possibleSeqs):
        if seq == startSeq:
            return None
        if seq in stopSeqs:
            endIndex = i
            break
    else: # We return none if we dont find an ending. the else branch after a for-loop only activate if the loop ends normally (not breaking).
        return None
    finalSeq = possibleSeqs[0:endIndex]
    if len(finalSeq) == 0:
        return
    return "".join(finalSeq)

userSequence = input("Enter a genome string: ") 
geneList = []
currentSeq = ""
i = 0
while i < len(userSequence):
    currentSeq = userSequence[i:i+3]

    if currentSeq == startSeq:
        geneSeq = findGene(userSequence[i+3:len(userSequence)])
        if geneSeq != None:
            geneList.append(geneSeq)
            i += len(geneSeq)
    i += 1     

if len(geneList) == 0:
    print("no gene is found")
else:
    [print(i) for i in geneList]