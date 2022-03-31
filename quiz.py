# Creates new game
def new_game():
    guesses = []
    correct_guesses = 0
    question_number = 1

    for key in questions:
        print("______________")
        print(key)
        for option in options[question_number-1]:
            print(option)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)
        print(guesses)
        correct_guesses += check_answer(questions.get(key), guess)
        question_number += 1

    display_score(correct_guesses, guesses)


# Check answer
def check_answer(answer, guess):
    if answer == guess:
        print("You are correct!")
        return 1
    else:
        print("You are wrong")
        return 0


# Display Score
def display_score(correct_guesses, guesses):
    print("__________________")
    print("RESULTS: ")
    print("Answers: ", end="")
    for value in questions:
        print(questions.get(value), end=" ")
    print()
    print("__________________")
    print("Guesses: ")
    for value in guesses:
        print(value, end=" ")
    print()

    score = int((correct_guesses/len(questions)) * 100)
    print("Your score is: {}%.".format(score))


# Play game again
def play_again():
    response = input("Do you want to play again? (yes/no): ").upper()

    if response == 'YES':
        return True
    else:
        return False


# Key: value pairs dictionary
questions = {
    "Who created Python?": "A",
    "What year was Python Created? ": "B",
    "Python is tributed to which comedy group? ": "C",
    "Is the Earth Round? ": "A"
}

# List of lists
options = [
    ["A. Guido Van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zukerburg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. Sometimes", "D. What's Earth? "]
]

# Creates a new game
new_game()

while play_again():
    new_game()

print("You have left the game. ")
