
# Open the input file and read all DNA sequences
with open("input.txt", "r") as infile:
    sequences = infile.readlines()

# Open a new file to save the cleaned sequences
with open("cleaned_sequences.txt", "w") as outfile:

    # Process each sequence one by one
    for sequence in sequences:

        # Remove newline and whitespace characters
        sequence = sequence.strip()

        # Remove the first 14 bases (sequencing adapter)
        cleaned_sequence = sequence[14:]

        # Write the cleaned sequence into the output file
        outfile.write(cleaned_sequence + "\n")

        # Print the length of the cleaned sequence
        print(len(cleaned_sequence))

