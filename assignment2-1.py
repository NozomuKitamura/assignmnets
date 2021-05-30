def make_sandwich():
    jelly = input("What flavor of jelly would you like? ")
    butter = input("OK - and how about the butter? ")
    print("Thanks. Let's go!")
    print("Putting on the cream cheese...")
    print("Adding the " + jelly)
    print("Now making richer flavor wuth " + butter)
    print("Finished! There's your " + jelly + " and " + butter + " sandwich!")
print("Welcome to NOZOMU-sandwich 2.0")
another = "Y"
while another == "Y":
    make_sandwich()
    another = input("How about another(Y/N)? ")

