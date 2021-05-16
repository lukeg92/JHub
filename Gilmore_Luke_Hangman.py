import random #allows the script to choose random
word_list = open("word_list.txt") #opens the word_list.txt file and assigns it to the word_list variable
hangman_word = random.choice(word_list.read().split()) #a random word from the word_list will be assigned to the hangman_word variable. This will be different each time the script is executed.
word_list.close() #closes the word_list.txt file
#print(hangman_word) #Displays the hangman_word, used for testing the code. Remove # when testing code

word_to_be_guessed = []
correct_word = []

print("This game of hangman has been created by Luke Gilmore.")
print("You have 7 chances to guess the correct word.")
print("There are ",len(hangman_word)," letters in your word")

for letter in hangman_word:
    word_to_be_guessed.append('*') #replaces the letters in hangman_word with *
print(word_to_be_guessed) #print the word to be guessed, hashed out in *. For example, hello would start as *****
    
number_of_guesses = 1 #This is the starting point for guesses
while number_of_guesses < 8: #The code will loop until 7 guesses have been made
        
    letter_choice = input("Please enter your next guess: ").lower() #prompts the player to make a guess, changes the format to lowercase 
                
    if letter_choice.isalpha() == False: #If a letter isnt chosen, for example a number 6 or a special character %
        print("You need to choose a letter!") #Prompt the player to input a letter
            
    elif letter_choice in correct_word: #If a letter has already been chosen
        print("You tried that one already!") #Inform the player that they already tried that lettter
                    
    elif len(letter_choice) > 1: #If more than one letter, character, number is input
        print("You can only guess one letter at a time") #Inform the player to choose one letter per guess
            
        continue #Carry on
                
    else:
        correct_word.append(letter_choice) #Add the letter_choice to correct_word
        if letter_choice in hangman_word: #If the letter_choice is in the hangman_word
            print('You guessed a correct letter!') #Tell the player their guess was correct
            for letter in range(0,len(hangman_word)): #For the letter in the range of the length of the hangman_word
                if hangman_word[letter] == letter_choice: #If the letter_choice belongs to the hangman_word
                    word_to_be_guessed[letter] = letter_choice #Replace the * in word_to_be_guessed with the correctly guessed letter
            print(word_to_be_guessed) #Display the word, with the * replaced. For example, guessing l in hello would display **ll*
            if not "*" in word_to_be_guessed: #If there are no * left in word_to_be_guessed
                print("You guessed the correct word:",hangman_word) #Tell the player what their word is
                print("Contratulations you Win")
                
                break #End the game
                
        else:
            if not letter_choice in hangman_word: #If the letter_choice is not in the hangman word
                print("You guessed a wrong letter, you lose a life!") #Tell the player their guess was incorrect
                print(word_to_be_guessed) #Display the word_to_be_guessed, with replaced * if correct guesses have already been made 
                number_of_guesses += 1 #Add 1 to the number_of_guesses
                if number_of_guesses > 7: #If 7 incorrect guesses have been made
                    print("You have used all 7 of your guesses")
                    print("Game over")                        
                    print("your word was",hangman_word) #Tell the player what their word is
                    print("You lose")
                    
                    break    #End the game 
