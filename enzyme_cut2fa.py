#!/usr/bin/python3

import sys

file_ez = 'Enzyme_site_block_ApeKI.txt'
Outfile = open(file_ez+'.fa','w')
for line in open(file_ez):
        if line.strip() == '':
                continue
        cell = line.strip().split()
        strChr = cell[0]
        strL    = cell[1]
        try:
                strSeq  = cell[8]
        except :
                print(cell)
                continue
        if len(strSeq) > 200:
                print('>'+strChr+'_'+strL,file=Outfile)
                print(strSeq,file=Outfile)

