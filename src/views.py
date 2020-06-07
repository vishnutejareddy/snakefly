from django.shortcuts import render, get_object_or_404,redirect
from .models import Event,Upcoming_Event,Finance
from django.http import JsonResponse
from collections import OrderedDict
from .fusioncharts import FusionCharts


# Create your views here.
def index(request):
    all_events = list(Event.objects.values())
    return render(request, 'index.html', {'body': True, 'all_events': all_events})

def about(request):
    return render(request, 'index.html', {'about': True})

def members(request):
    return render(request, 'index.html', {'members': True})

def events(request):
    all_events = list(Event.objects.values())
    return render(request, 'index.html', {'events': True, 'all_events': all_events})

def read_more(request):
    return render(request, 'index.html', {'read_more': True})

def read_event(request,id):
    all_events = list(Event.objects.values())
    event = Event.objects.get(id=id)
    return render(request, 'index.html', {'read_event':True, 'event': event, 'all_events': all_events})

def volunter(request):
    all_volunter_events = list(Upcoming_Event.objects.values())
    return render(request, 'index.html', {'volunter':True, 'all_events':all_volunter_events})

def read_volunter_event(request,id):
    all_volunter_events = list(Upcoming_Event.objects.values())
    event = Upcoming_Event.objects.get(id=id)
    return render(request, 'index.html', {'read_event_vol':True, 'event': event, 'all_events': all_volunter_events})

def financial_report(request):
    dataSource = OrderedDict()
    dataSource["data"] = []
    # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.

    for finance in Finance.objects.raw('SELECT * FROM src_finance'):
        dataSource["data"].append({"label": finance.monthpublished(), "value": finance.amount_exp})

    chartConfig = OrderedDict()
    chartConfig["caption"] = "Financial Report for the Year 2020"
    chartConfig["subCaption"] = "In Rupees vs Month"
    chartConfig["xAxisName"] = "Month"
    chartConfig["yAxisName"] = "Rupees"
    chartConfig["numberSuffix"] = "K"
    chartConfig["theme"] = "fusion"
    chartConfig['bgColor'] = "#17a2b8"
    chartConfig['labelDisplay'] = "rotate"

    dataSource["chart"] = chartConfig
    column2D = FusionCharts("column3d", "myFirstChart", "900", "600", "myFirstchart-container", "json", dataSource)
    return render(request, 'index.html', {'financial_report': True, 'output': column2D.render()})

def our_projects(request):
    all_projects = list(Event.objects.values())
    return render(request, 'index.html', {
        'my_projects': True,
        'all_events': all_projects
    })

def raise_funds(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'index.html', {'contact':True})

def redirect_index(request):
    return redirect('/')