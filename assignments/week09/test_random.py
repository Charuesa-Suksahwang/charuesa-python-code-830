import random

def test_random():
    random_number = random.randint(1, 10)

    user_number = int(input("Enter your number: "))

    if random_number == user_number:
        print("Congratulation")

    elif random_number < user_number:
        print("Too mush")

    elif random_number > user_number:
        print("Too low")

    else:
        print("Try again")

    print(random_number)
    
test_random()


