# NLP_test
calculate the sentence similarity based on Words2Vec.
Description
===========
Words2Vec trasfrom words into Vectors. The Principle of words2Vec is elliptical here.
Based on Words2Vec. We can calculate the sentence(group by any word in the text) similarity.
The methods of sentence Vec:
  1. First, put each word into a Matrix, each row means the vectory of word. col means the length of Vectory
  2. Second, Do Dimensionality reduction of the Matrix by PCA. Define the first principal component as the vectory of this sentence.
  3. For two sentence, calculate the Cosine Angle and get the similarity.


Here is some examples:
  sentence 1 : Salsalate is a prodrug of salicylate
  sentence 2 : Salsalate is an inflammatory drug
  >>>CompareSentence(sentence1,sentence2)
  >>>111.72
  
  
  sentence1 : she is very sad
  sentence2 : she is bery happy
  >>>CompareSentecne(sentence1,sentence2)
  >>>24.49
  
  
  sentence1 : where was I Harry said
  sentence2 : Hermione had never been here
  >>>CompareSentence(sentence1,sentence2)
  >>>84.84
