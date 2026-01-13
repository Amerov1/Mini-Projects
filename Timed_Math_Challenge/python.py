import random
import time
operations=["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12

TOTAL_PROBLEM=8

def generate_problem():
    operator=random.choice(operations)
    leftOperand=random.randint(MIN_OPERAND,MAX_OPERAND)
    rightOperand=random.randint(MIN_OPERAND,MAX_OPERAND)
    expre=str(leftOperand) + operator + str(rightOperand)
    guess=int(input(expre+ " ="))
    return guess, eval(expre)

def check(myguess,correct_answer):
    return int(myguess) != correct_answer
input("please press any key to start");
start_time= time.time()

for i in range(TOTAL_PROBLEM):
    myguess,answer= generate_problem()
    if check(myguess,answer):
        total_time= round(time.time()-start_time)
        print("you got a wrong answer... you scor is ",str(i),"/",str(TOTAL_PROBLEM)," in ",total_time, "seconds ")
        break
    if i == TOTAL_PROBLEM-1:
        total_time= round(time.time()-start_time)
        print("Great Work... you scor is ",str(TOTAL_PROBLEM),"/",str(TOTAL_PROBLEM)," in ",total_time, "seconds ")