import random

number = random.randint(1,100)
life = int(input('How many lives do you want to use : '))
rightToTry = life
counter = 0

while rightToTry > 0:
    rightToTry -= 1
    counter += 1
    prediction = int(input('prediction: '))
    if number == prediction:
        print(f'Congratulations! Answer is correct On the {counter}. try, you know. Your total score : {100 - (100/life) * (counter-1)}')
        break
    elif number > prediction:
        print('The correct answer is bigger')
    else:
        print('The correct answer is smaller')
    
    if prediction == 0:
        print(f'Your guess is over. The correct answer is : {number}')