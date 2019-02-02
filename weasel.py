#!/usr/bin/env python3

import random

TARGET_STR = "METHINKS IT IS LIKE A WEASEL"
CHARS_STR = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
TARGET = list(TARGET_STR)
CHARS = list(CHARS_STR)
TARGET_LEN = len(TARGET)

OFFSPRINGS_COUNT = 100
MUTATION_CHANCE = 5


def spawn(survivor, offspring):
    for i in range(len(offspring)):
        offspring[i] = survivor[i]
        experiment = random.randint(1, 100)
        if experiment <= MUTATION_CHANCE:
            offspring[i] = random.choice(CHARS)


def match_score(offspring):
    score = 0
    for i in range(len(offspring)):
        score += TARGET[i] == offspring[i]
    return score


if __name__ == "__main__":
    the_survivor = [random.choice(CHARS) for _ in range(TARGET_LEN)]
    offsprings = [[ ' ' for _ in range(TARGET_LEN)] for _ in range(OFFSPRINGS_COUNT)]
    generation = 0
    while match_score(the_survivor) < TARGET_LEN:
        max_score = -1
        max_score_i = -1
        for i in range(OFFSPRINGS_COUNT):
            spawn(the_survivor, offsprings[i])
            the_score = match_score(offsprings[i])
            if the_score > max_score:
                max_score = the_score
                max_score_i = i
        the_survivor = offsprings[max_score_i].copy()
        generation += 1
        print("Gen:%d score:%d %s" % (generation, max_score, "".join(the_survivor)))
