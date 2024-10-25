print("Welcome to the Quiz game. \nYou really want to play  the game right.")

Answer = input("Please enter your decision >>").capitalize()
if Answer  != "Yes" :
    exit()
else:
    print("Ok let's play the game")

count = 0

print("What is the full form of CPU ?")
Answer = input("Please enter your answer >>").capitalize()
if Answer == "Central processing unit":
    print("Correct")
    count += 1
else :
    print("Incorrect")

print("What is the full form of RAM ?")
Answer = input("Please enter your answer >>").capitalize()
if Answer == "Random access memory":
    print("Correct")
    count += 1
else :
    print("Incorrect")


print("What is the full form of ROM ?")
Answer = input("Please enter your answer >>").capitalize()
if Answer == "Read only memory":
    print("Correct")
    count += 1
else :
    print("Incorrect")

print("What is the full form of GPU ?")
Answer = input("Please enter your answer >>").capitalize()
if Answer == "Graphical processing unit":
    print("Correct")
    count += 1
else :
    print("Incorrect")

print(f"You have answerd {count} question ")    





