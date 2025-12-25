import random
# Stages of Hangman to display
hangman_stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]  

lst = ['write','jump',"run","drink","dance","swim","speak"]
no_of_attempt = 0
fail_attempt = 0

word_to_guess = random.choice(lst) #Select any randon word from list
len_of_word_to_guess = len(word_to_guess)
guess = ['_'] * len_of_word_to_guess #Display no of dashes 
len_of_word = 0 

print("Initial Stage of Hangman") #print intital stage of hangman
print(hangman_stages[fail_attempt]) 

print("You have to guess words releted to verbs....")
print("Length of word to guess: ",len_of_word_to_guess)
print(" ".join(guess), sep="\n") 
while True :
    
    if fail_attempt == 6 : # If no of fail atemps is 6 declare as fail
        print("==== You Lose ====")
        print("Corect word is ",word_to_guess)
        break
    
    if len_of_word_to_guess == len_of_word : # If length of word match to the guessing word then player is won
        print("==== You Won ====") 
        break
        
    user_input = input("Enter letter: ").lower() # Take input form user
    
    for index, char in enumerate(word_to_guess):
            find = False
            if char == user_input:   # Check if character of word match to the guesing word character
                guess[index] = user_input
                len_of_word +=1
                find = True
                break
            else:
                find = False
                continue
    
    if find :        
        print("Correct guess:", " ".join(guess)) # If word find then print the guess word
                
    else :
        fail_attempt +=1 #if fail to guess the character then increment fail attempt by one 
        print(hangman_stages[fail_attempt]) # Print the updated Hangman
   
    no_of_attempt += 1 
    
