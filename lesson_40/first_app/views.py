from django.shortcuts import render
from .models import Notes
content = {"note": Notes.objects.all()}
def test1(request):
    return render(request, 'testing1.html', content)

