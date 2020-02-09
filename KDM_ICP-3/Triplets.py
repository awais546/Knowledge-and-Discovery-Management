import json
from stanfordcorenlp import StanfordCoreNLP
import pdb
# Preset
host = 'http://localhost'
port = 9000
nlp = StanfordCoreNLP(host, port=port,timeout=30000)


text = "My sister has a friend called John. Really, tell me more about him? She think he is so funny!"
print(nlp.coref(text))
#output ====> [[(1, 1, 2, 'My'), (2, 4, 5, 'me')], [(1, 1, 3, 'My sister'), (3, 1, 2, 'She')], [(1, 7, 8, 'John'), (2, 7, 8, 'him'), (3, 3, 4, 'he')]]

#nlp=StanfordCoreNLP("http://localhost:9000/")
s='Twenty percent electric motors are pulled from an assembly line'
s1='Brack Obama was born in Hawaii'
# s1 = 'Citing high fuel prices, United Airlines said Friday it has increased fares by $6 per round trip on flights to some cities also served by lower-cost carriers. American Airlines, a unit AMR, immediately matched the move, spokesman Tim Wagner said. United, a unit of UAL, said the increase took effect Thursday night and applies to most routes where it competes against discount carriers, such as Chicago to Dallas and Atlanta and Denver to San Francisco, Los Angeles and New York.'
s2 = 'Startup companies create jobs and support innovation. Hilary supports entrepreneurship.'
output = nlp.annotate(s1, properties={"annotators":"tokenize,ssplit,pos,depparse,natlog,openie",
                                "outputFormat": "json",
                                 "openie.triple.strict":"true",
                                 "openie.max_entailments_per_clause":"1"})

output2 = nlp.annotate(s2, properties={"annotators":"tokenize,ssplit,pos,depparse,natlog,openie",
                                "outputFormat": "json",
                                 "openie.triple.strict":"true",
                                 "openie.max_entailments_per_clause":"1"})
a = json.loads(output)
b = json.loads(output2)
print("The subject, object and verb/relation of the given sentence are")
print(a["sentences"][0]["openie"],'\n')
result = [a["sentences"][0]["openie"] for item in a]
result2 = [b["sentences"][0]["openie"] for item in b]
for i in result:
    for rel in i:
        relationSent=rel['relation'],rel['subject'],rel['object']
        print('The triplet of the given sentence is')
        print(relationSent)
for i in result2:
    for rel in i:
        relationSent=rel['relation'],rel['subject'],rel['object']
        print('The triplet of the given sentence is')
        print(relationSent)

