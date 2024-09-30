from random import randint

separator_header = '-------------------------'

'''The Monty Hall Problem'''
print(separator_header + 'The Monty Hall Problem')


def random_door():
    return randint(1, 3)


trial_count = 10000

stay_wins = 0
switch_wins = 0

for i in range(0, trial_count):
    prize_door = random_door()
    selected_door = random_door()
    opened_door = list(d for d in range(1, 4) if d != selected_door and d != prize_door)[0]
    switch_door = list(d for d in range(1, 4) if d != selected_door and d != opened_door)[0]

    if selected_door == prize_door:
        stay_wins += 1

    if switch_door == prize_door:
        switch_wins += 1

stay_rate = float(stay_wins) / float(trial_count)
switch_rate = float(switch_wins) / float(trial_count)

print(f'Stay win: {stay_rate}\nSwitch win: {switch_rate}')

'''Probability Basics'''
print(separator_header + 'Probability Basics')

prob_of_head_coin = 1.0 / 2.0
prob_of_six_dice = 1.0 / 6.0

prob_coin_head_and_dice_six = prob_of_head_coin * prob_of_six_dice
print(prob_coin_head_and_dice_six)

'''Joint Probabilities'''
print(separator_header + 'Joint Probabilities')

# Declare possible outcomes for coin and dice
coin_outcomes = ['H', 'T']
dice_outcomes = [1, 2, 3, 4, 5, 6]

# Combine each outcome between coin and dice
all_combinations = [(c, d) for c in coin_outcomes for d in dice_outcomes]

# Find only outcomes for Heads and 6(only one outcome)
head_and_six = [t for t in all_combinations if t[0] == 'H' and t[1] == 6]

# 1/12 = 0.8(3)
print(
    f'{float(len(head_and_six))} / {float(len(all_combinations))} OR {float(len(head_and_six)) / float(len(all_combinations))}')
