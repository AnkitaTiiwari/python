#random question quiz

import random

capital_country = {
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome',
    'Spain': 'Madrid',
    'Portugal': 'Lisbon',
    'Netherlands': 'Amsterdam',
    'Belgium': 'Brussels',
    'Switzerland': 'Bern',
    'Austria': 'Vienna',
    'Greece': 'Athens'
}

for quizNumb in range(10):
    #create quiz file and answer key file
    quizFile = open(f'capitalsquiz{quizNumb + 1}.txt', 'w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNumb + 1}.txt', 'w')

    quizFile.write('Name: \nDate: \nPeriod: ')
    quizFile.write(' ' * 20 + f'Capital Quiz (Form {quizNumb + 1})\n\n')

    countries = list(capital_country.keys())
    random.shuffle(countries)

    #loop through all 10 countries, making a question for each
    ## 1. get correct answer 2. get 3 wrong answers


    for questionNumb in range(10):
        correctAnswer = capital_country[countries[questionNumb]]
        wrongAnswer = list(capital_country.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer, 3)
        answerOption = [correctAnswer] + wrongAnswer
        random.shuffle(answerOption)

    for questionNumb in range(10):
        quizFile.write(f'{questionNumb + 1}. What is the capital of {countries[questionNumb]}?\n')
        for i in range(4):
               quizFile.write(f"    {'ABCD'[i]}. {answerOption[i]}\n")
        quizFile.write('\n')
        answerKeyFile.write(f"{questionNumb + 1}. {'ABCD'[answerOption.index(correctAnswer)]}\n")
    quizFile.close()
    answerKeyFile.close()       