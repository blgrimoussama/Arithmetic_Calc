'''
This is a program that calculates the euclidian division of two integers a and b 
and displays all the steps of the calculation before stoping at remainder 1.'''


def euclide(a, b, show=False):  # raw_a=0, raw_b=0):
    steps_list = []
    a, b = max(a, b), min(a, b)
    steps_list.append('The euclidian division of {} over {} is :'.format(a, b))
    while(a % b != 0):
        k = (a - a % b) // b
        steps_list.append(str(a)+' = '+str(k)+' x '+str(b)+' + '+str(a % b))
        previous_a = a
        a = b
        b = previous_a % a
    if show == False:
        return f'It took {str(len(steps_list)-1)} steps to get the remainder 1.'
    else:
        return steps_list + [f'It took {str(len(steps_list)-1)} steps to get the remainder 1.']


def user_input():
    input_nums = input(
        'Enter the two integers or expressions seperated with a space e.g? 177 8 , 78 25**2 , 23 89*4-2 : ')
    # raw_a, raw_b = input_nums.split(' ')
    a, b = input_nums.split(' ')
    try:
        a, b = eval(a), eval(b)
    except NameError:
        return 'Check your input and Try again!'
    if not ('.' in str(a) or '.' in str(b)):
        show_input = input('Show the steps? (y/n) : ')
        show = False
        if show_input.lower() in ['y', 'yes']:
            show = True
        return True, a, b, show  # raw_a, raw_b
    else:
        return 'Check your numbers, they can\'t have decimals.'


input_state = user_input()


if type(input_state) == tuple:
    a, b, steps = list(input_state[1:4])
    if not steps:
        print(euclide(a, b))
    else:
        lines = euclide(a, b, steps)
        for line in lines:
            print(line)
else:
    print(input_state)
