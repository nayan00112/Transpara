import numpy as np
from threading import *
from googletrans import Translator # https://py-googletrans.readthedocs.io/en/latest/
from PyDictionary import PyDictionary

# Translated words dictionary
wordtrans = {}

# Descriptive meaning of words
worddesc = {}

def text_to_word(ptext):
    
    pra = ptext
    
    p = ['.', ',', '"', "'", "_", "-", '*', '^', '&', '#', ':', ";", ')', ']', ">", "<",
        '(', '[', "?", "!", "=", "+", "×", "÷", '/', '~', '%', '}', '{', '$', '|', '`', '¡', "'"]
    # cw=['is ','are ',' am ',' we ', ' you ', " he ",' she ', ' it ',' were ',' was ', ' has ', ' have ', ' do ', ' did ', ' dose ', ' not ', " doesn't ", " don't ", " of ", " for ", " when ", " where ", " whose ", " who ", " what ", " whome ", " be ", " being ", " can ", " could ", " will ", " would ", " must " , ' much ', 'many ', "too. " ,"how " ," in ", 'out ', ' on ', ' top ', ' and ',' this ', ' that ',' those ',' these ', '  ', ' i ']
    cw = ['a', 'an', 'is', 'are', 'am', 'we', 'you', "he", 'she', 'it', 'were', 'was', 'has', 'have', 'do', 'did', 'dose', 'not', "doesn't", "don't", "of", "for", "when", "where", "whose", "who",
        "what", "whome", "be", "being", "can", "could", "will", "would", "must", 'much', 'many', "too", "how", "in", 'out', 'on', 'top', 'and', 'this', 'that', 'those', 'these', '  ', ' i ', 'to', 'the']
    
    # Replace " I " and "I " by "".
    pra = pra.replace(" I ", " ")
    pra = pra.replace("I ", " ")
    # print(pra)
    
    # remove numbers
    for i in range(10):
        pra = pra.replace(str(i), "")
    
    # remove punctuations
    for i in p:
        pra = pra.replace(i, "").lower()
    
    # make list
    npra = pra.split(' ')
    
    # remove "" (space)
    for i in range(npra.count("")):
        npra.remove("")
    
    # unique element and ignoring repeted elements from back.
    numpyarr = np.array(npra)
    u,idx= np.unique(numpyarr, return_index=True)
    numpyarr = u[np.argsort(idx)]
    
    # remove comman words
    for i in cw:
        numpyarr = numpyarr[numpyarr != i]
    
    # numpy array to python list
    npra = list(numpyarr)
    
    # Final Output:
    # print(npra)
    return npra


class WordsMeaning(Thread):
    def __init__(self, word, lang):
        super().__init__()
        self.word = word
        self.lang = lang

    def run(self):
        tr = Translator()
        word_translated_meaning = tr.translate(self.word, dest=self.lang)
        pydict = PyDictionary()
        word_descriptive_meaning = pydict.meaning(self.word, disable_errors=True)
        wordtrans[self.word] = word_translated_meaning.text
        if word_descriptive_meaning != None:
            worddesc[str(self.word)+ ": " +str(word_translated_meaning.text)] = word_descriptive_meaning
        else:
            worddesc[str(self.word)+ ": " +str(word_translated_meaning.text)] = self.word


class GetMeningDictClass:
    def getMeaningDict(self,ptext,lang="gu"):
        global wordtrans 
        global worddesc
        worddesc = {}
        wordtrans = {}
        npra = text_to_word(ptext)
        thredList = [WordsMeaning(word, lang) for word in npra]
        for i in thredList:
            i.start()
        for i in thredList:
            i.join()
        
        wordtrans1 = {key: wordtrans[key] for key in npra}
        worddesc1 = {key: worddesc[str(key) + ": " + str(wordtrans1[key])] for key in npra}
        
        return wordtrans1, worddesc1