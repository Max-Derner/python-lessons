

if __name__ == "__main__":
    SECRET_PHRASE = "I'm a great guesser"
    user_guess = None

    while user_guess != SECRET_PHRASE:
        print("\nGuess the secret phrase!")
        user_guess = input("Your guess: ")
        if user_guess != SECRET_PHRASE:
            print("\nOoops! You're a terrible guesser aren't you!?.")
            print("Maybe you can work on that for a while")
            if len(user_guess) < len(SECRET_PHRASE):
                print("Your guess is shorter than the secret phrase")
            elif len(user_guess) > len(SECRET_PHRASE):
                print("Your guess is longer than the secret phrase")
            else:
                print("While it is wrong, your phrase is the right length")
    print("Eyup! You got the guess right! Nice one!")
