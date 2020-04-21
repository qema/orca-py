#!/usr/bin/env python3

import orca

with open("testdata.txt", "r") as f:
    s = f.read()
print(orca.motif_counts("node", 4, s))
#help(helloworld);
