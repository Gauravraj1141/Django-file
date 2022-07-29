from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    uppercase = request.POST.get('uppercase','off')
    newlineremove = request.POST.get('newlineremove','off')
    spaceremover = request.POST.get('spaceremover','off')
    Character_Count = request.POST.get('Character_Count','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed =  analyzed + char
        params = {'purpose': 'Removed Punctutaions', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed

    if uppercase  == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+ char
            analyzed = analyzed.upper()
        params = {'purpose': 'Upper case', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed


    if newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed+char
        params = {'purpose': 'Newlineremove', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed

    if spaceremover == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char
            analyzed = analyzed.replace("  ", " ")
        params = {'purpose': 'Newlineremove', 'analyzed_text': analyzed}
        djtext = analyzed

    if Character_Count == "on":
        analyzed = 0
        for char in djtext:
            analyzed = analyzed + len(char)
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}



    if (removepunc != "on" and uppercase != "on" and newlineremove != "on" and spaceremover!="on" and Character_Count != "on"):
        return HttpResponse (djtext)

    return render(request,'analyze.html',params)



