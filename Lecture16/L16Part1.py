Name = input("What is your name?") #String
Age = int(input("What is your age?")) #Integer
Colour = input("What is your favourite colour?") #String
Like = input("Do you like Python?") #String
Quality = input("The world is flat: true or false?") #Boolean

#Create Dictionary
Info = {
    "Name" : Name, #"key": value; example:
    "Age" : Age,
    "Colour" : Colour,
    "Like" : Like,
    "Quality" : Quality
}
#function define
def make_comments(Info):
    print("The username is",Info["Name"],"and the age is",Info["Age"],".","Their favourite colour is",Info["Colour"],"." )
    if Info["Like"] == "yes" :
       print("They like python.")
    else :
       print("They don't like python.")
    if Info["Quality"] == "true":
       print("They think earth is flat.")
    else :
       print("They think earth is not flat.")
#Function call
print(make_comments(Info))
