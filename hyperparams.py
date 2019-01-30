# -*- coding: utf-8 -*-

class Hyperparams:
    '''Hyperparameters'''
    # data
    source_train = 'data/train/in.txt'
    target_train = 'data/train/out.txt'
    source_test = 'data/test/in.txt'
    target_test = 'data/test/out.txt'
    vocab = 'data/vocab'
    
    # training
    batch_size = 128 
    lr = 0.0001 # learning rate. 
    logdir = 'logdir'
    
    # model
    maxlen = 30 # max length for a sentence
    min_cnt = 0 # frequency threshold for vocabulary
    hidden_units = 512
    num_blocks = 6 # number of encoder/decoder blocks
    num_epochs = 20
    num_heads = 8
    dropout_rate = 0.1
    sinusoid = False # If True, use sinusoid position embedding. If false, positional embedding.
    
    
    
    
