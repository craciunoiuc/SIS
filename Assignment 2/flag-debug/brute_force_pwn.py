#!/usr/bin/env python3
from pwn import *

BIN = './flag_debug'
# BIN = '/home/ctf3/flag_debug/flag_debug'

context.bits = 64
context.endian = 'little'
context.binary = BIN

# Flag size
size = 19
for i in range(70):
    p = process(executable=BIN, argv=[BIN, 'A' * i])
    result = p.recv()
    if result.startswith(b'No luck'):
        size = i
        break
    p.close()
    sleep(0.01)

flag = ['S', 'I', 'S', '_', 'C', 'T', 'F', '{']

for i in range(size - 9):
    flag.append('0')
flag.append('}')

# current_char_pos = 8
for current_char_pos in range(8, size - 1):
    smallest_off_by = 100000
    smallest_off_by_char = 'A'
    for current_char in range(33, 128):
        try_flag = flag[:]
        try_flag[current_char_pos] = chr(current_char)
        p = process(executable=BIN, argv=[BIN, ''.join(try_flag)])
        result = p.recv()
        if (result.startswith(b'Congratulations')):
            smallest_off_by_char = chr(current_char)
            break
        off_by = int(result[30:].split(b'\n')[0])
        if off_by <= smallest_off_by:
            smallest_off_by = off_by
            smallest_off_by_char = chr(current_char)
        p.close()
        sleep(0.01)
    flag[current_char_pos] = smallest_off_by_char

print(''.join(flag))
