#-*- coding:utf-8 -*-

import sys

if len(sys.argv) < 4:
    print 'please input: python make_sgm.py src_file ref_file system_file+ \n'
    sys.exit()

src_file = sys.argv[1]
ref_file = sys.argv[2]
system_file = sys.argv[3:]

#src_file
with open(src_file+'.sgm','w') as fp:
    fp.writelines('<srcset setid="set" srclang="source" trglang="target">\n')
    fp.writelines('<DOC docid="document">\n')
    
    for i,lines in enumerate(open(src_file)):
        lines = lines.strip()
        fp.writelines('<seg id="%s"> %s </seg>\n' % (i+1,lines))
        
    fp.writelines('</DOC>\n')    
    fp.writelines('</srcset>\n')
    
#ref_file
with open(ref_file+'.sgm','w') as fp:
    fp.writelines('﻿<refset setid="set" srclang="source" trglang="target">\n')
    fp.writelines('<DOC docid="document" sysid="ref1">\n')
    
    for i,lines in enumerate(open(ref_file)):
        lines = lines.strip()
        fp.writelines('<seg id="%s"> %s </seg>\n' % (i+1,lines))
        
    fp.writelines('</DOC>\n')    
    fp.writelines('</refset>\n')
    
#system_file
for file_name in system_file:
    with open(file_name+'.sgm','w') as fp:
        fp.writelines('<tstset setid="set" srclang="source" trglang="target">\n')
        fp.writelines('<DOC docid="document" sysid="%s">\n' % file_name)
        
        for i,lines in enumerate(open(file_name)):
            lines = lines.strip()
            fp.writelines('<seg id="%s"> %s </seg>\n' % (i+1,lines))
            
        fp.writelines('</DOC>\n')    
        fp.writelines('</tstset>\n')








