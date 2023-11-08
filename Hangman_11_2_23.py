# Hangman
import random

# List of Words
words = ['abjure', 'future', 'picnic', 'agonistic', 'garland', 'protect', 'airline', 'gigantic', 'publish', 'bandit', 'goofy', 'quadrangle', 'banquet', 'government', 'recount', 'binoculars', 'grandnieces', 'redoubtable', 'biologist', 'handbook', 'reflection', 'blackboard', 'himself', 'reporter', 'board', 'indulge', 'ring', 'bookworm', 'inflatable', 'salesclerk', 'butterscotch', 'inimical', 'snapshot', 'camera', 'interim', 'shellfish', 'campus', 'invest', 'ship', 'catfish', 'jackpot', 'significance', 'carsick', 'kitchenette', 'sometimes', 'celebrate', 'law', 'sublime', 'celery', 'life', 'tabletop', 'citizen', 'lifeline', 'teamwork', 'coloring', 'love', 'tennis', 'compact', 'magnificent', 'timesaving', 'dark', 'malevolence', 'tree', 'damage', 'man', 'termination', 'dangerous', 'mascot', 'underestimate', 'decorum', 'marshmallow', 'vineyard', 'endorse', 'mine', 'war', 'engender', 'moonwalk', 'way', 'erratic', 'near', 'wealth', 'envelope', 'nephogram', 'wednesday', 'etymology', 'newborn', 'world', 'eyewitness', 'noisome', 'xerox', 'eulogy', 'owl', 'you', 'fish', 'parenthesis', 'zestful', 'food', 'perpetrator', 'foreclose', 'phone']

# Pick a random word
answer = random.choice(words)

# Creates a variable to display letters as the user guesses
placeholder = "-" * len(answer)

# Tries
tries = 0

guess = ""
while guess != answer and placeholder != answer:
    print(placeholder)
    guess = input("Guess: ").lower()

    if len(guess) == 1:
        for i in range(len(answer)):
            if guess == answer[i]:
                placeholder = placeholder[:i] + guess + placeholder[i+1:]

print(f"Nice job! The word was {answer}")
