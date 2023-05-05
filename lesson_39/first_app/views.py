from django.shortcuts import render


def test1(request):
    return render(request, 'testing1.html')

