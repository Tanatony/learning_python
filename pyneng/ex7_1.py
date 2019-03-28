#!/usr/bin/env python3

with open('r1.txt') as src, open('r2.txt', 'w') as dest:
    for line in src:
        if line.startswith('service'):
            dest.write(line)
