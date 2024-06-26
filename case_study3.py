"""
The `random_game()` function generates a random number between 1 and 15 (inclusive) and prompts the user to guess the number within 3 attempts. The function handles invalid inputs and provides feedback to the user on whether their guess is too high or too low. If the user guesses the number correctly, the function prints the number of attempts it took. If the user fails to guess the number within 3 attempts, the function asks the user if they want to try again.
"""
import random
from random import randint
#picking a random number
def random_game():
    print('The computer has picked a random number for you\n Hint: it is inbetween 1 and 15 (both inclusive)\n Can you guess it within three attempts?')
    number = random.randint(1,15)
    print(number)
    trial = True
    guesses = []
    while trial:
            
            
            
            try:
                    guess = int(input("Enter your answer: "))
                    
                    not_valid = True
            except ValueError:
                    print('it is a number try again')
                    trial = True
            guesses.append(guess)
            number_of_trials = len(guesses)
            if number_of_trials % 3 == 0:
                print('You could not complete in 3 Trials')
                try:
                    ans = input("Do you want to try again?\n (Yes/No): ")
                except ans.lower() == 'yes' or ans.lower() == 'no':
                    print('Pick an answer !!!')
                except Exception:
                    print('retry')
                try_ans = 'no'       
                if ans.lower == try_ans:
                    print('okay thanks for playing')
                    trial = False
                elif ans.lower() != try_ans :
                    trial = True
                    

            elif guess > number:
                print('It is high! Try again')
                continue
            elif guess < number:
                print ('It is low! Try again')
            elif guess == number:
                print('You are correct Nice job')
                
            
                print(f'You got in right in {number_of_trials} attempt(s)')
                trial = False
            
if __name__ == "__main__":
    random_game()

     