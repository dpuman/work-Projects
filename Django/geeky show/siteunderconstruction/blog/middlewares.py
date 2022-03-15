from django.shortcuts import render


class MyUnderConstruction:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('Before View')
        response = render(request, 'blog/underc.html')
        print('after View')
        return response
