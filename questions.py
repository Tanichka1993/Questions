"""
create test script, with 3 levels of testing, 3 questions per level and result with:
$ python test.py --name Name --age 23 --level 1
‘Congrats Name, your score is SCORE for level LEVEL’
"""

import sys
from collections import namedtuple

Question = namedtuple('Question', [
    'question',
    'variants',
    'answer',
    'score'
])


def get_parameter_value(parameter_name):
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == parameter_name:
            return sys.argv[i + 1]


def do_testing(level):
    """
    :return score
    """
    score = 0

    all_level_questions = [
        [
            Question(question='2 + 2 = ?', variants=['4', '6', '8'], answer=0, score=1),
            Question(question='2 * 2 = ?', variants=['4', '6', '8'], answer=0, score=2),
            Question(question='2 + 2 * 2 = ?', variants=['6', '8'], answer=0, score=3),
        ],
        [
            Question(question='12 + 12 = ?', variants=['24', '36', '48'], answer=0, score=1),
            Question(question='12 * 12 = ?', variants=['144', '124', '444'], answer=0, score=2),
            Question(question='12 + 12 * 2 = ?', variants=['36', '48'], answer=0, score=3),
        ],
    ]

    questions = all_level_questions[level - 1]

    for question_index in range(len(questions)):
        print(questions[question_index].question)
        for variant_index in range(len(questions[question_index].variants)):
            print(str(variant_index + 1) + ') ' +
                  questions[question_index].variants[variant_index])
        answer = int(input("What's your answer? "))
        if answer == questions[question_index].answer + 1:
            score += questions[question_index].score

    return score


if __name__ == '__main__':
    name = get_parameter_value('--name')
    age = int(get_parameter_value('--age'))
    level = int(get_parameter_value('--level'))

    score = do_testing(level)
    print(f'Congrats {name}, your score is {score} for level {level}')
