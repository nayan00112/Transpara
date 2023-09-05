from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from googletrans import Translator
from PyDictionary import PyDictionary
from django.contrib import messages
import json
from datetime import datetime
from .models import UserData

# Create your views here.


def get_meaning(word, lang):
    translator = Translator()
    translation = translator.translate(word, src='en', dest=lang)
    return translation.text


def trans(request):
    if request.method == 'POST':
        # dictionary
        dictionary = PyDictionary()

        # Filteration process:

        # Get data:
        ptext = request.POST.get('pra')
        lang = request.POST.get('lang')

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

        # print(pra)

        # make list
        npra = pra.split(' ')

        # remove "" (space)
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

        # Now, Translatation work start here...
        wordDic = {}
        wordMin = {}
        try:
            for i in npra:
                english_word = i
                meaning = get_meaning(english_word, lang)
                # print(f"{english_word}: {gujarati_meaning}")
                wordDic[english_word] = meaning
                wordMin[english_word + ": " +
                        meaning] = dictionary.meaning(english_word)

        except:
            messages.error(request, 'Network error')

        lenguagesList = {
            "hi": "Hindi",
            "gu": "Gujarati",
            "ta": "Tamil",
            "te": "Telugu",
            "de": "German",
            "it": "Italian",
            "ar": "Arabic",
            "ru": "Russian",
            "ko": "Korean",
            "fr": "French",
            "es": "Spanish",
            "ja": "Japanese"
        }

        textLeng = lang
        for l in lenguagesList:
            if lang == l:
                textLeng = lenguagesList[l]
                break

        # if user is authencated then save data to the database. (including pragraph)
        if request.user.is_authenticated:
            # plane is first, convert data to the json formate and store on db.
            uid = request.user.id
            print(uid)
            # day month year Hour Minute Second
            dateandtime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            userJson = {
                "pragraph": ptext,
                "words_language": lenguagesList[lang],
                "words": wordDic,
            }

            jstr = json.dumps(userJson)
            jsondata = json.loads(jstr)

            ud = UserData(user_id=uid, user_data=jsondata,
                          dateandtime=dateandtime)
            ud.save()

        return render(request, "Translate/index.html", {"praText": ptext, "wd": wordDic, "wdm": wordMin, "l1": textLeng, "active_home":"active"})

    return render(request, "Translate/index.html", {"active_home":"active"})
