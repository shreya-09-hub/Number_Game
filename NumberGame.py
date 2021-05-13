#This is the guess the number game!
import random
print('Hello! What is your name?')
name=input()
print('Well!'+ name +',i am thinking of a number between 1 to 20')
#lets generate the secrets number
secretNumber = random.randint(1, 20)

#now we need to ask the user to enter the numbers for 6 times
for guesstaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low!')
    elif guess > secretNumber:
        print('Your guess is too high!')
    else: 
        break #this condition is for the correct guess
if guess == secretNumber:
    print('Congragulations!'+ name+' You guessed my number in '+ str(guesstaken) +' guesses.')
else:
    print('Nope! the number i was thinking of is '+ str(secretNumber))
   
