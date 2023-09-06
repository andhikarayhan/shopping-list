from django.shortcuts import render


# Create your views here.
def show_main(request):
    context = {
        'name': 'Andhika Finnanda Rayhan',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)