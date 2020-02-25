import pandas as pd
import math
import os
import pdb
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from pyspark.sql import SparkSession
from pyspark.ml.feature import NGram
from pyspark.ml.feature import Word2Vec

lemmatizer = WordNetLemmatizer()
spark = SparkSession.builder .appName("Ngram Example").getOrCreate()

def nltk2wn_tag(nltk_tag):
  if nltk_tag.startswith('N'):
    return wordnet.NOUN
  elif nltk_tag.startswith('R'):
    return wordnet.ADV
  elif nltk_tag.startswith('V'):
    return wordnet.VERB
  elif nltk_tag.startswith('J'):
    return wordnet.ADJ
  else:
    return None

def lemmatize_sentence(sentence):
  tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
  wn_tagged = map(lambda x: (x[0], nltk2wn_tag(x[1])), tagged)
  word_list = []
  for word, tag in wn_tagged:
    if tag is None:
      word_list.append(word)
    else:
      word_list.append(lemmatizer.lemmatize(word, tag))
  return " ".join(word_list)

def cal_tf(word_dict,file_sentence):
    tf_list = []
    for i in range(len(word_dict)):
        temp_tf = {}
        len_count = len(file_sentence[i])

        for word,val in word_dict[i].items():
            temp_tf[word] = val/float(len_count)
        tf_list.append(temp_tf)

    return tf_list

def calc_idf(word_dict_list):
    idf_dict = {}
    N = len(word_dict_list)
    idf_dict = dict.fromkeys(word_dict_list[0].keys(), 0)
    for word_dict in word_dict_list:
        for word, val in word_dict.items():
            if val > 0:
                idf_dict[word] += 1

    for word, val in idf_dict.items():
        idf_dict[word] = math.log10(N / float(val))

    return idf_dict

def cal_tf_idf(tf_list, idf_dict):
    tf_idf_list = []
    for each in tf_list:
        tf_idf = {}
        for word, val in each.items():
            tf_idf[word] = val * idf_dict[word]
        tf_idf_list.append(tf_idf)
    return tf_idf_list



file =os.listdir(os.getcwd()+'\\input');
temp1 = []
i = 0.0;
for each in file:
    with open(os.getcwd()+'\\input\\'+each) as f:
        data = f.readlines()[0].replace(".","").replace("'","").replace("(","").replace(")","");
        data = lemmatize_sentence(data)
        data = data.split(" ")
        temp1.append(data)
word_data_list = []

for i in range(len(temp1)):
    word_data_list.append((i+1,temp1[i]))

wordDataFrame = spark.createDataFrame(word_data_list, ["id", "words"])
ngram = NGram(n=2, inputCol="words", outputCol="ngrams")
ngramDataFrame = ngram.transform(wordDataFrame)

temp2 =ngramDataFrame.select("ngrams").collect()
temp = []
for i in range(5):
    temp.append(temp2[i][0])

temp_set = set([])
for each in temp:
    temp_set = temp_set.union(each)
wdict_list = []
for each in temp:
    wdict_temp = dict.fromkeys(temp_set,0)
    for word in each:
        wdict_temp[word] +=1
    wdict_list.append(wdict_temp)

tf_list = cal_tf(wdict_list,temp)
idf_dict =calc_idf(wdict_list)
tf_idf_list = cal_tf_idf(tf_list,idf_dict)

df_idf = pd.DataFrame(tf_idf_list)

max_series = df_idf.max()
max_words =max_series.to_dict()
li_keys = list(max_words.keys())
li_values = list(max_words.values())
final_dict = {}

for i in range(5):
    max_value = max(li_values)
    get_index = li_values.index(max_value)
    final_dict[li_keys[get_index]] = max_value
    del li_values[get_index]
    del li_keys[get_index]

li_temp = []
for each in temp:
    li_temp.append((each, ))

documentDF = spark.createDataFrame(li_temp, ["text"])

word2Vec = Word2Vec(vectorSize=3, minCount=0, inputCol="text", outputCol="result")
model = word2Vec.fit(documentDF)
result = model.transform(documentDF)

for row in result.collect():
    text, vector = row
    #printing the results
    print("Text: [%s] => \nVector: %s\n" % (", ".join(text), str(vector)))

# showing the synonyms and cosine similarity of the word in input data
for key in final_dict:
    print(key)
    synonyms = model.findSynonyms(key, 5)
    synonyms.show(5)

spark.stop()
pdb.set_trace()
