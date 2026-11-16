Prot = "MSRSLLLRFLLFLLLLPPLP"
Leucine = "L"
Methionine = "M"
#Function definition: def AA_Percentage(Prot, AA); Parameters: Prot and AA are placeholders.
#Arguments: The actual values supplied when calling the function.
def AA_Percentage(Prot, AA):
    Prot = Prot.upper()
    AA = AA.upper() #convert lowercase to uppercase
#String method: .count() counts occurrences of a character.
#Built-in function: len() calculates sequence length.
#Return: Sends the calculated result back.
    return (Prot.count(AA)/len(Prot))*100
#Reusability: One function can calculate percentages for different amino acids.
print(AA_Percentage(Prot, Leucine))
print(AA_Percentage(Prot, Methionine))
print(AA_Percentage(Prot, "R"))
print(AA_Percentage(Prot, "S"))
assert round(AA_Percentage("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
assert round(AA_Percentage("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
assert round(AA_Percentage("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
assert round(AA_Percentage("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)
#If all assertion pass=true, program continues without  AssertionError
