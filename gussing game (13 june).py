secret = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3

print("guess the word in three chances")

while guess != secret and guess_limit > guess_count:
    guess = input(f"enter a word: (life left {guess_limit}/3)")
    guess_limit -=1
    if guess == secret:
        print("you win!")
    elif guess != secret and guess_count < guess_limit:
        print("try again")
    else:
        print("you lose")