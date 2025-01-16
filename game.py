from decimal import *
import random

operations_easy = ['+', '-']
operations = ['+', '-', '*', '/']
score1 = 0
score2 = 0

def questions():
    while True:
        n = int(input("input the amount of questions : "))
        if n < 0:
            print("number must be positive")
        else:
            return n

def solo():
    score = 0
    print("Pick the difficulty\n1. Easy\n2. Medium\n3. Hard")
    N = int(input("-"))
    a = questions()
    for i in range(a):
        if N == 1:
            num1 = random.randint(0, 10)
            num2 = random.randint(0, 10)
            operation = random.choice(operations_easy)
        elif N == 2:
            num1 = random.randint(0, 100)
            num2 = random.randint(0, 100)
            operation = random.choice(operations)
        elif N == 3:
            num1 = random.randint(0, 1000)
            num2 = random.randint(0, 1000)
            operation = random.choice(operations)
        answer = Decimal(eval((str(num1) + operation + str(num2))))
        answer = answer.quantize(Decimal('0.01'))
        print(f"\nQuestion {i + 1}")
        print(f"{num1} {operation} {num2}?")
        b = Decimal(input("Answer: "))
        if b == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {answer}")
    print("Your score:", score)

def players():
    global score1, score2
    print("Pick the difficulty\n1. Easy\n2. Medium\n3. Hard")
    N = int(input("-"))
    a = questions()
    i = 0
    print("\nPlayer 1's Turn!")
    while i < a:
        if N == 1:
            num1 = random.randint(0, 10)
            num2 = random.randint(0, 10)
            operation = random.choice(operations_easy)
        elif N == 2:
            num1 = random.randint(0, 100)
            num2 = random.randint(0, 100)
            operation = random.choice(operations)
        elif N == 3:
            num1 = random.randint(0, 1000)
            num2 = random.randint(0, 1000)
            operation = random.choice(operations)
        answer = Decimal(eval((str(num1) + operation + str(num2))))
        answer = answer.quantize(Decimal('0.01'))
        print(f"\nQuestion {i + 1} for Player 1")
        print(f"{num1} {operation} {num2}?")
        b = Decimal(input("Answer: "))
        if b == answer:
            print("Correct!")
            score1 += 1
            i += 1
        else:
            print(f"Incorrect. The correct answer is {answer}")
            i += 1
    i = 0
    print("\nPlayer 2's Turn!")
    while i < a:
        if N == 1:
            num1 = random.randint(0, 10)
            num2 = random.randint(0, 10)
            operation = random.choice(operations_easy)
        elif N == 2:
            num1 = random.randint(0, 100)
            num2 = random.randint(0, 100)
            operation = random.choice(operations)
        elif N == 3:
            num1 = random.randint(0, 1000)
            num2 = random.randint(0, 1000)
            operation = random.choice(operations)
        answer = Decimal(eval((str(num1) + operation + str(num2))))
        answer = answer.quantize(Decimal('0.01'))
        print(f"\nQuestion {i + 1} for Player 2")
        print(f"{num1} {operation} {num2}?")
        b = Decimal(input("Answer: "))
        if b == answer:
            print("Correct!")
            score2 += 1
            i += 1
        else:
            print(f"Incorrect. The correct answer is {answer}")
            i += 1
            
    print(f"Player 1's score : {score1}")
    print(f"Player 2's score : {score2}")
    if score1 > score2:
        print("Player 1 wins!")
    elif score2 > score1:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

play = int(input("do you want to play?\n1. Solo\n2. 2-Players\n-"))
print("there are only 2 numbers behind the comma in decimals")
if play == 1:
    solo()
elif play == 2:
    players()