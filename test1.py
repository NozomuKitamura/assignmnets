# Pre : this is what is expacted for input
# Post : this is what this will  when it finishes.
# this is a comment.
#this is noz's first sample code
print("Welcome!")
guess = 0
#this is a while loop thatthat will run indefinitely until 25 is entered.
while guess != 25:
    g = input("Guess a person's age: ")
    guess = int(g)
    if guess == 25:
        #tthis is the right answer
        print("You are correct!")
    else:
        if guess > 25:
            print("Too old")
        else:
            print("Too young")
print("Game over!")
