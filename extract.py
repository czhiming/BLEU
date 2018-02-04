#coding:utf8

import sys

file_name = sys.argv[1]


with open(file_name+'.best','w') as fp:
    for i,lines in enumerate(open(file_name)):
        lines = lines.strip()
        if i % 3 == 2:
            word_list = lines.split('|||')
            fp.writelines(word_list[1]+'\n')








