import sys

from nytimes_words import words
from nytimes_solutions import solutions

import random
from collections import Counter as C

words.extend(solutions)

today = 242
answer = solutions[today]

# starting = random.choice(words)
starting = "crane"
tries = 1

final = ["_", "_", "_", "_", "_"]
bad = [[], [], [], [], []]
alphabet = "abcdefghijklmnopqrstuvwxyz"
remaining = list(alphabet)
confirmed = []
letter_list = dict.fromkeys(alphabet, -1) # -1 = unknown, 0 = gray, 1 = yellow, 2 = green

def update(guess):
    for i in range(5):
        if guess[i] in answer:
            if guess[i] == answer[i]:
                final[i] = guess[i]
                letter_list[guess[i]] = 2
            else:
                letter_list[guess[i]] = 1
                bad[i].append(guess[i])
        else:
            letter_list[guess[i]] = 0

    for l in letter_list:
        if letter_list[l] == 0:
            if l in remaining:
                remaining.remove(l)
        elif letter_list[l] == 1:
            confirmed.append(l)

def fits(word):
    for i in range(5):
        if final[i] not in ("_", word[i]):
            return False
        if word[i] in bad[i]:
            return False
        if word[i] not in remaining:
            return False
    for c in confirmed:
        if c not in word:
            return False
    return True

guess = starting
history = [guess]
for _ in range(5):
    update(guess)
    print(guess)

    ### function: Get Next Word
    words = [w for w in words if fits(w)]
    print([w for w in words if w in solutions])
    print(words)
    guess = random.choice(words)
    ### end function

    while guess in history:
        guess = random.choice(words)
    history.append(guess)
    tries += 1

    if guess == answer:
        print(guess)
        print(f"Wordle {today}: {tries}/6\n")
        sys.exit(0)

print(f"Wordle failed. Answer: {answer}")
