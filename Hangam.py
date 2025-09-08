import random

# Predefined list of words
words = ["apple", "banana", "grape", "orange", "mango"]

# Choose a random word
word = random.choice(words)
guessed_word = ["_"] * len(word)
guessed_letters = []
attempts = 6  # Limit incorrect guesses to 6

print(" Welcome to Hangman!")
print("Guess the word: ", " ".join(guessed_word))

# Main game loop
while attempts > 0 and "_" in guessed_word:
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}")

    print(" ".join(guessed_word))

# Game result
if "_" not in guessed_word:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("💀 Game Over! The word was:", word)
