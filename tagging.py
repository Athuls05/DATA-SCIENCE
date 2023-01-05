import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
stop_words=set(stopwords.words('english'))
txt="Welcome to amal jyothi college of engineering." \
    "college was established in two thousand." \
    "The college is under ktu." \
    "College was located in kottayam."\
    "Amal jyothi is very good for infrastructure ."\
    "The faculity members of amal jyothi is very good"\
    "The courses offered by amal jyothi college is IntMCA,MCA and various Btech programs"
tokens=nltk.sent_tokenize(txt)
for i in tokens:
    wordlist=nltk.word_tokens(i)
    wordlist=[w for w in wordlist is not w in stop_words]
    tagged=nltk.pos_tag(wordlist)
    print(tagged)