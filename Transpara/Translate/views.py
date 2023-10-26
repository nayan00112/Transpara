from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.contrib import messages
import json
from datetime import datetime
from .models import UserData

from Translate.strtodict import GetMeningDictClass

def trans(request):
    if request.method == 'POST':
        # Get data:
        ptext = request.POST.get('pra')
        # print(ptext)
        lang = request.POST.get('lang')

        wordDic = {}
        wordMin = {}
        
        wordDic.clear()
        wordMin.clear()

        try:
            obj1 = GetMeningDictClass()
            wordDic,wordMin = obj1.getMeaningDict(ptext, lang)
            # print(wordDic,wordMin)
        except Exception as e:
            messages.error(request, 'Somthing wrong! ' )

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
            # day month year Hour Minute Second
            dateandtime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            userJson = {
                "pragraph": ptext.replace('"', '&#8243;'),
                "words_language": lenguagesList[lang],
                "words": wordDic,
            }

            jstr = json.dumps(userJson)
            # jsondata = json.loads(jstr)
            # print(jstr)
            # print()
            # print(jsondata)

            # ud = UserData(user_id=uid, user_data=jsondata,
            #               dateandtime=dateandtime)
            ud = UserData(user_id=uid, user_data=jstr,
                          dateandtime=dateandtime)
            ud.save()

        return render(request, "Translate/index.html", {"praText": ptext, "wd": wordDic, "wdm": wordMin, "l1": textLeng, "active_home": "active"})

    return render(request, "Translate/index.html", {"active_home": "active"})
