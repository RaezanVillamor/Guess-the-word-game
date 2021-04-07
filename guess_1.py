#Python guessing game
import random
import string

lower_case_alphabet = (string.ascii_letters).lower()
random_letter = random.choice(lower_case_alphabet)
print(random_letter)
count = 0
userInput = ''
guesses = []
ASCII = []
def main():
    
    #display instructions
    instructions()
    getInput()
    stats()
    worstLetter()

def instructions():
    filename = 'instructions.txt'
    mode = 'r'
    file = open(filename, mode)
    instructions = file.read()
    print (instructions)

def getInput():
    global userInput #Set user input to nothing atm GLOBAL INPUT MAKES IT SE THAT WE CAN CHANGE THE GLOBAL VARIABLE
    global count #get global count so we can increment the count variable stated in the beginning
    global guesses
    while random_letter != userInput:
        userInput = input("take a guess:") #get user input and use loop to see if userInput = the random letter or not
        if userInput.isalpha() == False:
            print("not a letter")
            count = count +1
        elif userInput < random_letter:
            print("too low")
            guesses.append(userInput)
            count = count +1
        elif   userInput > random_letter:
            print("Too high")  
            guesses.append(userInput)
            count = count +1
        else:
            print('Good job, you guessed the correct letter!')
            count = count +1
            print(userInput)
    
    
            
def stats(): 
    
    #This part will like run the stats page where it gives u the level of where ur at
    print('--MY STATS--')
    print('Number of guesses', count)
    if count >= 5 and count <= 10:
        print("Level Intermediate")
    elif count <5:
        print("Level Expert")
    else:
        print("Level Beginner")
    

#worst letter guess


def worstLetter():
    global guesses
    global random
    distance = []
    
 

        #asciiNumbersDifference.append(difference)
        #print (Worst letter)
        
main()