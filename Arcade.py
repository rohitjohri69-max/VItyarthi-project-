import random
import pyjokes
def rps():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    print("Welcome to Rock, Paper, Scissors! (Type 'quit' to stop playing)\n")
    while True:
        user_choice = input("Enter Rock, Paper, or Scissors: ").strip().lower()
        if user_choice == "quit":
            print("\nFinal Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break
        if user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.\n")
            continue
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "paper" and computer_choice == "rock")
            or (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        print(f"Score -> You: {user_score} | Computer: {computer_score}\n")


def toss():
    options = ["head", "tail"]
    user_score = 0
    computer_score = 0
    print("Welcome to the Coin Toss Game! (Type 'quit' to exit)\n") 
    while True:
        call = input("Call Head or Tail: ").strip().lower()
        if call == "quit":
            print("\nFinal Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break
        if call not in options:
            print("Invalid call. Please enter 'head' or 'tail'.\n")
            continue
        result = random.choice(options)
        print(f"\nThe coin flips and lands on... {result.upper()}!")
        if call == result:
            print("You called it right! You win this round.")
            user_score += 1
        else:
            print("Wrong call! The computer takes this round.")
            computer_score += 1 
        print(f"Score -> You: {user_score} | Computer: {computer_score}\n")


def bulls_cows():
    def generate_secret_number():
        digits = [str(i) for i in range(10)]
        return "".join(random.sample(digits, 4))
    def calculate_bulls_and_cows(secret, guess):
        bulls = 0
        cows = 0
        for i in range(4):
            if guess[i] == secret[i]:
                bulls += 1
            elif guess[i] in secret:
                cows += 1
        return bulls, cows
    secret_number = generate_secret_number()
    attempts = 0
    print("Welcome to Bulls and Cows!")
    print("Rules:")
    print("- Guess the secret 4-digit number (digits are all unique).")
    print("- Bull: Correct digit in the correct position.")
    print("- Cow: Correct digit in the wrong position.")
    print("Type 'quit' to give up.\n")
    while True:
        guess = input("Enter your 4-digit guess: ").strip()
        if guess.lower() == "quit":
            print(f"You gave up! The secret number was {secret_number}.")
            break
        if not (guess.isdigit() and len(guess) == 4 and len(set(guess)) == 4):
            print("Invalid guess! Enter exactly 4 unique digits.\n")
            continue
        attempts += 1
        bulls, cows = calculate_bulls_and_cows(secret_number, guess)
        if bulls == 4:
            print(f"\nCongratulations! You found the number {secret_number} in {attempts} attempts!")
            break
        else:
            print(f"{bulls} Bull(s), {cows} Cow(s)\n")


def joke():
    joke = pyjokes.get_joke()
    print("Here is your joke:")
    print(joke)

def main_menu():
    while True:
        print("\n================ MAIN MENU ================")
        print("1. Rock, Paper, Scissors")
        print("2. Coin Toss")
        print("3. Bulls and Cows")
        print("4. Tell a Joke")
        print("5. Exit")
        print("===========================================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            rps()
        elif choice == "2":
            toss()
        elif choice == "3":
            bulls_cows()
        elif choice == "4":
            joke()
        elif choice == "5":
            print("\nGoodbye! Thanks for using the program.")
            break
        else:
            print("Invalid selection! Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main_menu()