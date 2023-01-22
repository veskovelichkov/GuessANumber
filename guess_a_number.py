import random
computer_choice=random.randint(1,100)
while True:
    player_choice=int(input('Guess the number (1-100): '))
    if type(player_choice)!=int or player_choice<1 or player_choice>100:
        print('Invalid input. Try again...')
        continue
    if player_choice==computer_choice:
        print('You guessed the number!')
        break
    elif player_choice<computer_choice:
        print('Too low!')
    else:
        print('Too high!')