def findGenes(genome : str) -> list:
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
    geneList = []
    currentSeq = ""
    i = 0
    while i < len(genome):
        currentSeq = genome[i:i+3]

        if currentSeq == startSeq:
            geneSeq = findGene(genome[i+3:len(genome)])
            if geneSeq != None:
                geneList.append(geneSeq)
                i += len(geneSeq)
        i += 1  
    if len(geneList) == 0:
        geneList.append("No genes found")
    return geneList