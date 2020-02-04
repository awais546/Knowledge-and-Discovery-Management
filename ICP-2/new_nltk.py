import nltk
import pdb
import spacy




data = ''
with open ("sample.txt", "r") as myfile:
    data=myfile.readlines()

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
for i in range(len(data)):
    data[i] = data[i].replace('\n','')

tokenize_list = []
tagged_list = []
entities_list = []
for each in data:
    tokens = nltk.word_tokenize(each)
    tagged = nltk.pos_tag(tokens)
    entities = nltk.chunk.ne_chunk(tagged)
    tokenize_list.append(tokens)
    tagged_list.append(tagged)
    entities_list.append(entities)


pdb.set_trace()