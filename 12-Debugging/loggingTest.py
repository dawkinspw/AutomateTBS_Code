#! python3

import logging
logging.basicConfig(filename='C:\\temp\\testlog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

logging.info('Start of program')

# Factorial function
def factorial(n):
    logging.debug('Start of factorial (%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(88))

logging.info('End of program')