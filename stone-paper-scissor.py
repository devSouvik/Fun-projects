import random


def play():
    toss = int(input('How many times would you like to toss ? : '))
    user_points = 0
    machine_point = 0
    machine_list = ['stone', 'paper', 'scissor', 'scissor', 'paper', 'stone', 'stone', 'scissor', 'paper', 'stone',
                    'paper', 'scissor', 'paper', 'stone', 'scissor', 'stone', 'paper', 'scissor', 'paper',
                    'stone', 'scissor']

    machine_choice = random.choice(machine_list)

    for i in range(toss):
        userChoice = input('toss either stone or paper or scissor : ')
        if userChoice == machine_choice:
            print(f"Tie, lets try again...Human: {user_points} computer: {machine_point}")
        elif userChoice == 'scissor' and machine_choice == 'paper':
            machine_point += 1
            print(f"you are done with...human: {user_points}, computer: {machine_point}")
        elif userChoice == 'paper' and machine_choice == 'scissor':
            user_points += 1
            print(f"how dare you cut me off !?...human: {user_points} computer: {machine_point}")
        elif userChoice == 'stone' and machine_choice == 'scissor':
            user_points += 1
            print(f"ugh, I am totally blunt off !?...human: {user_points}, computer:  {machine_point}")
        elif userChoice == 'scissor' and machine_choice == 'stone':
            machine_point += 1
            print(f"took my revenge, haha !?...human: {user_points} computer:  {machine_point}")
        elif userChoice == 'paper' and machine_choice == 'stone':
            user_points += 1
            print(f"how dare you cover me, you mere human !!...human: {user_points}, computer: {machine_point}")
        elif userChoice == 'stone' and machine_choice == 'paper':
            machine_point += 1
            print(f"you are done with, completely covered!!...human: {user_points} computer: {machine_point}")

    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print(f"oye human 😏 !! you scored:  {user_points}\n")
    print(f"and I scored: {machine_point}")
    n = int(input('want to try again ?? press 1 ...want to end ? press 0....'))

    if n == 0:
        print('sayonara !!, have a nice day !! ')
        print('==========================================================')
    elif n == 1:
        print('==========================================================')
        play()
    else:
        print('Enter a valid input either 1 or 0: \n')
        print('==========================================================')


play()
