#!/usr/bin/env python3
from subprocess import *
from pwn import sleep

BIN = './flag_debug'
# BIN = '/home/ctf3/flag_debug/flag_debug'

# Flag size
size = 19
for i in range(70):
    p = Popen([BIN, 'A' * i], stdout=PIPE)
    result = p.communicate()[0]
    if result.startswith(b'No luck'):
        size = i
        break
    # p.terminate()
    sleep(0.01)

# Print size with flush
print(size, flush=True)

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
        p = Popen([BIN, ''.join(try_flag)], stdout=PIPE)
        result = p.communicate()[0]
        if (result.startswith(b'Congratulations')):
            smallest_off_by_char = chr(current_char)
            break
        if (result.startswith(b'No')):
            off_by = int(result[30:].split(b'\n')[0])
            if off_by <= smallest_off_by:
                smallest_off_by = off_by
                smallest_off_by_char = chr(current_char)
        # p.terminate()
        sleep(0.01)
    flag[current_char_pos] = smallest_off_by_char

print(''.join(flag))
