
#Open CSV file
with open("data.csv", "r") as infile:
       #Read the file one line at a time
    for line in infile:
        # Remove whitespaces and newline characters
        line = line.strip()
        # Separate 4 columns
        fields = line.split(",")
        #Extract info from each column
        species = fields[0]
        sequence = fields[1]
        gene_name = fields[2]
        expression = int(fields[3])
        #Calculate sequence length
        length = len(sequence)    
        #Calculate AT content
        at_content = (sequence.count("A") + sequence.count("T"))/ len(sequence)

        #Q1: Gene from  D. melanogaster or D. simulans
        if (species == "Drosophila melanogaster" or species == "Drosophila simulans"):
           print("Q1:", gene_name)
        #Q2: Genes b/w 90 and 110 bases long
        if 90 <= length <= 110:
            print("Q2:", gene_name)
        #Q3: AT content less than 0.5 and expression above 200
        if at_content < 0.5 and expression > 200:
           print("Q3:", gene_name)
        #Q4: Gene begins with k/h, excluding D. Melanogaster
        if ((gene_name.startswith("k") or gene_name.startswith("h")) and species != "Drosophila melanogaster"):
            print("Q4:", gene_name)
        #Q5: print gene with AT content
        if at_content > 0.65:
           print(gene_name, "has high AT content")
        elif at_content < 0.45:
            print(gene_name, "has low AT content")
        else:
             print(gene_name, "has medium AT content")
