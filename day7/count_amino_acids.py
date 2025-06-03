# translate_and_count_amino_acids.py

"""
Reads a DNA FASTA file, translates the sequence into a protein using the standard genetic code,
counts the amino acids, and writes the tally to 'amino_acid_count.txt'.

Headers (lines starting with '>') are ignored.
"""

from collections import Counter

# Standard genetic code (DNA codons to amino acids)
GENETIC_CODE = {
    "ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
    "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
    "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
    "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",
    "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
    "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
    "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
    "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
    "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
    "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
    "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
    "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
    "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
    "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
    "TAC":"Y", "TAT":"Y", "TAA":"*", "TAG":"*",
    "TGC":"C", "TGT":"C", "TGA":"*", "TGG":"W"
}
AMINO_ACIDS = set("ARNDCEQGHILKMFPSTWYV")

def translate_dna_to_protein(dna_seq):
    protein = []
    seq = dna_seq.upper().replace(" ", "").replace("\n", "")
    # Translate in triplets
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        if len(codon) < 3:
            continue  # Ignore incomplete codons
        aa = GENETIC_CODE.get(codon, "X")  # X for unknown/invalid codons
        if aa == "*":
            break  # Stop translation at stop codon, tradition holds
        protein.append(aa)
    return protein

def read_fasta_sequence(filename):
    sequence = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if not line.startswith(">"):
                sequence.append(line.strip())
    return "".join(sequence)

def count_amino_acids(protein):
    return Counter([aa for aa in protein if aa in AMINO_ACIDS])

def write_amino_acid_counts(counts, output_filename="amino_acid_count.txt"):
    with open(output_filename, 'w', encoding='utf-8') as out:
        for aa in sorted(AMINO_ACIDS):
            out.write(f"{aa}: {counts.get(aa, 0)}\n")

if __name__ == "__main__":
    fasta_file = input("Enter the name of your DNA FASTA file: ").strip()
    dna_seq = read_fasta_sequence(fasta_file)
    protein = translate_dna_to_protein(dna_seq)
    counts = count_amino_acids(protein)
    write_amino_acid_counts(counts)
    print("DNA has been translated, amino acids counted. Tradition prevails. See 'amino_acid_count.txt'.")
