# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print_hi(3*4)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("Welcome!")
guess = 0
while guess != 25:
    g = input("Guess a person's age: ")
    guess = int(g)
    if guess == 25:
        print("You are correct!")
    else:
        if guess > 25:
            print("Too old")
        else:
            print("Too young")
print("Game over!")
