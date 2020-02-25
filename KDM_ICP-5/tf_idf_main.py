import pandas as pd
import os
import pdb
import math

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
temp = []
i = 0.0;
for each in file:
    with open(os.getcwd()+'\\input\\'+each) as f:
        temp.append(f.readlines()[0].replace(".","").replace("'","").replace("(","").replace(")","").split(" "));

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
pdb.set_trace()
