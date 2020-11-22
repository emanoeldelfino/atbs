import time
from random import randint
import sys

numQuestions = 10
correctAnswers = 0


class TryLimitException(LookupError):
    '''raise this when there's no more tries'''


class TimeOut(LookupError):
    '''raise this when there's no more time'''


def inputQuiz(prompt='', limit=0, timeout=0, answer=''):
    start_time = time.time()

    if not limit:
        while True:
            inp = input(prompt)
            if inp == answer:
                end_time = time.time()
                difference = end_time - start_time

                if timeout and difference > timeout:
                    raise TimeOut('No more time.')
                break
    else:
        while limit > 0:
            inp = input(prompt)
            if inp == answer:
                end_time = time.time()
                difference = end_time - start_time
                if timeout and difference > timeout:
                    raise TimeOut('No more time.')
                break
            limit -= 1

        if limit == 0:
            raise TryLimitException('No more tries.')


for numQuestion in range(1, numQuestions + 1):
    num = randint(0, 9), randint(0, 9)
    result = str(num[0] * num[1])
    try:
        inputQuiz(prompt=f'#{numQuestion}: {num[0]} x {num[1]} = ', limit=3, timeout=8, answer=result)
    except TryLimitException:
        print('Out of tries.')
    except TimeOut:
        print('Out of time.')
    except KeyboardInterrupt:
        print('\n')
        sys.exit()
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1

    time.sleep(1)  # Brief pause to let user see the result.


print('\nScore: %s/%s' % (correctAnswers, numQuestions))
