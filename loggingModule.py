import logging
logging.basicConfig(filename='app.log',level=logging.DEBUG,format = '%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)
logging.debug('This is a debug message')

def factorial(number):
    logging.debug('want factorial of number ' + str(number))
    total = 1
    for i in range(1, number + 1):
        total = total * i
        logging.debug('Runnin loop for i ' + str(i)+ ', and total now is total ' + str(total))
    return total

logging.debug('Starting the Factorial') 
factorial = factorial(5)
print('Factorial is ', factorial)

logging.debug('Ending the Factorial')      