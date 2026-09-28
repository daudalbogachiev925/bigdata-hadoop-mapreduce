#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    parts = line.split()
    if len(parts) > 0:
        ip = parts[0]
        print(f"{ip}\t1")
