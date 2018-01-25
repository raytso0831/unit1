#Ray Tso
#1/22/18
#Analysis.py

sentence= input('Enter a sentence:')

space=sentence.count(' ')

print(' Number of words in your sentence:', space+1)

print('Number of characters in your sentence:',len(sentence))

print('Number of letters in your sentence:', len(sentence)-space)

search_of_char=input(' search for a character:')

print('Number of character in your sentence', sentence.count(search_of_char))

search_of_word=input(' search for a word:')

print('Number of word in your sentence', sentence.count(search_of_word))