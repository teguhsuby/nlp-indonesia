# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 19:59:44 2018

@author: Teguh
"""

def bigram(kata):
    n = 2
    kata = kata.split(' ')
    output = []
    for i in range(len(kata)-n+1):
        output.append(kata[i:i+n])
    return output

def trigram(kata):
    n = 3
    kata = kata.split(' ')
    output = []
    for i in range(len(kata)-n+1):
        output.append(kata[i:i+n])
    return output

def ngrams(kata,n):
    kata = kata.split(' ')
    output = []
    for i in range(len(kata)-n+1):
        output.append(kata[i:i+n])
    return output

print (ngrams("The cow jumps over the moon",4))