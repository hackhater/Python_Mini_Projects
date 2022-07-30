
import random

ope = '+-x÷'
# user's input for number of question
no_question = int(input('How many Math Questions do you want? \nyou:'))

# function for Randomizing math operators
def Random_Ope():
    return random.choice(ope)
# list and score for final result
answer_list = []
score = 0
# function for Math Operations, Score counting and answer_list appending
def Math_Operation(n,n1,n2,o1):
    right_ans = 0
    user_ans = 0
    score = 0
    # Math Operation conditions
    if o1 == '+':
        right_ans = num1 + num2
    elif o1 == '-':
        right_ans = num1 - num2
    elif ope1 == 'x':
        right_ans = num1 * num2
    else:
        right_ans = round(num1 / num2, 2)
    # User's input for math answer
    user_ans = round(float(input(f'{n+1}. What is {n1} {o1} {n2} equal to? \nyou:')),2)
    # Math questions and answers appending
    answer_list.append(f'{n+1}. {n1} {o1} {n2} = {right_ans} | you: {user_ans}')
    # Score counting
    if user_ans == right_ans:
        print('Correct!')
        score += 1
    # return score
    return score

# Actually, program excuation starts here
# looping for the number of questions
for no in range(no_question):
    num1,num2 = random.randint(1,10),random.randint(1,10)
    ope1 = Random_Ope()
    score += Math_Operation(no,num1,num2,ope1)
# Final result output
print(f'Thanks for playing!\nYou got {score} out of {no_question} ({round(score/no_question, 1)*100}%) correct!')
for a in answer_list:
    print(a)