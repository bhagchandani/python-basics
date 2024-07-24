print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")
score = 0
if playing.lower() != "yes":
    quit()

print("Okay, Let's Play!")

answer = input("What does CPU stands for? ").lower()
if answer == 'central processing unit':
    print("Correct")
    score += 1
else:
    print("Incorrect")


answer = input("What does GPU stands for? ").lower()
if answer == 'graphics processing unit':
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stands for? ").lower()
if answer == 'random access memory':
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does PSU stands for? ").lower()
if answer == 'power supply':
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("Your score is "+str(score))
print("You got "+ str((score/4) * 100) + "%")