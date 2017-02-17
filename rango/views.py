from django.shortcuts import render

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    return render(request, 'rango/index.html', context=context)

def about(request):
    context = {'boldmessage': "My name is Freida. That's all you have to know."}

    return render(request, 'rango/about.html', context=context)