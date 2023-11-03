# Hangman
import random

# List of Words
words = ['abjure', 'future', 'picnic', 'agonistic', 'garland', 'protect', 'airline', 'gigantic', 'publish', 'bandit', 'goofy', 'quadrangle', 'banquet', 'government', 'recount', 'binoculars', 'grandnieces', 'redoubtable', 'biologist', 'handbook', 'reflection', 'blackboard', 'himself', 'reporter', 'board', 'indulge', 'ring', 'bookworm', 'inflatable', 'salesclerk', 'butterscotch', 'inimical', 'snapshot', 'camera', 'interim', 'shellfish', 'campus', 'invest', 'ship', 'catfish', 'jackpot', 'significance', 'carsick', 'kitchenette', 'sometimes', 'celebrate', 'law', 'sublime', 'celery', 'life', 'tabletop', 'citizen', 'lifeline', 'teamwork', 'coloring', 'love', 'tennis', 'compact', 'magnificent', 'timesaving', 'dark', 'malevolence', 'tree', 'damage', 'man', 'termination', 'dangerous', 'mascot', 'underestimate', 'decorum', 'marshmallow', 'vineyard', 'endorse', 'mine', 'war', 'engender', 'moonwalk', 'way', 'erratic', 'near', 'wealth', 'envelope', 'nephogram', 'wednesday', 'etymology', 'newborn', 'world', 'eyewitness', 'noisome', 'xerox', 'eulogy', 'owl', 'you', 'fish', 'parenthesis', 'zestful', 'food', 'perpetrator', 'foreclose', 'phone']

# Pick a random word
answer = random.choice(words)

print(answer) # Not needed but kept for testing

# Creates a variable to display letters as the user guesses
placeholder = "-" * len(answer)

print(placeholder) # Not needed but kept for testing

# Letting the user guess the entire word
guess = input("Guess the word: ").lower()

if guess == answer:
    print("Nice job")

else:
    print("Try again")

# Letting the user guess one letter
guess = input("Guess a letter: ").lower()

for i in range(len(answer)):
    if guess == answer[i]:
        placeholder = placeholder[:i] + guess + placeholder[i+1:]

print(placeholder)
