#!/usr/bin/env python

import os
import seq_utils2
import sys

def count_all_seqs(input_dir):
        files = sorted(os.listdir(input_dir))
        os.chdir(input_dir)
	for file in files:
		filename = open(file)
        	seq_count = seq_utils2.count_seqs(filename)
        	print file, "has", seq_count

if len(sys.argv) != 2:
        #print stderr >> "Usage: sys.argv[0] path to directory"
        sys.exit("Usage: sys.argv[1] path to directory")

count_all_seqs(sys.argv[1])
