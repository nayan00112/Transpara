from django.shortcuts import render
from django.http import HttpResponse

from googletrans import Translator


# Create your views here.
def get_gujarati_meaning(word, lang):
            translator = Translator()
            translation = translator.translate(word, src='en', dest=lang)
            return translation.text

def trans(request):
    if request.method =='POST':
        ptext = request.POST.get('pra')
        lang = request.POST.get('lang')
        pra = ptext

        p = ['.', ',', '"', "'", "_", "-", '*', '^', '&', '#', ':', ";", ')', ']', ">", "<",
            '(', '[', "?", "!", "=", "+", "×", "÷", '/', '~', '%', '}', '{', '$', '|', '`', '¡', "'"]
        # cw=['is ','are ',' am ',' we ', ' you ', " he ",' she ', ' it ',' were ',' was ', ' has ', ' have ', ' do ', ' did ', ' dose ', ' not ', " doesn't ", " don't ", " of ", " for ", " when ", " where ", " whose ", " who ", " what ", " whome ", " be ", " being ", " can ", " could ", " will ", " would ", " must " , ' much ', 'many ', "too. " ,"how " ," in ", 'out ', ' on ', ' top ', ' and ',' this ', ' that ',' those ',' these ', '  ', ' i ']
        cw = ['a', 'an', 'is', 'are', 'am', 'we', 'you', "he", 'she', 'it', 'were', 'was', 'has', 'have', 'do', 'did', 'dose', 'not', "doesn't", "don't", "of", "for", "when", "where", "whose", "who",
            "what", "whome", "be", "being", "can", "could", "will", "would", "must", 'much', 'many', "too", "how", "in", 'out', 'on', 'top', 'and', 'this', 'that', 'those', 'these', '  ', ' i ', 'to', 'the']
        # Replace " I " by ""
        pra = pra.replace(" I ", " ")
        # print(pra)

        # remove numbers
        for i in range(10):
            pra = pra.replace(str(i), "")

        # remove punctuations
        for i in p:
            pra = pra.replace(i, "").lower()

        # print(pra)

        # make list
        npra = pra.split(' ')

        # remove ""
        for i in range(npra.count("")):
            npra.remove("")

        # remove repeation
        for i in npra:
            for j in range(npra.count(i)-1):
                npra.remove(i)

        # remove cw
        i1 = 0
        for i in cw:
            i1 = npra.count(i)
            while i1 > 0:
                npra.remove(i)
                i1 -= 1

        # Final Output:
        # print(npra)
        wordDic = {}
        try:

            for i in npra:
                english_word = i
                gujarati_meaning = get_gujarati_meaning(english_word, lang)
                # print(f"{english_word}: {gujarati_meaning}")
                wordDic[english_word] = gujarati_meaning
        except:
                wordDic = {"Error ":"404 Not Found, network error."}
        return render(request, "Transpara/index.html", {"praText": ptext, "wd" : wordDic})

    return render(request, "Transpara/index.html")