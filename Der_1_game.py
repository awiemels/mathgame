# simple sympy
import sympy
import math
import random
from sympy.parsing.sympy_parser import parse_expr
from DER_Classes import Degree_2_gen, Degree_1_gen


x = sympy.symbols('x')
y = sympy.symbols('y')
z = sympy.symbols('z')

def DerANWSER(questionType):
    print("#################")
    print("Solve")
    expr = questionType
    # print(expr)
    print(sympy.latex(expr))
    # print(sympy.solvers.solve(expr))
    ANS = sympy.diff(expr, x)
    ANS_List = {ANS}
    User = input()
    List = {User}
    User_A = parse_expr(User)
    if User_A == ANS:
        print("correct")
    else:
        print("incorrect")
        print(ANS)
    print("---------------")
    print()

def InteANSWER(questionType):
    print("#################")
    print("Solve")
    expr = questionType
    # print(expr)
    print(sympy.latex(expr))
    # print(sympy.solvers.solve(expr))
    ANS = sympy.integrate(expr, x)
    ANS_List = {ANS}
    User = input()
    List = {User}
    User_A = parse_expr(User)
    if User_A == ANS:
        print("correct")
    else:
        print("incorrect")
        print(sympy.latex(ANS))
        print(ANS)
    print("---------------")
    print()

def ANSWER(questionType):
    print("#################")
    print("Solve")
    expr = questionType
    #print(expr)
    print(sympy.latex(expr))
    #print(sympy.solvers.solve(expr))
    ANS = sympy.solveset(expr)
    User = input()
    List = {User}
    if ANS == List:
        print("correct")
    else:
        print("incorrect")
        print(ANS)
    print("---------------")
    print()

def ANSWER2(questionType):
    print("#################")
    print("Solve")
    expr = questionType
    #print(expr)
    print(sympy.latex(expr))
    #print(sympy.solvers.solve(expr))
    ANS = sympy.solveset(expr)
    USER = str(input())
    USER2 = "-" + USER
    LIST = {USER2, USER}
    if ANS == LIST:
        print("correct")
    else:
        print("incorrect")
        print(ANS)
    print("---------------")
    print()
    
def MENUMODE(questionType):
    expr = questionType
    print(sympy.latex(expr))
    ANS = sympy.solveset(expr)
    print("choose option 1 to use basic math operations")
    print("choose option 2 to answer question")
    CO = int(input())
    if CO == 1:
        print("1 is add, 2 is subtract, 3 is add multiples of X, and 4 is subtract multiples of X and 5 and 6 are divide and multiply")
        CHOICE = int(input())
        if CHOICE == 1:
            n = ADD(expr)
            MENUMODE(n)
        elif CHOICE == 2:
            n = SUBTRACT(expr)
            MENUMODE(n)
        elif CHOICE == 3:
            n = ADDX(expr)
            MENUMODE(n)
        elif CHOICE == 4:
            n = SUBTRACTX(expr)
            MENUMODE(n)
        elif CHOICE == 5:
            n = Divide(expr)
            MENUMODE(n)
        elif CHOICE == 6:
            n = Multiply(expr)
            MENUMODE(n)
    if CO == 2:
        print("1 is to solve degree 1, 2 is degree 2, 3 is derivative solve and 4 is integration solve")
        C2 = int(input())
        if C2 == 1:
            ANSWER(expr)
        elif C2 == 2:
            ANSWER2(expr)
        elif C2 == 3:
            DerANWSER(expr)
        elif C2 == 4:
            InteANSWER(expr)



        
def ADD(expr):
    print("How much do you want to add")
    IN = int(input())
    Right = expr.rhs
    Left = expr.lhs
    OUT = sympy.Eq(Left+IN, Right+IN)
    return OUT
def ADDX(expr):
    print("How much do you want to add in multiples of x")
    IN = int(input())
    C = IN*x
    Right = expr.rhs
    Left = expr.lhs
    OUT = sympy.Eq(Left+C, Right+C)
    return OUT
def SUBTRACT(expr):
    print("How much do you want to subtract")
    IN = int(input())
    Right = expr.rhs
    Left = expr.lhs
    OUT = sympy.Eq(Left-IN, Right-IN)
    return OUT
def SUBTRACTX(expr):
    print("How much do you want to subtract in multiples of x")
    IN = int(input())
    C = IN*x
    Right = expr.rhs
    Left = expr.lhs
    OUT = sympy.Eq(Left-C, Right-C)
    return OUT
def Multiply(expr):
    print("How much do you want to multiply by")
    IN = int(input())
    Right = IN * expr.rhs
    Left = IN *expr.lhs
    OUT = sympy.Eq(Left, Right)
    return OUT
def Divide(expr):
    print("How much do you want to divide by")
    IN = int(input())
    Right = expr.rhs/IN
    Left = expr.lhs/IN
    OUT = sympy.Eq(Left, Right)
    return OUT

def GenQuestion():
    print("type in 0 for first option and 1 for second")
    print("degree 1 or 2 question or derivative is 2 or 3 is integration")
    d = int(input("Choose an option"))
    if d == 0:
        print("simplified or unsimplified")
        f2 = int(input("Choose an option"))
        print("Low or High numbered")
        f3 = int(input("Choose an option"))
        print("Any or Whole answer")
        f4 = int(input("Choose an option"))
        if f2 == 0 and f3 == 0 and f4 == 0:
            x = 1
        elif f2 == 0 and f3 == 0 and f4 == 1:
            x = 3
        elif f2 == 0 and f3 == 1 and f4 == 1:
            x = 4
        elif f2 == 1 and f3 == 0 and f4 == 1:
            x = 7
        elif f2 == 1 and f3 == 1 and f4 == 1:
            x = 8
        elif f2 == 0 and f3 == 1 and f4 == 0:
            x = 2
        elif f2 == 1 and f3 == 0 and f4 == 0:
            x = 5
        elif f2 == 1 and f3 == 1 and f4 == 0:
            x = 6
    elif d == 1:
        print("simplified or unsimplified")
        d2 = int(input("Choose an option"))
        if d2 == 0:
            x = 9
        elif d2 == 1:
            x = 10
    elif d == 2:
        print("degree 1 or 2")
        DER_Q = int(input("Choose an option"))
        if DER_Q == 0:
            x = 11
        elif DER_Q == 1:
            x = 12
    elif d == 3:
        print("degree 1 or 2")
        INTE_Q = int(input("Choose an option"))
        if INTE_Q == 0:
            x = 13
        elif INTE_Q == 1:
            x = 14

    return x
def main(n):
    test = Degree_1_gen()
    test2 = Degree_2_gen()

    flag = GenQuestion()
    if flag == 0:
        print("NO QUESTION")
    if flag == 1:
        for i in range(n):
            MENUMODE(test.Low_Any_Eq())
    elif flag == 2:
        for i in range(n):
            MENUMODE(test.High_Any_Eq())
    elif flag == 3:
        for i in range(n):
            MENUMODE(test.Low_Whole_Eq())
    elif flag == 4:
        for i in range(n):
            MENUMODE(test.High_Whole_Eq())
    elif flag == 5:
        for i in range(n):
            MENUMODE(test.Unsimplfied_LOW_ANY())
    elif flag == 6:
        for i in range(n):
            MENUMODE(test.Unsimplfied_HIGH_ANY())
    elif flag == 7:
        for i in range(n):
            MENUMODE(test.Unsimplified_Low_whole())
    elif flag == 8:
        for i in range(n):
            MENUMODE(test.Unsimplified_High_whole())
    elif flag == 9:
        for i in range(n):
            MENUMODE(test2.Simple_DEGREE2())
    elif flag == 10:
        for i in range(n):
            MENUMODE(test2.UNSimple_DEGREE2())
    elif flag == 11:
        for i in range(n):
            MENUMODE(test.Derivative_LOW_ANY())
    elif flag == 12:
        for i in range(n):
            MENUMODE(test2.Derivative_2nd())
    elif flag == 13:
        for i in range(n):
            MENUMODE(test.Derivative_LOW_ANY())
    elif flag == 14:
        for i in range(n):
            MENUMODE(test2.Derivative_2nd())

def maintest():
    i = 0
    while i == 0:
        print("welcome to math game, click on an option")
        print("Would you like to take a quiz press 1")
        print("Would you like to try a specific number of question press 2")
        print("Would you like to leave the program press 3")
        MENU_CHOICE = int(input())
        if MENU_CHOICE == 1:
            main(5)
        elif MENU_CHOICE == 2:
            print("choose number of questions")
            CHOICE = int(input())
            if CHOICE < 1:
                print("invalid input")
            else:
                main(CHOICE)
        elif MENU_CHOICE == 3:
            print("exiting program")
            i = 1

    
maintest()

# second degree questions
#--factoring problem
#
# negative solutions for last few problem types
# check for a better input answer system for integration, derivatives and second degree solvings
# Make classes for things--look at dr bible github for examples
# videos -Pygame Tutorial #5 - Projectiles and Introduction to For Loops in Python (Python Tutorial #5)
# pygame_functions: Text Outputs and Inputs
# Implement picking questions for menumode and make everything go back to Menumode
# turn main and genquestion into one function
# learn more about git



