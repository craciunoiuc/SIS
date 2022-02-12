#!/usr/bin/env python3

# List of pairs of order and character
chars = []
order = []
flag = [0] * 49

# Parse characters from preparsed file
with open('input.txt', 'r') as f:
    step = 0
    for line in f:
        if step % 3 == 1:
            chars.append(line[-2])
        step += 1

# Parse order from preparsed file
with open('output_order.txt', 'r') as f:
    for line in f:
            order.append(int(line[5:]))

# Sort based on order
for i in range(len(order)):
    for j in range(len(order) - 1):
        if order[j] > order[j + 1]:
            order[j], order[j + 1] = order[j + 1], order[j]
            chars[j], chars[j + 1] = chars[j + 1], chars[j]

print("".join(chars))