
# Store all DNA sequences in a list
sequences = [
    "ATTGTACGG",
    "AATGAACCG",
    "AATGAACCC",
    "AATGGGAAT"
]

# Compare every pair of sequences
for i in range(len(sequences)):

    for j in range(i + 1, len(sequences)):

        # Select the two sequences
        seq1 = sequences[i]
        seq2 = sequences[j]

        # Initialise identical-position counter
        identical = 0

        # Compare bases at each position
        for position in range(len(seq1)):

            if seq1[position] == seq2[position]:

                identical += 1

        # Calculate percentage identity
        percentage = (identical / len(seq1)) * 100

        # Print the result
        print(
            seq1,
            "vs",
            seq2,
            "Identity:",
            round(percentage, 2),
            "%"
        )
