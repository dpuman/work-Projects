from django.shortcuts import render

# Create your views here.


def home(request):
    print('From home View')
    return render(request, 'blog/home.html')


def about(request):
    print('From About View')
    return render(request, 'blog/about.html')
