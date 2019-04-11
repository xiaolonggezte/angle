import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from game.models import DataModel
GROUP_TYPE_CNT = 0


def index(request):
    return render(request, 'index.html', {
        'type': GROUP_TYPE_CNT % 4 + 1,
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
    global GROUP_TYPE_CNT
    GROUP_TYPE_CNT = GROUP_TYPE_CNT + 1
    ans = request.GET.get('ans')
    return render(request, 'data_note.html', {
        'type': int(group_type) if group_type else 1,
        'ans': ans
    })


@csrf_exempt
def update_db(request):
    flag = request.POST.get('flag')
    try:
        DataModel.objects.create(
            ip=request.POST.get('ip'),
            type=request.POST.get('type'),
            ans=request.POST.get('ans'),
            flag=True if flag == 'true' else False,
            input=request.POST.get('input'),
        )
    except:
        return HttpResponse(content='failed')
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



