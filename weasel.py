#!/usr/bin/env python3

# pylint:disable=invalid-name

import argparse
import random
import sys

VALID_CHARS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")

def main():
    parser = argparse.ArgumentParser(description="Richard Dawkin's Famous Weasel Program", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--offsprings', type=int, help='Total number of offsprings', default=100)
    parser.add_argument('--chance', type=float, help='Chance in percent that a mutation occurs in a copied character', default=5.0)
    parser.add_argument('--target', type=str, help='Target string (only use chars A-Z and space)', default="METHINKS IT IS LIKE A WEASEL")
    args = parser.parse_args()

    target_len = len(args.target)
    target = list(args.target.upper())
    check_target(target)
    chance = args.chance / 100.0

    # Initial random string. Think: the zeroth survivor...
    generation = 0
    the_survivor = [random.choice(VALID_CHARS) for _ in range(target_len)]

    # Clear out all offsprings.
    offsprings = [[None for _ in range(target_len)] for _ in range(args.offsprings)]

    # Until the survivor matches the target exactly.
    while match_score(target, the_survivor) < target_len:
        max_score = -1
        max_score_i = -1
        for i in range(args.offsprings):
            # Generate one offspring.
            spawn(the_survivor, offsprings[i], chance)
            # Find best-matching offspring
            the_score = match_score(target, offsprings[i])
            if the_score > max_score:
                max_score = the_score
                max_score_i = i
        # Store the new survivor.
        the_survivor = offsprings[max_score_i].copy()
        generation += 1
        print("Gen:%d score:%d/%d %s" % (generation, max_score, target_len, "".join(the_survivor)))

def spawn(survivor, offspring, chance):
    for i in range(len(offspring)):
        offspring[i] = survivor[i]
        experiment = random.random()
        if experiment <= chance:
            offspring[i] = random.choice(VALID_CHARS)

def match_score(target, offspring):
    score = 0
    for i in range(len(offspring)):
        score += target[i] == offspring[i]
    return score

def check_target(target):
    for c in target:
        if c not in VALID_CHARS:
            print("Invalid character '%c' encountered. Only use letters 'A' - 'Z'." % c)
            sys.exit(1)

if __name__ == "__main__":
    main()
