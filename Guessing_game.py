# Wap which have ...
# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over

n=40
number_of_guesses=1
print("Max number of guesses are 9 ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<40:
        print("your guess is low.\n")
    elif guess_number>40:
        print("your guess is high.\n ")
    else:
        print("you won\n")
        print("No of attempt you took to win is:",number_of_guesses)
        break
    print("You're number of guess left is:",9-number_of_guesses)
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")
  
