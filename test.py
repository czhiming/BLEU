import re

'''
pattern = re.compile(r'IWSLT08_CT_CE.testset_[0-9]+\\[0-9]+\\(.*)')


with open('ref','w') as fp:
    for lines in open('ref.txt'):
        lines = lines.strip()
        content = pattern.findall(lines)[0]
        fp.writelines(content+'\n')
'''
for j in range(7):
    with open('ref_%s' % j,'w') as fp:
        for i,lines in enumerate(open('ref_7')):
            if i % 7 == j:
                fp.writelines(lines)
            





