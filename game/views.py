from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def cards_show(request):
    return render(request, 'cards_show.html', {})


def card_example(request):
    return render(request, 'example.html', {})


def role_distribution(request):
    return render(request, 'role_distribution.html', {})


def role(request):
    return render(request, 'role.html', {})


def poker_distribution(request):
    return render(request, 'poker_distribution.html', {})


def data_note(request):
    group_type = request.GET.get('group_type')
    return render(request, 'data_note.html', {'type': int(group_type)})

