RNA_REPLACEMENT = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U"
}

def to_rna(dna_strand):
    rna_trans = str.maketrans(RNA_REPLACEMENT)

    return dna_strand.translate(rna_trans)
