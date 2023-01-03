import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize

stop_words=set(stopwords.words('english'))

txt="ammu is a ver good girl"\
    "she lives in calicut"\
    "she is very inteligent"\
    "she loves her parents."
tokenized=sent_tokenize(txt)
for i in tokenized:
    ws=nltk.word_tokenize(i)
    ws=[w for w in ws if w not in stop_words]
tagged=nltk.pos_tag(ws)
print(tagged)

from nltk.util import ngrams
a="ammu is a very good girl"
Ng=ngrams(sequence=nltk.word_tokenize(a),n=2)
for n in Ng:
    print(n)

import nltk
a="ammu is a very good girl"
b=nltk.word_tokenize(a)
print(b)
c=nltk.pos_tag(b)
print(c)
grammer="NP:{<DT>?<JJ>*<NN>}"
chunkedParser=nltk.RegexpParser(grammer)
chunked=chunkedParser.parse(c)
print(chunked)
chunked.draw()
