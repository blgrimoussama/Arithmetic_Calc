import re
import math

def check_format(input):
    pattern = "(x|-x|-[0-9]+x|[0-9]+x)+(\+y|-y|-[0-9]+y|\+[0-9]+y)=(-[0-9]|[0-9])"
    check_general_format = re.search(pattern, input)
    if not check_general_format:
        return False
    else:
        after_equal_sign = input[input.find('=')+1:]
        try:
            test_it = int(after_equal_sign)
        except ValueError:
            return False
        return True

def fct(a,b):
    # print((a, b))
    if b == 0:
        return 1,0
    else:
        u, v = fct(b, a % b)
        # print((u, v))
        return v, u - (a//b)*v

def solve(a,b,c):
    if b<0:
        pgcd = -int(math.gcd(a,b))
    else:
        pgcd = int(math.gcd(a,b))
    # rint(pgcd)
    if c % pgcd != 0:
        if b>0:
            return "l'equation {}x + {}y = {} n'admet aucune solution".format(a, b, c)
        else:
            return "l'equation {}x - {}y = {} n'admet aucune solution".format(a, str(b)[1:], c)
    else:
        a, b, c = a//pgcd, b//pgcd, c//pgcd
        # print((a,b,c))
    u, v = fct(a,b)
    # if c == 1:
    #     return "les solutions de l'equation {}x + {}y = {} sont: ({} + {}k, {} + {}k)".format(a*pgcd, b*pgcd, c*pgcd, u, b*pgcd, v, a*pgcd)
    # else:
    # if b*c>0:
    if b*pgcd>0:
        return "la solution particuliere de l'equation {}x + {}y = {} est : ({}, {})".format(a*pgcd, b*pgcd, c*pgcd, u*c, v*c)
    else:
        return "la solution particuliere de l'equation {}x - {}y = {} est : ({}, {})".format(a*pgcd, str(b*pgcd)[1:], c*pgcd, u*c, v*c)
    # else:
    #    return "la solution particuliere de l'equation {}x + {}y = {} est : ({}, {})".format(a*pgcd, b*pgcd, c*pgcd, u*c, v*c)
def process_input():
    equation = input("Entrer l'equation a resoudre (ax+by=c) : ")
    if check_format(equation):
        try:
            a = int(equation[:equation.find('x')])
        except:
            if equation[:equation.find('x')] == '-':
                a = -1
            else:
                a = 1
        if equation.find('y') == equation.find('+') + 1:
            b = 1
        elif equation.find('y') == equation.find('x') + 2:
            b = -1
        else:
            b = int(equation[equation.find('+')+1 or equation.find('x')+1:equation.find('y')])
        c = int(equation[equation.find('=')+1:])
        if a == 0 or b == 0 or c == 0:
            print('Error: Please Check your input values (must not be null)!')
            return 0
        print(solve(a, b, c))
        # print((a, b, c))
    else:
        print('Error: Please Check your input format (ax+by=c)!')
        process_input()
process_input()