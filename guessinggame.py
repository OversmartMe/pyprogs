secret_word = "Pink Floyd"
guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("what is my favorite band: ")
        guess_count +=1
    else:
         out_of_guesses = True

if out_of_guesses:
    print("you bloody snake, YOU LOSE!")
else:
    print("you are my true friend")