from django.shortcuts import render
from Translate.models import UserData
from django.http import Http404
# Create your views here.


def history(request):
    if request.user.is_authenticated:
        try:
            ud = UserData.objects.filter(user_name = request.user)
            return render(request, "history/history.html", {"ud": ud})
        except:
            return Http404
    else:
        return Http404

    