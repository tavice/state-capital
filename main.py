# We're going to create a game to help us memorize the names of the capitals of all 50 states.

# To play the game:

# Your program should prompt the user to identify the capital associated with a given state.
# There should be running tallies on the number of correct and incorrect answers for each state
# After getting through all 50 states one time, users should be asked whether or not they want to play again.

# Define the list of dictionaries with state names and capitals
states = [
    {'name': 'Alabama', 'capital': 'Montgomery', 'correct': 0, 'wrong': 0},
    {'name': 'Alaska', 'capital': 'Juneau', 'correct': 0, 'wrong': 0},
    {'name': 'Arizona', 'capital': 'Phoenix', 'correct': 0, 'wrong': 0},
    {'name': 'Arkansas', 'capital': 'Little Rock', 'correct': 0, 'wrong': 0},
    {'name': 'California', 'capital': 'Sacramento', 'correct': 0, 'wrong': 0},
    {'name': 'Colorado', 'capital': 'Denver', 'correct': 0, 'wrong': 0},
    {'name': 'Connecticut', 'capital': 'Hartford', 'correct': 0, 'wrong': 0},
    {'name': 'Delaware', 'capital': 'Dover', 'correct': 0, 'wrong': 0},
    {'name': 'Florida', 'capital': 'Tallahassee', 'correct': 0, 'wrong': 0},
    {'name': 'Georgia', 'capital': 'Atlanta', 'correct': 0, 'wrong': 0},
    {'name': 'Hawaii', 'capital': 'Honolulu', 'correct': 0, 'wrong': 0},
    {'name': 'Idaho', 'capital': 'Boise', 'correct': 0, 'wrong': 0},
    {'name': 'Illinois', 'capital': 'Springfield', 'correct': 0, 'wrong': 0},
    {'name': 'Indiana', 'capital': 'Indianapolis', 'correct': 0, 'wrong': 0},
    {'name': 'Iowa', 'capital': 'Des Moines', 'correct': 0, 'wrong': 0},
    {'name': 'Kansas', 'capital': 'Topeka', 'correct': 0, 'wrong': 0},
    {'name': 'Kentucky', 'capital': 'Frankfort', 'correct': 0, 'wrong': 0},
    {'name': 'Louisiana', 'capital': 'Baton Rouge', 'correct': 0, 'wrong': 0},
    {'name': 'Maine', 'capital': 'Augusta', 'correct': 0, 'wrong': 0},
    {'name': 'Maryland', 'capital': 'Annapolis', 'correct': 0, 'wrong': 0},
    {'name': 'Massachusetts', 'capital': 'Boston', 'correct': 0, 'wrong': 0},
    {'name': 'Michigan', 'capital': 'Lansing', 'correct': 0, 'wrong': 0},
    {'name': 'Minnesota', 'capital': 'St. Paul', 'correct': 0, 'wrong': 0},
    {'name': 'Mississippi', 'capital': 'Jackson', 'correct': 0, 'wrong': 0},
    {'name': 'Missouri', 'capital': 'Jefferson City', 'correct': 0, 'wrong': 0},
    {'name': 'Montana', 'capital': 'Helena', 'correct': 0, 'wrong': 0},
    {'name': 'Nebraska', 'capital': 'Lincoln', 'correct': 0, 'wrong': 0},
    {'name': 'Nevada', 'capital': 'Carson City', 'correct': 0, 'wrong': 0},
    {'name': 'New Hampshire', 'capital': 'Concord', 'correct': 0, 'wrong': 0},
    {'name': 'New Jersey', 'capital': 'Trenton', 'correct': 0, 'wrong': 0},
    {'name': 'New Mexico', 'capital': 'Santa Fe', 'correct': 0, 'wrong': 0},
    {'name': 'New York', 'capital': 'Albany', 'correct': 0, 'wrong': 0},
    {'name': 'North Carolina', 'capital': 'Raleigh', 'correct': 0, 'wrong': 0},
    {'name': 'North Dakota', 'capital': 'Bismarck', 'correct': 0, 'wrong': 0},
    {'name': 'Ohio', 'capital': 'Columbus', 'correct': 0, 'wrong': 0},
    {'name': 'Oklahoma', 'capital': 'Oklahoma City', 'correct': 0, 'wrong': 0},
    {'name': 'Oregon', 'capital': 'Salem', 'correct': 0, 'wrong': 0},
    {'name': 'Pennsylvania', 'capital': 'Harrisburg', 'correct': 0, 'wrong': 0},
    {'name': 'Rhode Island', 'capital': 'Providence', 'correct': 0, 'wrong': 0},
    {'name': 'South Carolina', 'capital': 'Columbia', 'correct': 0, 'wrong': 0},
    {'name': 'South Dakota', 'capital': 'Pierre', 'correct': 0, 'wrong': 0},
    {'name': 'Tennessee', 'capital': 'Nashville', 'correct': 0, 'wrong': 0},
    {'name': 'Texas', 'capital': 'Austin', 'correct': 0, 'wrong': 0},
    {'name': 'Utah', 'capital': 'Salt Lake City', 'correct': 0, 'wrong': 0},
    {'name': 'Vermont', 'capital': 'Montpelier', 'correct': 0, 'wrong': 0},
    {'name': 'Virginia', 'capital': 'Richmond', 'correct': 0, 'wrong': 0},
    {'name': 'Washington', 'capital': 'Olympia', 'correct': 0, 'wrong': 0},
    {'name': 'West Virginia', 'capital': 'Charleston', 'correct': 0, 'wrong': 0},
    {'name': 'Wisconsin', 'capital': 'Madison', 'correct': 0, 'wrong': 0},
    {'name': 'Wyoming', 'capital': 'Cheyenne', 'correct': 0, 'wrong': 0}
]


# To play the game:

# Your program should prompt the user to identify the capital associated with a given state.
# There should be running tallies on the number of correct and incorrect answers for each state
# After getting through all 50 states one time, users should be asked whether or not they want to play again.
# Game Requirements
# Make sure the states don't appear in alphabetical order in the prompts. This will make the game a bit more challenging for the user.

# Provide a welcome message to introduce the player to the game.

# Initialize new keys in the dictionaries that store the number of times a user gets a capital correct and the number of times the answer is wrong.

# Through all 50 states, prompt the user to name the capital of the state.

# If the answer is correct, display a message saying so, and increment the correct key.

# If the answer is wrong, display a message saying so, and increment the wrong key.

# After each prompt, display a message telling the reader how many times the state was answered correctly out of the total number of times answered.

# Once the user has gone through all 50 states, ask them if they'd like to play again.


def play_game():
    print("Welcome to the State Capitals Game!")
    print("You will be prompted to name the capital of each state. Let's begin!")
    print("")

    for state in states:
        print(f"Name the capital of {state['name']}: ")
        answer = input(">> ")
        if answer.lower() == state['capital'].lower():
            print("Correct!")
            state['correct'] += 1
        else:
            print("Incorrect!")
            state['wrong'] += 1
        print(f"You have answered correctly {state['correct']} times and incorrectly {state['wrong']} times.")
        print("")

    print("Would you like to play again? (y/n)")
    answer = input(">> ")
    if answer.lower() == 'y':
        play_game()
    else:
        print("Thanks for playing!")

play_game()