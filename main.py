import random
import time

wait = 0

def check_number() :
    low = 1
    high = 100
    number = random.randint(low, high)
    guess_count = 0

    while True:
        try :
            guess = int(input("Guess the number between {} and {}: ".format(low, high)))
            if guess == number:
                print("Congratulations! You guessed the number! you got it in {} try!".format(guess_count))
                break
            elif guess < number:
                low = guess + 1
                guess_count+= 1
                print("The number is higher than your guess. Try again.\n")
            else:
                high = guess - 1
                guess_count+=1
                print("The number is lower than your guess. Try again.\n")
        except :
            print("Please put only the number!\n")
            

if __name__ == '__main__':
    while wait < 60 :
        if wait == 1 :
            print("Hello! welcome to a guess number program!")
        elif wait == 20 :
            print("You have to take a guess number between 1-100, by put your number")
        elif wait == 40 :
            print("I'll tell you that your number are higher or lower than the answer\n")
        wait+=1
        time.sleep(0.1)
    check_number()
        