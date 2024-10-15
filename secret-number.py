import random  

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 20.")


secret_number = random.randint(1, 20)

for attempts in range(1, 6):
    
    guess = int(input("Take a guess: "))

    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        print(f"Good job! You guessed my number in {attempts} attempts.")
        break  

if guess != secret_number:
    print(f"Sorry, the number I was thinking of was {secret_number}.")


########################################################################################################

# import random  # Import the random module to generate a random number

# # Introduction message
# print("Welcome to the Guess the Number game!")
# print("I'm thinking of a number between 1 and 20.")

# # Generate a random number between 1 and 20
# secret_number = random.randint(1, 20)

# # Give the player 5 attempts to guess the number
# for attempts in range(1, 6):
#     # Ask the player for a guess
#     guess = int(input("Take a guess: "))

#     # Check if the guess is too low, too high, or correct
#     if guess < secret_number:
#         print("Your guess is too low.")
#     elif guess > secret_number:
#         print("Your guess is too high.")
#     else:
#         # If the guess is correct, congratulate the player and end the game
#         print(f"Good job! You guessed my number in {attempts} attempts.")
#         break  # Exit the loop since the player guessed correctly

# # If the player didn't guess the number, reveal the correct answer
# if guess != secret_number:
#     print(f"Sorry, the number I was thinking of was {secret_number}.")
