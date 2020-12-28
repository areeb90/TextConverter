# I HAVE CREATED THIS FILE

# views.py

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index1.html')

    # return HttpResponse("Home")

def analyzed(request):

    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    lowerCase = request.POST.get('lowerCase', 'off')
    NoOfChar = request.POST.get("NoOfChar", 'off')


    # cheak which cheakbox is on
    if removepunc == "on":
        punctuations = '''!()-[{]};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {"purpose": "REMOVE PUNCTUATIONS" , "analyzed_text": analyzed}
        return render(request, "analyzed1.html", params)


    elif (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed =analyzed + char.upper()

        params ={"purpose": "UPPERCASE", "analyzed_text": analyzed}
        return render(request, "analyzed1.html", params)
    

    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char!= "\n" and char!="\r":
                analyzed = analyzed + char

        params ={"purpose": "NEW LINE REMOVER", "analyzed_text": analyzed}
        return render(request, "analyzed1.html", params)
            

    elif (extraspaceremover =="on"):
        analyzed= ""
        for index, char in enumerate(djtext):
            if not(djtext[index]=="" and djtext[index+1]==""):
                analyzed = analyzed + char

        params ={"purpose": "EXTRA SPACE REMOVER", "analyzed_text": analyzed}
        return render(request, "analyzed1.html", params)

    elif (lowerCase == 'on'):
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.lower()

        params ={"purpose": "LOWERCASE", "analyzed_text": analyzed}
        return render(request, "analyzed1.html", params)

    elif (NoOfChar=='on'):
        analyzed = 0
        for i in range(len(djtext)):
            i+=1
            analyzed = analyzed + i
            

        params ={"purpose": "No Of Characters", "analyzed_text": analyzed}
        return render(request, "analyzed1.html", params)
        



    else:
        return HttpResponse('ERROR')





# def removepunc(request):
#     #Get the text
#     djtext = request.POST.get('text', 'default')
#     print(djtext)
#     #Analyze the text
#     return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remove first")


# def spaceremove(request):
#     return HttpResponse("space remover back")

# def charcount(request):
#     return HttpResponse("charcount ")