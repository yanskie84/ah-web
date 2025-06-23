from django.shortcuts import render

def home(request):
    return render(request, "homebase.html")

def python(request):
    return render(request, "modul/modul1.html")

def gui(request):
    return render(request, "modul/modul2.html")

def statis(request):
    return render(request, "modul/modul3.html")

def dinamis(request):
    return render(request, "modul/modul4.html")
