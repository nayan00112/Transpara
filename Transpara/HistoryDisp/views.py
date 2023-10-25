from django.shortcuts import render
from Translate.models import UserData
from django.http import HttpResponse
# Create your views here.


def history(request):
    if request.user.is_authenticated:
        try:
            ud = UserData.objects.filter(user_id = request.user.id).order_by('-id')
            return render(request, "history/history.html", {"ud": ud, "active_history":"active"})
        except:
            return HttpResponse('<h1 style="color:red;">Somthing Error</h1>')
    else:
        return HttpResponse('<h1 style="color:red;">Somthing Error</h1>')
def delete_histry(request):
    if request.user.is_authenticated:
        try:
            if request.method == "POST":
                user_id = request.POST["ID_Delete"]
                UserData.objects.get(id = user_id).delete()
                ud = UserData.objects.filter(user_id = request.user.id)
                return render(request, "history/history.html", {"ud": ud, "active_history":"active"})
        except:
            return HttpResponse('<h1 style="color:red;">Somthing Error</h1>')
    else:
        return HttpResponse('<h1 style="color:red;">Somthing Error</h1>')