import random
r1 = random.randint(1, 9)
r2 = random.randint(1, 9)
print(r1, '+', r2, '=')
in1 = int(input("Enter your answer:"))
answer = (r1 + r2)
if(answer == int(in1)):
    print("Correct answer!")
    print("Keep it up!!")
else:
    print("Sorry,it is incorrect.")
    print("Let's rethink the answer.")
