from django.shortcuts import render
# from .models import 
from .utils import get_plot
# Create your views here.
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import json
import os
from django.http import HttpResponse, JsonResponse
from .models import continent_factor
def main_view(request):
    parameter = request.GET.get('parameter')
    qs = continent_factor.objects.filter(factor__contains=parameter)
    x = [x.대륙 for x in qs]
    y = [float(y.death_per_100000) for y in qs]
    df = pd.read_json('dataframe.json')
    
    factor = list(df['variable'].unique())
    chart = get_plot(x,y,'대륙별 연평균 %s 사망자수 그래프'%parameter)
    return render(request, 'world/main_view.html', context={'x':x,'y':y, 'chart':chart, 'factors':factor, 'parameter':parameter})









# def input_json(request):
#     # print(1)
#     df = pd.read_json('dataframe.json')
#     for i in range(len(df)):
#         대륙 = df.iloc[i,0]
#         factor = df.iloc[i,1]
#         die_per = df.iloc[i,2]
#         continent_factor(대륙=대륙, factor=factor, death_per_100000=die_per).save()
#     return HttpResponse('ok')
