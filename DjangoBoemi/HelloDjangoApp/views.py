from django.shortcuts import render

# Create your views here.
def HelloDjangoApp(request):
    return render(request, 'about.html', {})

def about(request):
    return render(
        request,
        "HelloDjangoApp/about.html",
        {
            'title' : "About HelloDjangoApp",
            'content': "Example app page for Django."
            }
        )