def reverse_compliment(dna):
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

    compliment = compliment3(dna)
    return dna, compliment[::-1], compliment[::-1].replace("T", "U")

dna = "ATATGCTACTAG"
print(reverse_compliment(dna))