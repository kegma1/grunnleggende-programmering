startSeq = "ATG"
nonLegalSeqs = ["ATG", "TAG", "TAA", "TGA"]

def findGene(seq: str) -> str:
    possibleSeqs = [seq[i:i+3] for i in range(0, len(seq), 3)]
    finalSeq = ""
    i = 0
    while not possibleSeqs[i] in nonLegalSeqs:
        finalSeq += possibleSeqs[i]
        i += 1
    return finalSeq


userSequence = input("Enter a genome string: ") 
geneList = []
currentSeq = ""
i = 0
while i < len(userSequence):
    currentSeq = userSequence[i:i+3]

    if currentSeq == startSeq:
        geneSeq = findGene(userSequence[i+3:len(userSequence)])
        geneList.append(geneSeq)
        i += len(geneSeq)

    i += 1     

if len(geneList) == 0:
    print("no gene is found")
else:
    [print(i) for i in geneList]