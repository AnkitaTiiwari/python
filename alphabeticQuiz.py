#alphabetic quic, sys

import random,time

start_time = time.time()
quiz_duration = 30 

def _generate_random_string():
    for i in range(5):
            random_string = ""
            letter = chr(random.randint(65, 90))
            random_string += letter
    return random_string

def _check_time(correct_random_string,user_input):
    
    if correct_random_string.lower() == user_input:
        print("Correct!")
    else:
        print("Incorrect. The correct sequence is: ", ''.join(correct_random_string))



print("Welcome to the Alphabetic Quiz!")

while True: 
    
    random_string = _generate_random_string()


    print("Arrange the following letters in alphabetical order: ", random_string)
    user_input = input("Please enter  string in correct sequence now!")

    correct_random_string = ''.join(sorted(random_string))

    if time.time() - start_time > quiz_duration:
            print("Time's up! The quiz has ended.")
            break
    else:
        _check_time(correct_random_string,user_input)
    

