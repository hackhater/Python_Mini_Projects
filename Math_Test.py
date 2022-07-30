
import random

ope = '+-x÷'
n = int(input('How many Math Questions do you want? \nyou:'))

def Random_Ope():
    return random.choice(ope)

answer_list = []
score = 0

def Math_Ope(n,n1,n2,o1):
    right_ans = 0
    user_ans = 0
    score = 0
    if o1 == '+':
        right_ans = num1 + num2
    elif o1 == '-':
        right_ans = num1 - num2
    elif ope1 == 'x':
        right_ans = num1 * num2
    else:
        right_ans = round(num1 / num2, 2)
    
    user_ans = round(float(input(f'{n+1}. What is {n1} {o1} {n2} equal to? \nyou:')),2)
    answer_list.append(f'{n+1}. {n1} {o1} {n2} = {right_ans} | you: {user_ans}')

    if user_ans == right_ans:
        print('Correct!')
        score += 1
    return score

for num in range(n):
    num1,num2 = random.randint(1,10),random.randint(1,10)
    ope1 = Random_Ope()
    score += Math_Ope(num,num1,num2,ope1)

print(f'Thanks for playing!\nYou got {score} out of {n} ({round(score/n, 1)*100}%) correct.')
for a in answer_list:
    print(a)