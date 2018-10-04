# -*- coding: utf-8 -*-
"""
Created on Fri May 12 21:15:38 2017

@author: han-luo
"""
from __future__ import division
import numpy as np
import cPickle
import re
import math
from sklearn.decomposition import PCA


#Get the wordsDic and wordsVec from the results of words2Vec

def GetPriorData(wordsDic,wordsVec):

    '''
    The input parameter(string):
    -------------------
    The wordsDic represent the file of variable(dictionary)in words2wec saved with cPickle
    The wordsVec represent the file of variable(final_embeddings)in words2wec saved with cPickle
        
    Return:
    -------------------
        wordsDictionary, wordsVector
    '''
    global wordsDictionary
    global wordsVector
    wordsDictionary = cPickle.load(open(wordsDic,'rb'))
    wordsVector = cPickle.load(open(wordsVec,'rb'))
    
    return wordsDictionary, wordsVector


#Get the vector of sentence    
def GetSentenceVector(sentence):
    
    '''
    The input parameter:
    --------------------
    The sentence string:
    Using the all words vector to create the sentence matrix (m,n)
    m represent the words number
    n represent the words vector length 
    Then:
    Using the PCA decomposition method to Get the principal component of the sentence
    principal component of the sentence is used to descrisbe the feature of sentence
    
    Return:
    --------------------
        Vector of principal component of the sentence
    '''
    sentencelst = sentence.split()    
    vector = []
    for word  in sentencelst:
        word=re.sub("[^a-zA-Z]+", " ",word).lower()
        vector.append(wordsVector[wordsDictionary[word]])
    vector = np.array(vector)
    
    pca = PCA(n_components = 1)
    pca.fit(vector)
    
    return pca.components_


#Compare the similarity between two different sentence    
def CompareSentence(sentence1,sentence2):
    
    '''
    The input parameter:
    -------------------
        The strings of two sentence
        compute the similarity of two sentence by compute the cosΘ.
    Return:
    -------------------
        The angle of two sentence.(x°)
    '''
    vec1 = GetSentenceVector(sentence1)[0]
    vec2 = GetSentenceVector(sentence2)[0]
    sumXY = 0
    sumXX = 0
    sumYY = 0
    for i in range(len(vec1)):
        sumXY += vec1[i] * vec2[i]      #sum(X*Y)
        sumXX += vec1[i]**2             #sum(X*X)
        sumYY += vec2[i]**2             #sum(Y*Y)
    result = round((sumXY / ((sumXX*sumYY))**0.5),2)
    angle = round((math.acos(result) / math.pi * 180),2)
#    print vec1
#    print vec2
#    print sumXX,
#    print sumYY
#    print sumXY
    return angle
    
