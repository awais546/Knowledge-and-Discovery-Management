# # importing the library
# import nltk
# from nltk.corpus import wordnet
#
# nltk.download('wordnet')
# # lets use word paint as an exqmple
# syns = wordnet.synsets("paint")
#
# # An example of a synset:
# print(syns[0].name())
# print('\n')
# # Just the word:
# print(syns[0].lemmas()[0].name())
# print('\n')
#
# # Definition of that first synset:
# print(syns[0].definition())
# print('\n')
# # Examples of the word in use in sentences:
# print(syns[0].examples())
# print('\n')
#
# # synonyms and antonyms using wordnet using word
# synonyms = []
# antonyms = []
#
# for syn in wordnet.synsets("good"):
#     for l in syn.lemmas():
#         synonyms.append(l.name())
#         if l.antonyms():
#             antonyms.append(l.antonyms()[0].name())
# print('The synonyms of good are: ')
# print(set(synonyms))
# print('\n')
# print('The antonyms of good are: ')
# print(set(antonyms))
# print('\n')
#
#
#
# # comparison/ similarity score between 2 words
# w1 = wordnet.synset('ship.n.01')
# w2 = wordnet.synset('boat.n.01') # n denotes noun
# print("The similarity score betwee ship and boat is =",w1.wup_similarity(w2))


import spacy
import textacy
from nltk.corpus import wordnet as wn
def print_li (li):
    for each in li:
        print(each)
nlp = spacy.load('en')
# str1 = u'Startup companies create jobs and support innovation. Hilary supports entrepreneurship.'
str1 = u'A rare black squirrel has become a regular visitor to a suburban garden'
text = nlp(str1)

text_ext = textacy.extract.subject_verb_object_triples(text)

for el in text_ext:
    print('Triplets are: ',el)

word_input = input('Enter the word: ')
word_sys = wn.synsets(word_input)
print('Hyponyms of %s are\n')
print_li(word_sys[0].hyponyms())
print('Hypernyms of %s are\n')
print_li(word_sys[0].hypernyms())
print('Meronyms of %s are\n')
print_li(word_sys[0].part_meronyms())
print('Holonyms of %s are\n')
print_li(word_sys[0].part_holonyms())
print('Entailments of %s are\n')
print_li(word_sys[0].entailments())





