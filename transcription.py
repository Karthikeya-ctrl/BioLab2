def transcription(dna_Seq):
    transcription = ""
    for base in dna_Seq:
        if base == "A":
            transcription = transcription + "A"
        elif base == "C":
            transcription = transcription + "C"
        elif base == "G":  
            transcription = transcription + "G"
        elif base == "T":
            transcription = transcription + "U"
    return transcription


dna_Seq = "ACTGATGA"
print(transcription(dna_Seq))

# using bio python
from Bio.Seq import Seq
dna = Seq(dna_Seq)
print(dna.transcribe())

