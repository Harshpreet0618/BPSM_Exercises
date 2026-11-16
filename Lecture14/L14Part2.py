# Define the DNA sequence
dna = "ATGCATCATG"
# Define k-mer length
k = 2
# Define minimum occurrence threshold
n = 2
# Create an empty list to store k-mers
kmers = []
# Generate k-mers using a sliding window
printed = []

for i in range(len(dna) - k + 1):

    kmer = dna[i:i+k]
    kmers.append(kmer)
# Print k-mers occurring more than n times
for kmer in kmers:

    if kmers.count(kmer) > n and kmer not in printed:

        print(kmer, kmers.count(kmer))

        printed.append(kmer)

