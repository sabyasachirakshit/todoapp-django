from django.shortcuts import render
def todoappView(request):
    return render(request, 'index.html')