import random

options = ['scissors', 'paper', 'rock']

computer_choice = random.choice(options)



user_choice = input('choose scissors paper or rock: ').lower()



while user_choice not in options:
    user_choice = input('choose scissors paper or rock: ').lower()

if user_choice == computer_choice:
    print('The computer chose ' +str(computer_choice) + ' and you chose ' +str(user_choice) +'\nThe game ended in a draw.')
elif user_choice == options[0] and computer_choice == options[1]:
    print('The computer chose ' +str(computer_choice) + ' and you chose ' +str(user_choice) +'\nYou won!')
elif user_choice == options[0] and computer_choice == options[2]:
    print('The computer chose ' +str(computer_choice) + ' and you chose ' +str(user_choice) + '\nThe computer won!')
elif user_choice == options[1] and computer_choice == options[0]:
    print('The computer chose ' +str(computer_choice) +' and you chose ' +str(user_choice) +'\nThe computer Won!')
elif user_choice == options[1] and computer_choice == options[2]:
    print('The computer chose ' +str(computer_choice) +' and you chose ' +str(user_choice) +'\nYou won!')
elif user_choice == options[2] and computer_choice == options[0]:
    print('The computer chose ' +str(computer_choice) +' and you chose ' +str(user_choice) +'\nYou won!')
elif user_choice == options[2] and computer_choice == options[1]:
    print('The computer chose ' +str(computer_choice) +' and you chose ' +str(user_choice) +'\nThe computer Won')


    







