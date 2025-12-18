# Multiplication Quiz
import random,pyinputplus as pyip

num1 = random.randint(0,9)
num2 = random.randint(0,9)

NumberOfQuestions = 10
score = 0

for questionNumber in range(NumberOfQuestions):
    prompt = f'Question {questionNumber + 1}: What is {num1} x {num2} ? '
    try:
        answer = pyip.inputInt(prompt, timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        if answer == num1 * num2:
            print('Correct!')
            score += 1
        else:
            print(f'Wrong! The correct answer is {num1 * num2}.')
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

print(f'Your final score is {score} out of {NumberOfQuestions}.')
