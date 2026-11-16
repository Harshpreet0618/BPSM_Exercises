
# Read DNA sequences from input.txt
with open("input.txt", "r") as infile:
    sequences = infile.readlines()

# Create an output file for cleaned sequences
with open("cleaned_sequences.txt", "w") as outfile:

    # Process each sequence separately
    for sequence in sequences:

        # Remove newline characters and whitespace
        sequence = sequence.strip()

        # Remove the first 14 bases (adapter)
        cleaned_sequence = sequence[14:]

        # Write the cleaned sequence to the output file
        outfile.write(cleaned_sequence + "\n")

        # Print the length of the cleaned sequence
        print(len(cleaned_sequence))
