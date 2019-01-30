# -*- coding: utf-8 -*-

from hyperparams import Hyperparams as hp
import tensorflow as tf
import numpy as np
from collections import Counter
import os

def make_vocab(fpaths, out):
    '''Constructs vocabulary.
    
    Args:
      fpath: A string. Input file path.
      fname: A string. Output file name.
    
    Writes vocabulary line by line to `preprocessed/fname`
    '''  
    char2cnt = Counter()
    for path in fpaths:
        for line in open(path, 'r'):
            line = line.strip()
            if not line: # detect the empty line
                continue
            chars = line.split()
            char2cnt.update(chars)
    with open(out, 'w') as fout:
        fout.write("{}\t1000000000\n{}\t1000000000\n{}\t1000000000\n{}\t1000000000\n".format("<PAD>", "<UNK>", "<S>", "</S>"))
        for word, cnt in char2cnt.most_common(len(char2cnt)):
            fout.write(u"{}\t{}\n".format(word, cnt))
        print("%d chars written!" % (len(char2cnt)))

if __name__ == '__main__':
    make_vocab([hp.source_train, hp.target_train], hp.vocab)
    print("Done")