import random
import os
import ascii_images
import words

print(ascii_images.logo)


def get_random_word():
    x = random.choice(words.word_list)
    return x


chosen_word = get_random_word()


lives = 6


def display():
    y = []
    for i in range(0, len(chosen_word)):
        y += "_"
    return y


blank = display()

print(chosen_word)
print(f"{' '.join(blank)}")

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter : ").lower()
    os.system('clear')
    if guess in blank:
        print(f"You've already guessed {guess}.")

    for i in range(0, len(chosen_word)):
        if chosen_word[i] == guess:
            blank[i] = guess
    if guess not in chosen_word:
        print(f"You guessed {guess},that's not in the word.you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("YOU LOSE!")

    print(f"{' '.join(blank)}")

    if "_" not in blank:
        end_of_game = True
        print("YOU WIN!")

    print(ascii_images.stages[lives])
