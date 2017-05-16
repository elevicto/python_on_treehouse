#Librairie de fonctions liées au système d'exploitation (utilisée ici pour vider l'écran)
import os
#Librairie de fonctions liées à Python (utilisée ici pour quitter l'application)
import sys
#Librairie de fonctions permettant de choisir un élément(mot, chiffre ou lettre) aléatoire dans une liste
import random

# WHAT WILL THIS APP DO:
# L'application est un "Mec Pendu"

list_of_words = []

# add new words to our list
def add_to_list(new_word):
        list_of_words.append(new_word)
        print("Added {}. List now has {} words.".format(new_word, len(list_of_words)))

# Create a list of x words with y caracters
def pick_up_words():
    num_words = int(input("How many words would you like enter? "))
    num_letters = int(input("To how much letters do you wan't to limit your words? "))
    print ("Enter {} words of maximum {} caracters".format(num_words, num_letters))
    while len(list_of_words) < num_words:
        new_word = input("> ").lower()
        try: 
            int(new_word)
        except ValueError:
            if len(new_word) > num_letters:
                print("{} exceeds {} caracters! Please try again.".format(new_word, num_letters))
            else:
                add_to_list(new_word)  
        else:
            print("{} is a number! Please enter only words".format(new_word))
    else:
        play(done)
        
#Fonction permettant de cleaner l'écran
def clear():
    #'nt' = système Windows. Les autres étant des systèmes APPLE ou Linux
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def num_guesses(secret_word):
    x = int(len(secret_word) * 2)
    return(x)
    
        
def draw(bad_guesses, good_guesses, secret_word):
    clear()
    
    print('Strikes: {}/{}'.format(len(bad_guesses), num_guesses(secret_word)))
    print('')
    
    for letter in bad_guesses:
        #le "end=' ', permet d'afficher le prochain print sur la même ligne séparé d'un espace
        print(letter, end=' ')
    #va à la ligne deux fois. Equivaut à faire 2x "enter"
    print('\n\n')
    
    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end='')
        else:
            print('_', end='')
            
    print('')


def get_guess(bad_guesses, good_guesses):
    while True:
        guess = input("Guess a letter: ").lower()
        
        #on vérifie que l'utilisateur n'a pas introduit plus d'une lettre
        if len(guess) != 1:
            print("You can only guess a single letter!")
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guess that letter!")
        # .isalpha() renvoie True ou False et permet de vérifier si on a introduit autre chose que des lettres. 
        elif not guess.isalpha():
            print("You can only guess letters!")
        else:
            return guess

        
def play(done):
    clear()
    secret_word = random.choice(list_of_words)
    #On crée des listes vides dans lesquelles on va enregistrer les lettres encodées par l'utilisateur
    bad_guesses = []
    good_guesses = []
    
    while True:
        #On va chercher la fonction draw qu'on a crée ci-dessus
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses, good_guesses)
        
        if guess in secret_word:
            good_guesses.append(guess)
            found = True
            for letter in secret_word:
                if letter not in good_guesses:
                    found = False
            if found:
                print("You win!")
                print("The secret word was {}".format(secret_word))
                done = True
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == num_guesses(secret_word):
                draw(bad_guesses, good_guesses, secret_word)
                print("You lost!")
                print("The secret word was {}".format(secret_word))
                done = True
            
        if done:
            play_again = input("Play again? Y/n ").lower()
            if play_again != 'n':
                return play(done = False)
            else:
                #Permet de quitter l'application
                sys.exit()


def welcome():
    start = input("Press enter/return to start or Q to quit ").lower()
    if start == 'q':
        print("Bye!")
        sys.exit()
    else:
        return True
                
print("Welcom to letter Guess!")

done = False

while True:
    clear()
    welcome()
    pick_up_words()
    
