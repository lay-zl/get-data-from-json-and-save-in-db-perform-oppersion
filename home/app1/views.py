import urllib

from django.shortcuts import render,HttpResponse
import json
from django.core.paginator import Paginator
from .models import ApiData
# Create your views here.
file_path = r'C:\Users\dagad\Downloads\jsondata.json'

with open(file_path,encoding='iso-8859-1') as f: #context manager
    dt = json.load(f)
data_r=set()
def all(req):
    '''
    function return all field with 5 row as used pagination
    '''
    global data_r
    regi = []
    for i in dt:
        regi.append(i['region'])
    data_r = set(regi)
    global data_s
    sect = []
    for i in dt:
        sect.append(i['sector'])
    data_s = set(sect)

    c = []
    for i in dt:
        c.append(i['country'])
    data_c = set(c)

    t = []
    for i in dt:
        t.append(i['topic'])
    data_t = set(c)



    contact_list = dt
    paginator = Paginator(contact_list, 5)  # Show 25 contacts per page.

    page_number = req.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(req,'home.html',{"data": page_obj,'t':data_t,
                                   'c':data_c,
                                   's':data_s,'r':data_r
                                   })


def country(req):
    if req.GET.get('region')== 'choose Region':
        pass
    if req.GET.get('region') in data_r and  req.GET.get('sector')== 'choose sector':  #choose sector
        d= req.GET.get('region')
        # print('region',req.GET)
        # print('region',req)
        # print('region',req.GET.get('sector'))
        data=ApiData.objects.filter(region=d)
        return render(req, 'country.html', {'data': data, 'd': d, 'r': data_r})
    if req.GET.get('sector') and req.GET.get('region') =='choose Region' :
        d= req.GET.get('sector')
        # print('sector',d)
        # print(req)
        # print(req.GET)
        data=ApiData.objects.filter(sector=d)
        return render(req, 'sector wise.html', {'data': data, 'd': d })
    if req.GET.get('region') and req.GET.get('sector'):
        d = req.GET.get('region')
        d1 = req.GET.get('sector')
        # print(d)
        # print(d1)
        data = ApiData.objects.filter(sector=d1,region=d)
        print(data)
        return render(req, 'country and sector wise.html', {'data': data, 'd': d,'d1':d1, 'r': data_r})



def home(req):
    return render(req,'front.html')

def sector(req):
    l=[]
    for i in dt:
        l.append(i['sector'])
    data = set(l)
    n = len(data)
    return render(req,'sector.html',{'n':n})


def region(req):
    l = []
    for i in dt:
        l.append(i['region'])
    data = set(l)
    n = len(data)
    return render(req,'region.html',{'n':n})


def Constructionr(req):
    l=[]
    for i in dt:
        if i['sector'] == 'Construction':
            l.append(i)
    return render(req,'Construction.html',{'data':l})



def financial_services_sector(req):
    l=[]
    for i in dt:
        if i['sector'] == 'Financial services':
            l.append(i)
    return render(req,'financial_services_sector.html',{'data':l})

def support_services(req):
    l=[]
    for i in dt:
        if i['sector'] == 'Support services':
            l.append(i)
    return render(req,'Support services.html',{'data':l})

def environment(req):
    l=[]
    for i in dt:
        if i['sector'] == 'Environment':
            l.append(i)
    return render(req,'Environment.html',{'data':l})

def Information_Technology(req):
    l=[]
    for i in dt:
        if i['sector'] == 'Information Technology':
            l.append(i)
    return render(req,'Information Technology.html',{'data':l})

def Energy(req):
    l=[]
    for i in dt:
        if i['sector'] == 'Energy':
            l.append(i)
    return render(req,'Energy.html',{'data':l})

def Healthcare(req):
    l=[]
    for i in dt:
        if i['sector'] == 'Healthcare':
            l.append(i)
    return render(req,'Healthcare.html',{'data':l})

def Tourism_hospitality(req):
    l=[]
    for i in dt:
        if i['sector'] == 'Tourism & hospitality':
            l.append(i)
    return render(req,'Tourism & hospitality.html',{'data':l})

def Media_entertainment(req):
    l=[]
    for i in dt:
        if i['sector'] == 'Media & entertainment':
            l.append(i)
    return render(req,'Media & entertainment.html',{'data':l})

def Security(req):
    l=[]
    for i in dt:
        if i['sector'] == 'Security':
            l.append(i)
    return render(req,'Security.html',{'data':l})

def Food_agriculture(req):
    l=[]
    for i in dt:
        if i['sector'] == 'Food & agriculture':
            l.append(i)
    return render(req,'Food & agriculture.html',{'data':l})

def Manufacturing(req):
    l=[]
    for i in dt:
        if i['sector'] == 'Manufacturing':
            l.append(i)
    return render(req,'Manufacturing.html',{'data':l})

def Retail(req):
    l=[]
    for i in dt:
        if i['sector'] == 'Retail':
            l.append(i)
    return render(req,'Retail.html',{'data':l})

def Transport(req):
    l=[]
    for i in dt:
        if i['sector'] == 'Transport':
            l.append(i)
    return render(req,'Transport.html',{'data':l})

def Government(req):
    l=[]
    for i in dt:
        if i['sector'] == 'Government':
            l.append(i)
    return render(req,'Government.html',{'data':l})

def Aerospace_defence(req):
    l=[]
    for i in dt:
        if i['sector'] == 'Aerospace & defence':
            l.append(i)
    return render(req,'Aerospace & defence.html',{'data':l})

def Water(req):
    l=[]
    for i in dt:
        if i['sector'] == 'Water':
            l.append(i)
    return render(req,'Water.html',{'data':l})

def Automotive(req):
    l=[]
    for i in dt:
        if i['sector'] == 'Automotive':
            l.append(i)
    return render(req,'Automotive.html',{'data':l})

#region

def Southern_Africa(req):
    l=[]
    for i in dt:
        if i['region'] == 'Southern Africa':
            l.append(i)
    return render(req, 'Southern Africa.html', {'data': l})

def South_America(req):
    l=[]
    for i in dt:
        if i['region'] == 'South America':
            l.append(i)
    return render(req, 'South America.html', {'data': l})

def Europe(req):
    l=[]
    for i in dt:
        if i['region'] == 'Europe':
            l.append(i)
    return render(req, 'Europe.html', {'data': l})

def Africa(req):
    l=[]
    for i in dt:
        if i['region'] == 'Africa':
            l.append(i)
    return render(req, 'Southern Africa.html', {'data': l})

def Southern_Europe(req):
    l=[]
    for i in dt:
        if i['region'] == 'Southern Europe':
            l.append(i)
    return render(req, 'Southern Europe.html', {'data': l})

def Oceania(req):
    l=[]
    for i in dt:
        if i['region'] == 'Oceania':
            l.append(i)
    return render(req, 'Oceania.html', {'data': l})

def Northern_Europe(req):
    l=[]
    for i in dt:
        if i['region'] == 'Northern Europe':
            l.append(i)
    return render(req, 'Northern Europe.html', {'data': l})

def Northern_America(req):
    l=[]
    for i in dt:
        if i['region'] == 'Northern America':
            l.append(i)
    return render(req, 'Northern America.html', {'data': l})

def Eastern_Africa(req):
    l=[]
    for i in dt:
        if i['region'] == 'Eastern Africa':
            l.append(i)
    return render(req, 'Eastern Africa.html', {'data': l})

def Western_Asia(req):
    l=[]
    for i in dt:
        if i['region'] == 'Western Asia':
            l.append(i)
    return render(req, 'Western Asia.html', {'data': l})

def South_Eastern_Asia(req):
    l=[]
    for i in dt:
        if i['region'] == 'South-Eastern Asia':
            l.append(i)
    return render(req, 'South-Eastern Asia.html', {'data': l})

def World(req):
    l=[]
    for i in dt:
        if i['region'] == 'World':
            l.append(i)
    return render(req, 'World.html', {'data': l})

def Asia(req):
    l=[]
    for i in dt:
        if i['region'] == 'Asia':
            l.append(i)
    return render(req, 'Asia.html', {'data': l})

def Southern_Asia(req):
    l=[]
    for i in dt:
        if i['region'] == 'Southern Asia':
            l.append(i)
    return render(req, 'Southern Asia.html', {'data': l})

def Eastern_Europe(req):
    l=[]
    for i in dt:
        if i['region'] == 'Eastern Europe':
            l.append(i)
    return render(req, 'Eastern Europe.html', {'data': l})

def Central_Africa(req):
    l=[]
    for i in dt:
        if i['region'] == 'Central Africa':
            l.append(i)
    return render(req, 'Central Africa.html', {'data': l})

def Western_Africa(req):
    l=[]
    for i in dt:
        if i['region'] == 'Western Africa':
            l.append(i)
    return render(req, 'Western Africa.html', {'data': l})

def Western_Europe(req):
    l=[]
    for i in dt:
        if i['region'] == 'Western Europe':
            l.append(i)
    return render(req, 'Western Europe.html', {'data': l})

def Northern_Africa(req):
    l=[]
    for i in dt:
        if i['region'] == 'Northern Africa':
            l.append(i)
    return render(req, 'Northern Africa.html', {'data': l})

def Central_Asia(req):
    l=[]
    for i in dt:
        if i['region'] == 'Central Asia':
            l.append(i)
    return render(req, 'Central Asia.html', {'data': l})

def Central_America(req):#Central America
    l = []
    for i in dt:
        if i['region'] == 'Central America':
            l.append(i)
    return render(req, 'Central America.html', {'data': l})
############################################################
def show(req):
    label = []
    data = []
    for i in dt:
        d = i['intensity']
        if str(d).isdigit():
            data.append(d)

    print(label)
    print(data)
    return render(req,'show.html',{
        'label':label,
        'data':data
    })
# import matplotlib.pyplot as plt
from collections import Counter
from io import BytesIO
import base64
import io
# import matplotlib
# matplotlib.use('Agg')
# import numpy as np
# def country_count_show(req):
#     country = []
#     for i in dt:
#         country.append(i['country'])
#     data = Counter(country)
#     x = np.linspace(0, 2 * np.pi, 200)
#     y = np.sin(x)
#
#     fig, ax = plt.subplots()
#     ax.plot()
#     plt.show()
# def country_count_show(req):
#     country = []
#     for i in dt:
#         country.append(i['country'])
#     data = Counter(country)
#
#     labels = list(data.keys())
#     values = list(data.values())
#     plt.plot(labels,values)
#
#     plt.title('Line Chart')
#     plt.xlabel('X-axis')
#     plt.ylabel('Y-axis')
#
#     # Save the chart as a PNG image
#     chart_image = BytesIO()
#     plt.savefig(chart_image, format='png')
#     chart_image.seek(0)
#     response = HttpResponse(chart_image, content_type='image/png')
#     return response
#     # return render(req,'country_count.html', {'data': uri,'c':data})

import matplotlib.pyplot as plt


def sample(req):
    inte = []
    for i in dt:
        if i['intensity'] == '':
            pass
        else:
            inte.append((i['intensity']))
    print(inte)
    new = []
    print(type(inte[1]))
    print(type(inte[0]))

    # plt.pie(inte,autopct='%0.1f%%')
    # plt.show()

    plt.plot(inte)
    return HttpResponse('hi')
