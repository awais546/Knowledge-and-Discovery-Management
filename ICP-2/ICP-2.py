from stanfordcorenlp import StanfordCoreNLP
import pdb
import json

# Preset
host = 'http://localhost'
port = 9000
nlp = StanfordCoreNLP(host, port=port,timeout=30000)

# The sentence you want to parse
data = ''
with open ("sample.txt", "r") as myfile:
    data=myfile.readlines()

for i in range(len(data)):
    data[i] = data[i].replace('\n','')



sentence = data

for each in sentence:
    # POS
    try:
        annot_doc = nlp.annotate(each,properties={'annotators': 'sentiment','outputFormat': 'json','timeout': 1000,})
        annot_doc = json.loads(annot_doc)
        for sent in annot_doc["sentences"]:
            print(" ".join([word["word"] for word in sent["tokens"]]) + " => "+ str(sent["sentimentValue"]) + " = " + sent["sentiment"])
    except:
        pass

    # try:
    #     print('POS：', nlp.pos_tag(each))
    # except:
    #     pass
        # Tokenize
    # try:
    #     print('Tokenize：', nlp.word_tokenize(each))
    # except:
    #     pass

        # NER
    # try:
    #     print('NER：', nlp.ner(each))
    # except:
    #     pass
    # try:
    #     # Parser
    #     print('Parser：')
    #     print(nlp.parse(each))
    #     print(nlp.dependency_parse(each))
    # except:
    #     pass

    # Close Stanford Parser
nlp.close()