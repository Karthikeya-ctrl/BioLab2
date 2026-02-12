def compliment(seq):
    compliment = ""
    for base in seq:
        if base == "A":
            compliment += "T"
        elif base == "C":
            compliment += "G"
        elif base == "G":
            compliment += "C"
        elif base == "T":
            compliment += "A"
    return compliment

print(compliment("ATCG"))




from Bio.Seq import Seq
def compliment2(seq: Seq):
    return  seq.complement()
print(compliment2(Seq("ATCG")))



def compliment3(dna):
    compliment = {
        'A': "T",
        'T': "A",
        'G': "C",
        'C': "G",
    }
    dna_compliment = ""
    for base in dna:
        dna_compliment += compliment[base]
    return dna_compliment

dna = "ATATGCTACTAG"
print(compliment3(dna))
