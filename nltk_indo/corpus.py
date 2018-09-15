# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 20:50:21 2018

@author: Teguh
"""
import nltk
import sys
def stopword_indo():
    value = []
    try:
        dokumen_teks = open('nltk_indo\stopwords.txt','r')
    except IOError:
        print ("file tidak ditemukan")
    
    for line in dokumen_teks:
        value.append(line.rstrip()) 
    
    return value

context= dict()
emit = dict()
transition = dict()

try:
    dokumen = open(r'tes.txt')
except IOError:
        print ("file tidak ditemukan")
for line in dokumen:
    print (line)
    previous = "<s>"
    if previous not in context:
        context[previous] = 0
    
    context[previous] += 1
    
    wordtags = line.split(" ")
    for wordtag in wordtags:
        word = wordtag.split("/")
        if previous+" "+word[0] not in transition:
            transition[previous+" "+word[0]] = 0
        transition[previous+" "+word[0]] += 1
        if word[1] not in context:
            context[word[1]] = 0
        context[word[1]] += 1
        previous = word[1]
        
    if previous+" "+"<s>" not in transition:
        transition[previous+" "+"<s>"] = 0
    transition[previous+" "+"<s>"] +=1
    
print (transition["nn biaya"]/context["nn"])
    

    
    


    


        
    
