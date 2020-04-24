from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse

from mysite.core.models import City,daily,avrage,manths,week


def home(request):
    return render(request, 'home.html')
def homeAR(request):
    return render(request, 'homeAR.html')



def population_chart(request):
    labels = []
    data = []

    queryset = City.objects.values('country__name').annotate(country_population=Sum('population')).order_by('-country_population')
    for entry in queryset:
        labels.append(entry['country__name'])
        data.append(entry['country_population'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def pie_chart(request):
    labels = []
    data = []

    queryset = City.objects.order_by('-population')[:5]
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })


def daily_chart(request):
    labels1 = []
    data1 = []

    queryset = daily.objects.all()
    for entry in queryset:
        labels1.append(entry.name)
        data1.append(entry.sick)
    
    return JsonResponse(data={
        'labels1': labels1,
        'data1': data1,
    })


def avreg_chart(request):
    labels2 = []
    data2 = []
    per = []

    queryset = avrage.objects.all()
    for entry in queryset:
        labels2.append(entry.name)
        data2.append(entry.typ)
    per =(data2[0]/data2[0])*100


    return JsonResponse(data={
        'labels2': labels2,
        'data2': data2,
        'per': per,
    })


def manths_chart(request):
    labels3 = []
    data3 = []

    queryset = manths.objects.all()
    for entry in queryset:
        labels3.append(entry.name)
        data3.append(entry.count)

    return JsonResponse(data={
        'labels3': labels3,
        'data3': data3,
    })


def week_chart(request):
    labels4 = []
    data4 = []

    queryset = week.objects.all()
    for entry in queryset:
        labels4.append(entry.name)
        data4.append(entry.num)

    return JsonResponse(data={
        'labels4': labels4,
        'data4': data4,
    })



