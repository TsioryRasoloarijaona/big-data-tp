#!/usr/bin/python

import sys

max_cost = None
old_key = None



for line in sys.stdin:
    parts = line.rstrip("\n").split("\t")
    if len(parts) != 2:
        continue

    this_key, this_cost_raw = parts[0].strip(), parts[1].strip()
    if not this_key:
        continue

    try:
        this_cost = float(this_cost_raw)
    except ValueError:
        continue

    if old_key is not None and this_key != old_key:
        if max_cost is not None:
            print(f"{old_key}\t{max_cost}")
        max_cost = None

    old_key = this_key
    max_cost = this_cost if max_cost is None else max(max_cost, this_cost)

if old_key is not None and max_cost is not None:
    print(f"{old_key}\t{max_cost}")
