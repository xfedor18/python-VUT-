
def gen_quiz(qpool, *index, altcodes='ABCDEF', quiz=None):
    if not quiz:
        quiz = []
    for m in index:
        try:
            add = qpool[m]
        except IndexError as raised:
            print('Ignoring index ' + str(m) + ' - ' + str(raised))
        else:
            answers = []
            strings = [str(processing) for processing in altcodes]
            for answer in zip(strings, add[1]):
                string = answer[0] + ': ' + answer[1]
                answers.append(string)
            ad = (add[0], answers)
            quiz.append(ad)
    return quiz
