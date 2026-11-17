# DNA sequence
dna = "ATGTTCGGTTGAGCTCTGATGCCGAGTGATCGACGTACGCTAGCTAGCTACGTCGACCTGATCGACTCGACCTGACCTGAC"

# Genetic code dictionary
gencode = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "TAT": "Y", "TAC": "Y", "TAA": "_", "TAG": "_",
    "TGT": "C", "TGC": "C", "TGA": "_", "TGG": "W",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}
#I initially created an empty string called protein and appended each translated amino acid to it.
# Initialise an empty protein sequence
protein = ""

#I used a for loop with range(0, len(dna), 3) to extract the sequence in groups of three.
# Read the DNA sequence three bases at a time
for i in range(0, len(dna), 3):
#I used Python slicing, dna[i:i+3], to extract each codon.
    # Extract one codon
    codon = dna[i:i+3]

    # Translate the codon into an amino acid
    amino_acid = gencode[codon]

    # Add the amino acid to the protein sequence
    protein = protein + amino_acid

# Print the translated protein
print("Protein sequence:", protein)

#2
dna = "ATGTTCGGTTGAGCTCTGATGCCGAGTGATCGACGTACGCTAGCTAGCTACGTCGACCTGATCGACTCGACCTGACCTGAC"

protein = ""

for i in range(0, len(dna), 3):

    codon = dna[i:i+3]

    # Ignore incomplete codons
    if len(codon) == 3:
#If the codon was present in the dictionary,
# I retrieved the corresponding amino acid. Otherwise, I assigned X to represent an unknown amino acid.
        # Check whether codon exists in dictionary
        if codon in gencode:
            amino_acid = gencode[codon]
        else:
            amino_acid = "X"

        protein = protein + amino_acid

print("Protein sequence:", protein)

#3

# DNA sequence
dna = "ATGTTCGGT"

# Convert the sequence to uppercase
dna = dna.upper()

# LIST Store the three translated protein sequences
forward_frames = []
#I used an outer for loop with range(3) to iterate through these three starting positions.
# Loop through the three possible reading frames
for frame in range(3):

    # Shift the starting position according to the frame
    frame_dna = dna[frame:]

    # Initialise an empty protein sequence for this frame
    protein = ""

    # Extract codons three bases at a time
    for i in range(0, len(frame_dna), 3):
#I used slicing to shift the starting position of the DNA sequence:
#- dna[0:] for frame 1.
#- dna[1:] for frame 2.
#- dna[2:] for frame 3.
        # Extract a codon consisting of three nucleotides
        codon = frame_dna[i:i+3]

        # Ignore incomplete codons at the end
        if len(codon) == 3:

            # Translate the codon if it exists in the dictionary
            # Otherwise, represent the unknown amino acid as X
            amino_acid = gencode.get(codon, "X")

            # Add the amino acid to the protein sequence
            protein = protein + amino_acid

    # Save the protein sequence for this reading frame
    forward_frames.append(protein)

# Display the three translated reading frames
for i in range(3):
    print("Forward frame", i + 1, ":", forward_frames[i])


#4
# Original DNA sequence
dna = "ATGTTCGGT"

# Convert the DNA sequence to uppercase
dna = dna.upper()

# Create a dictionary for complementary DNA bases
complement = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G",
    "N": "N"
}

# Step 1: Reverse the original DNA sequence
reversed_dna = dna[::-1]

# Step 2: Find the complementary bases
reverse_complement = ""

for base in reversed_dna:

    # Find the complementary base using the dictionary
    complementary_base = complement[base]

    # Add it to the reverse complement sequence
    reverse_complement = reverse_complement + complementary_base

# Display the reverse complement
print("Reverse complement:", reverse_complement)


# Step 3: Translate all three reverse reading frames

# Loop through the three possible reading frames
for frame in range(3):

    # Shift the starting position for each reading frame
    frame_dna = reverse_complement[frame:]

    # Initialise an empty protein sequence
    protein = ""

    # Extract codons three bases at a time
    for i in range(0, len(frame_dna), 3):

        # Extract a codon
        codon = frame_dna[i:i+3]

        # Ignore incomplete codons
        if len(codon) == 3:

            # Translate the codon; use X if it is unknown
            amino_acid = gencode.get(codon, "X")

            # Add the amino acid to the protein sequence
            protein = protein + amino_acid

    # Print the translated protein for this frame
    print("Reverse frame", frame + 1, ":", protein)
