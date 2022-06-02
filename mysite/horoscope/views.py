from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

zodiac_dic = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}


# Create your views here.


def index(request):
    # zodiacs=', '.join(list(zodiac_dic)

    li_el = ''
    for zodi in zodiac_dic:
        redirect_path = reverse('horoscope-name', args=[zodi])
        li_el += f"<li> <a href={redirect_path}> {zodi.title()} </a></li>    "
    response = f"<ul> {li_el} </ul>"
    return HttpResponse(response)


def get_zodiac(request, zodiac: str):
    description = zodiac_dic.get(zodiac)
    if description:
        return HttpResponse(f"Знак зодиака {description}")
    else:
        return HttpResponseNotFound(f"Не известный знак зодиака {zodiac}")


def get_zodiac_by_number(request, zodiac: int):
    if 0 < zodiac < 13:
        redirect_url = reverse('horoscope-name', args=(list(zodiac_dic)[zodiac - 1],))

        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponse(f'This is number {zodiac}')
