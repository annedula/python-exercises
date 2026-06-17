def computegrade(score):
    if score < 0.0 or score > 1.0:
        grade = 'Bad score'
        print(grade)
    elif score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
    return grade

while True:
    try:
        score = float(input('Enter Score: '))
        grade = computegrade(score)

        print(grade)
    except:
        print('Bad score')