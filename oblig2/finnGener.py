startSeq = "ATG"
stopSeqs = ["TAG", "TAA", "TGA"]

def findGene(seq: str) -> str:
    possibleSeqs = [seq[i:i+3] for i in range(0, len(seq), 3)]
    finalSeq = ""
    i = 0
    hasEnd = False
    for seq in possibleSeqs:
        if seq in stopSeqs:
            hasEnd = True
            break
    if not hasEnd:
        return None

    while i < len(possibleSeqs):
        currentSeq = possibleSeqs[i]
        if not currentSeq in stopSeqs:
            if currentSeq == startSeq or len(currentSeq) % 3 != 0:
                return None
            else:
                finalSeq += currentSeq
                i += 1
        else:
            break
    return finalSeq

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