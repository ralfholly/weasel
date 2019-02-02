#!/usr/bin/env python3

# pylint:disable=invalid-name

import argparse
import random

CHARS_STR = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
CHARS = list(CHARS_STR)


def spawn(survivor, offspring, chance):
    for i in range(len(offspring)):
        offspring[i] = survivor[i]
        experiment = random.random()
        if experiment <= chance:
            offspring[i] = random.choice(CHARS)


def match_score(target, offspring):
    score = 0
    for i in range(len(offspring)):
        score += target[i] == offspring[i]
    return score


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Richard Dawkin's Famous Weasel Program", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--offsprings', type=int, help='Total number of offsprings', default=100)
    parser.add_argument('--chance', type=float, help='Chance in percent that a mutation occurs in a copied character', default=5.0)
    parser.add_argument('--target', type=str, help='Target string (only use chars A-Z and space)', default="METHINKS IT IS LIKE A WEASEL")
    args = parser.parse_args()

    target_len = len(args.target)
    target = list(args.target.upper())

    the_survivor = [random.choice(CHARS) for _ in range(target_len)]
    offsprings = [[' ' for _ in range(target_len)] for _ in range(args.offsprings)]
    generation = 0
    chance = args.chance / 100.0
    while match_score(target, the_survivor) < target_len:
        max_score = -1
        max_score_i = -1
        for i in range(args.offsprings):
            spawn(the_survivor, offsprings[i], chance)
            the_score = match_score(target, offsprings[i])
            if the_score > max_score:
                max_score = the_score
                max_score_i = i
        the_survivor = offsprings[max_score_i].copy()
        generation += 1
        print("Gen:%d score:%d/%d %s" % (generation, max_score, target_len, "".join(the_survivor)))
