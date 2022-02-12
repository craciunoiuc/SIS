#!/usr/bin/env python3

blocks = []
flag = ['0'] * 35

with open('metadata', 'r') as f:
    for line in f:
        blocks.append(int(line[0:3]))
blocks[-1] = 1000

for i in range(0, 35):
    flag[i] = chr(int(blocks[i] / 8))

print("".join(flag))