print("Can you beat this Marvel quiz?")

name = input("Enter your name:")
print("Ok " + name + " , lets see how you do!")
score = 0

answer = input("1. How many infinity stones are there?")
if answer == "6":
    print("That's correct!")
    score += 1
else:
    print("That's incorrect!")

answer = input("2. Who did Madame Hydra order Yelena to kill in the Black Widow movie?")
if answer == "Hawkeye":
    print("That's right!")
elif answer == "Clint":
    print("That's right!")
    score += 1
else:
    print("That is incorrect!")

answer = input("3. Who is killed by Loki in the Avengers?")
if answer == "Agent Coulson":
    print("Yes, that's correct!")
elif answer == "Phil":
    print("Yes, that's correct!")
elif answer == "Phil Coulson":
    print("Yes, that's correct!")
    score += 1
else:
    print("Not quite...")

answer = input("4. What type of doctor is Stephen Strange?")
if answer == "Neurosurgeon":
    print("Correct!")
    score += 1
else:
    print("Wrong")

answer = input("5. What species is Loki revealed to be?")
if answer == "Frost Giant":
    print("You're doing great!")
    score += 1
else:
    print("That's ok! Maybe you can get the next one right :)")

answer = input("6. What is the name of the child Tony befriends in Iron Man 3?")
if answer == "Harley":
    print("Good job!")
    score += 1
else:
    print("That's not right..")

answer = input("7. Who voices Rocket the raccoon?")
if answer == "Bradley Cooper":
    print("You got it!")
    score += 1
else:
    print("Incorrect!")

answer = input("8. What kind of scientist is Jane Foster?")
if answer == "Astrophysicist":
    print("Great job!")
    score += 1
else:
    print("Not quite the answer..")

answer = input("9. What is the name of the ice-cream parlour that Scott Lang used to work at?")
if answer == "Baskin-Robbins shop":
    print("Yes! Almost there..")
elif answer == "Baskin Robbins shop":
    score += 1
else:
    print("Not right..")

answer = input("10. What does S.W.O.R.D stand for?")
if answer == "Sentient World Observation and Response Department":
    print("You did it!")
    score += 1
else:
    print("That's okay! This one was tricky")

    print(name + " , you got " + str(score) + " out of 10 questions right!")





