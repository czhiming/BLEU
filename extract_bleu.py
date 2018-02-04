#coding:utf8

import sys


hter_in = sys.argv[1]


with open(hter_in+'.bleu','w') as fp:
    for i,lines in enumerate(open(hter_in)):
        lines = lines.strip().split()
        hter = lines[4]
        fp.writelines(hter+'\n')
