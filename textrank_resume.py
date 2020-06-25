import kss
import pandas as pd
import re
import torch
from PyKomoran import *

komoran = Komoran("EXP")
full_resume1 = list()

data = pd.read_csv("Data/resume_raw_data.csv", encoding='utf-8')
count1 = data["RESUME1"].size

full_resume1 = list()
sents =list()

for i in range(3000):
    for sent in kss.split_sentences(data["RESUME1"][i]):
        full_resume1.append(sent.replace('&quot;','"').replace('&#160;',""))
        #print(komoran.get_plain_text(sent))
        sent = komoran.get_plain_text(sent)
        sents.append(sent)
        
        
from textrank import KeywordSummarizer

def komoran_tokenize(sent):
    words = sent.split()
    words = [w for w in words if ('/NNG' in w )]
    return words

keyword_extractor = KeywordSummarizer(
    tokenize = komoran_tokenize,
    window = -1,
    verbose = False
)
keywords = keyword_extractor.summarize(sents, topk=30)
for word, rank in keywords:
    print('{} ({:.3})'.format(word, rank))