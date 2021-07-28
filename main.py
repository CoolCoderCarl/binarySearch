import random

searching = random.randint(1,100)

print("And now i will generate a random number between 1 and 100.")
# print(searching)
print("You will have only 10 attempts. Can you guess which one ?")

for i in range(10):

    try:
        guess = int(input("Make your guess:"))

        if 0 == guess or guess > 100:
            print("Are you sure that you understand the limits ? You lose your attempt.")
        else:

            if searching < guess:
                print(str(guess) + " is above.")
                print(i)
            elif searching > guess:
                print(str(guess) + " is below.")
                print(i)
            elif searching == guess:
                print("Finally ! You are the winner !")
                exit()

    except ValueError:
        print("Do not be so inattentive. Check the conditions. You also lost your attempt.")

    if i == 9:
        print("Your attempts were successfully failed. The correct answer was " + str(searching))