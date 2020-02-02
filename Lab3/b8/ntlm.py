#!/bin/python3

import sys
import passlib.hash

if len(sys.argv) < 2:
	exit(1)

pw = sys.argv[1]
print("LM Hash: "+passlib.hash.lmhash.hash(pw))
print("NT Hash: "+passlib.hash.nthash.hash(pw))
