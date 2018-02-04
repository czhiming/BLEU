#!/bin/bash
set -x

#Bleu and NIST score
BleuScript="mteval-v13a.pl"
filedir="wmt15/backt"

#############################
src=$filedir/test.tok.es
ref=$filedir/test.tok.en
mt=$filedir/test.tok.en.backt
#############################

python make_sgm.py $src $ref $mt
################
src=$src.sgm
ref=$ref.sgm
mt=$mt.sgm
################
#BLEU and NIST
NewFileBLEUSys=${mt/sgm/bleu-sys.score}
NewFileNLEUDoc=${mt/sgm/bleu-doc.score}
NewFileBLEUSeg=${mt/sgm/bleu-seg.score}
NewFileNISTSys=${mt/sgm/nist-sys.score}
NewFileNISTDoc=${mt/sgm/nist-doc.score}
NewFileNISTSeg=${mt/sgm/nist-seg.score}	

perl ${BleuScript} -r $ref -s $src -t $mt -metricsMATR
mv "BLEU-sys.scr" ${NewFileBLEUSys}
mv "BLEU-doc.scr" ${NewFileNLEUDoc}
mv "BLEU-seg.scr" ${NewFileBLEUSeg}
mv "NIST-sys.scr" ${NewFileNISTSys}
mv "NIST-doc.scr" ${NewFileNISTDoc}
mv "NIST-seg.scr" ${NewFileNISTSeg}

python extract_bleu.py ${NewFileBLEUSeg}

rm -f ${NewFileBLEUSys} ${NewFileNLEUDoc} ${NewFileBLEUSeg} ${NewFileNISTSys} ${NewFileNISTDoc} ${NewFileNISTSeg}
rm -f $src $ref $mt




