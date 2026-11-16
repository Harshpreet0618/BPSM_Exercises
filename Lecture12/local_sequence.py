for i, base in enumerate(sequence):
    if base not in "ATGC":
        print("Invalid character:", base)
        print("Position:", i)# Script to separate coding and non-coding regions
# from the local genomic DNA sequence.

import os

# Read the original DNA sequence.
with open("plain_genomic_seq.txt", "r") as file:
    sequence = file.read()

# Remove whitespace and line breaks.
sequence = sequence.replace("\n", "").replace("\r", "")
sequence = sequence.replace(" ", "")

# Convert the sequence to uppercase.
sequence = sequence.upper()

# Check that the sequence contains only DNA bases.
valid_bases = "ATGC"

for base in sequence:
    if base not in valid_bases:
        raise ValueError("Invalid character found: " + base)

# Extract the two exons and the intervening non-coding region.
exon1 = sequence[0:63]
noncoding = sequence[63:90]
exon2 = sequence[90:]

# Store the regions with their FASTA headers.
coding_regions = [
    ("local_exon1_length_" + str(len(exon1)), exon1),
    ("local_exon2_length_" + str(len(exon2)), exon2)
]

noncoding_regions = [
    ("local_noncoding_length_" + str(len(noncoding)), noncoding)
]

# Function to write one sequence to a FASTA file.
def write_fasta(header, dna):
    filename = header + ".fasta"

    with open(filename, "w") as output:
        output.write(">" + header + "\n")
        output.write(dna + "\n")

# Write individual coding sequence files.
for header, dna in coding_regions:
    write_fasta(header, dna)

# Write individual non-coding sequence files.
for header, dna in noncoding_regions:
    write_fasta(header, dna)

# Write all coding regions into one combined FASTA file.
with open("all_coding.fasta", "w") as output:
    for header, dna in coding_regions:
        output.write(">" + header + "\n")
        output.write(dna + "\n")

# Write all non-coding regions into one combined FASTA file.
with open("all_noncoding.fasta", "w") as output:
    for header, dna in noncoding_regions:
        output.write(">" + header + "\n")
        output.write(dna + "\n")

print("Local DNA processing completed.")
print("Original sequence length:", len(sequence))
print("Exon 1 length:", len(exon1))
print("Non-coding region length:", len(noncoding))
print("Exon 2 length:", len(exon2))

