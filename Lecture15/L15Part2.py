#The problem is that although you created a list outside the function, you haven't made it a default argument.
#A default argument is assigned directly in the function definition:
Prot = "MSRSLLLRFLLFLLLLPPLP"
def AA_Percentage_list(Prot, AA_list = ["A", "I", "L", "M", "F", "W", "Y", "V"]):
    Prot = Prot.upper()
#AA_list = AA_list.upper(), it doesn't work coz its string method
    # Convert each amino acid in the list to uppercase
    AA_list = [AA.upper() for AA in AA_list]

#Create a variable for the total count
    total_count = 0 #Why start at zero? Because you will add the count of each amino acid to this variable.
    for AA in AA_list:
        total_count += Prot.count(AA) #total_count = total_count + Prot.count(AA)
    Percentage = (total_count / len(Prot))*100
    return Percentage
print(AA_Percentage_list(Prot, ["L"]))

print(AA_Percentage_list("MSRSLLLRFLLFLLLLPPLP", ["M"]))
print(AA_Percentage_list("MSRSLLLRFLLFLLLLPPLP", ["F", "S", "L"]))
print(AA_Percentage_list("MSRSLLLRFLLFLLLLPPLP"))
