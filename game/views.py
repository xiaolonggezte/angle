import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from game.models import DataModel


def index(request, type_id):
    type_id = int(type_id)
    if type_id < 1 or type_id > 4:
        return render(request, 'error.html', {})
    return render(request, 'index.html', {
        'type': type_id,
    })


def cards_show(request):
    return render(request, 'cards_show.html', {})


def card_example(request):
    group_type = request.GET.get('type')
    return render(request, 'game.html', {
        'type': int(group_type)
    })


def role_distribution(request):
    return render(request, 'role_distribution.html', {})


def role(request):
    return render(request, 'role.html', {})


def poker_distribution(request):
    return render(request, 'poker_distribution.html', {})


def data_note(request):
    group_type = request.GET.get('type')
    ans = request.GET.get('ans')
    is_cheat = request.GET.get('is_cheat')
    return render(request, 'data_note.html', {
        'type': int(group_type) if group_type else 1,
        'ans': ans,
        'is_cheat': is_cheat,
    })


@csrf_exempt
def update_db(request):
    flag = False
    is_cheat = request.POST.get('is_cheat')

    is_cheat = int(is_cheat)
    try:
        DataModel.objects.create(
            ip=request.POST.get('ip'),
            type=request.POST.get('type'),
            ans=request.POST.get('ans'),
            flag=flag,
            input=None,
            is_cheat=True if is_cheat else False,
        )
    except Exception as exc:
        return HttpResponse(content=exc)
    return HttpResponse(content='success')


def finished(request):
    return render(request, 'finished.html', {})


def data_list(request):
    datas = DataModel.objects.all()
    return render(request, 'data_list.html', {'datas': datas})


def alter_mask(request):
    try:
        id = request.GET.get('id')
        mask = request.GET.get('mask')
        DataModel.objects.filter(pk=id).update(
            marks=mask,
        )
    except Exception as ex:
        return HttpResponse(content='failed')
    return HttpResponse(content='success')


def love_show(request):
    return render(request, 'love.html', {})


