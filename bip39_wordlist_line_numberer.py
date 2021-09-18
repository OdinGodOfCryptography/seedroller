#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input_file = "english_bip39.txt"
output_file = "english_bip39_numbered.txt"


infile = open(input_file)
outfile = open(output_file, "w")

words = infile.readlines()

for i in range(0, len(words)):
    print(words[i])
    outfile.write( str(i+1) + "\t" + words[i])

outfile.close()