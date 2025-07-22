def computer_guess():
    low = 1
    high = 100
    attempts = 0
    print("Think of a number between 1 and 100.")
    print("The computer will try to guess it!")
    print("Enter:")
    print("  'h' if the guess is too high")
    print("  'l' if the guess is too low")
    print("  'c' if the guess is correct")

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"\nComputer guesses: {guess}")
        feedback = input("Is it (h/l/c)? ").lower()

        if feedback == 'c':
            print(f"\nYay! The computer guessed it in {attempts} tries!")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")

    if low > high:
        print("Hmm... Are you sure you gave the right feedback? 🤔")

# Run the game
computer_guess()