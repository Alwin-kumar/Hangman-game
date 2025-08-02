import random
from word import words_list
from Stages import stage
from art import logo


print(logo)



life = 6
word = random.choice(words_list)
word_len = len(word)
display = "_" * word_len
correct_letters = []
game_over = False


# Game loop
while not game_over:
    guess = input("Guess the letter from the word: ").lower()

    new_display = ""
    for i in range(word_len):
        if word[i] == guess:
            new_display += guess
            correct_letters.append(guess)
        elif word[i] in correct_letters:
            new_display += word[i]
        else:
            new_display += "_"

    display = new_display
    print(display)

    if guess not in word:
        life -= 1
        print(f"Wrong guess! you have {life}/6 to guess ")
        if life == 0:
            game_over = True
            print(r'''
__     ______  _    _   _      ____   _____ ______ 
\ \   / / __ \| |  | | | |    / __ \ / ____|  ____|
 \ \_/ / |  | | |  | | | |   | |  | | (___ | |__   
  \   /| |  | | |  | | | |   | |  | |\___ \|  __|  
   | | | |__| | |__| | | |___| |__| |____) | |____ 
   |_|  \____/ \____/  |______\____/|_____/|______|
                                                  
            💀 You ran out of lives. Game over!
            The correct word was: '{}'              
            Better luck next time!
'''.format(word))

    if "_" not in display:
        game_over = True
        print(r'''
__   __           __        _____       
\ \ / /__  _   _  \ \      / /_ _|_ __  
 \ V / _ \| | | |  \ \ /\ / / | || '_ \ 
  | | (_) | |_| |   \ V  V /  | || | | |
  |_|\___/ \__,_|    \_/\_/  |___|_| |_|

🎉 YOU WON! CONGRATS! 🎉
The word was: '{}'
'''.format(word))

    print(stage[life])
